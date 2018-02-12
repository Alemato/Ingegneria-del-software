#ifndef UPDATE_H_
#define UPDATE_H_

#include <string>
#include <stdio.h>
#include <map>
#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
#include "robotTree.h"
#include <math.h>
#include <thread>
#include "./clusterJson.h"
#include "./irEngine.h"
#include "./parameters.h" // contains system configuration parameters
#include "./json.h"
#include <tbb/concurrent_queue.h> // tbb library to manipulate concurrent_queue
#include <fstream>


//queue holding messages
tbb::concurrent_queue<nlohmann::json> jsonQueue;

bool busy = false;
bool updateComplete = true;
bool consumer = false;



/* Prototypes */
void consumeQueue();
void createJson(nlohmann::json);


void systemUpdate(){

    int rCount = 0;
    int totalBotIr = 0;
    updateComplete = false;

    /*

    //start consumer is id died
        if(!consumer){
            
            std::thread jsonConsumer(consumeQueue);
            jsonConsumer.detach();
        
        } 
    
    */

    //for each area
    for(map<string,clusters>::iterator it1 = general.begin(); it1 != general.end(); ++it1) {
        
        //for each cluster in area
        for(map<string,robots>::iterator it2 = (general[it1->first]).begin(); it2 != general[it1->first].end(); ++it2) {        
            
            //create temporary json
            nlohmann::json j = nullptr;
            
            //add area name
            if((it1->first) != "") j["AreaName"] = it1->first;
            
            //add cluster name
            if((it2->first) != "") j["ClusterName"] = it2->first;
            
            //used to calc cluster IR
            rCount = 0;
            totalBotIr = 0;


            //for each robot in cluster
            for(map<string,sigMap>::iterator it3 = ((general[it1->first])[it2->first]).begin(); it3 != ((general[it1->first])[it2->first]).end(); ++it3) {
                    //std::cout << it3->first;
                    int ir = getBotIr(it3->second,getCurrentTime());
                    //std::cout<<": " << getBotIr(it3->second,getCurrentTime())<<" \% \n";
                    
                    //add robots
                    j["Robots"][it3->first] = ir;
                    
                    //for cluster IR
                    rCount++;
                    totalBotIr += ir;

                      
            }
            //add cluster IR

            if(totalBotIr != 0 || rCount != 0) j["ClusterInef"] = (int) round(totalBotIr/rCount);
                //fix 
                else j["ClusterInef"] = 0;
            
            
            //jsonQueue.push(j);
            clock_t t = clock();
            
            createJson(j);

            std::cout<< "Json Creation time: " + std::to_string((double)(clock() - t)/CLOCKS_PER_SEC)<<"\n";
            
            //if(j!=nullptr) 
            //else cout<<"\nj is null\n";


        }
    }

    //update finished
    updateComplete = true;

}

void consumeQueue(){

        while(true){

            if(!busy && jsonQueue.unsafe_size()){

                busy = true;
                nlohmann::json result;
                jsonQueue.try_pop(result);
                std::thread worker1(createJson,result);
                worker1.detach();
                cout<<"\nworking.. \n";

            }
            //cout<<"\nLooping..\n";
        }
      
            cout<<"Thread died \n";
            consumer = false;

}


void createJson(nlohmann::json j){

    string areaName = j["AreaName"];
    string clusterName = j["ClusterName"];
    string nameFile = "Json/";
    string extension = ".json";
    
    /*
    std::ostream stream(nullptr);
    string s = "andonio.json";

    std::ofstream json;
    json.open ("./example.txt");
    json << (j).dump(1) << "\n" << std::endl;
    json.close();
    */

    ofstream json ("/opt/lampp/htdocs/Dashboard/ingegnere/system/pageGenerator/data/" + areaName + clusterName + extension);

    if (json.is_open())
    {
        json << (j).dump(1) << "\n" << std::endl;
        json.close();
    }
    else cout << "Unable to open file";

    busy=false;

    
}

#endif