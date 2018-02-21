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
void createAreaJson(nlohmann::json);


void systemUpdate(){

    int rCount = 0;
    int totalBotIr = 0;
    updateComplete = false;
    
    int cCount = 0;
    int totalClusterIr = 0;

    //create temporary json
    nlohmann::json a = nullptr;



    //for each area
    for(map<string,clusters>::iterator it1 = general.begin(); it1 != general.end(); ++it1) {
    
        //reset for area IR
        cCount = 0;
        totalClusterIr = 0;

        //for each cluster in area
        for(map<string,robots>::iterator it2 = (general[it1->first]).begin(); it2 != general[it1->first].end(); ++it2) {        
            cout<<it1->first<<"-"<<it2->first<<"\n";
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



                    int ir = getBotIr(it3->second,getCurrentTime());
                    
                    
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
            
         

            totalClusterIr += (int) round(totalBotIr/rCount);
            cCount++;           

          
            
            //jsonQueue.push(j);
            clock_t t = clock();
            
            createJson(j);
            
        

            std::cout<< "Json Creation time: " + std::to_string((double)(clock() - t)/CLOCKS_PER_SEC)<<"\n";
            
            //if(j!=nullptr) 
            //else cout<<"\nj is null\n";

        }
        
        //create json aree
        if(totalClusterIr != 0 || cCount != 0) a[it1->first] = (int) round(totalClusterIr/cCount);
            //fix 
            else a[it1->first] = 0;

    }

    createAreaJson(a);
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
    string extension = ".json";

    ofstream json (JSON_PATH + areaName + clusterName + extension);

    if (json.is_open())
    {
        json << (j).dump(1) << "\n" << std::endl;
        json.close();
    }
    else cout << "Unable to open file";

    busy=false;

    
}

void createAreaJson(nlohmann::json j){

    string fileName = "Aree";
    string extension = ".json";

    ofstream json (JSON_PATH + fileName + extension);

    if (json.is_open())
    {
        json << (j).dump(1) << "\n" << std::endl;
        json.close();
    }
    else cout << "Unable to open file";

    busy=false;

    
}

#endif
