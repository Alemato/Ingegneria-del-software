#ifndef ROBOTTREE_H_
#define ROBOTTREE_H_
#include <string>
#include <stdio.h>
#include <map>
#include <iostream>
#include <vector>
#include <string.h>
#include <sys/time.h>
#include <unistd.h>
#include "./message.h"
#include "./parameters.h"

using namespace std;
//map of timestamps of a robot
typedef std::map<long,char> sigLineMap;
//single robot
typedef std::map<std::string, sigLineMap> sigMap;
//map robot of a cluster
typedef std::map<std::string,sigMap> robots;
//map of clusters of an area -- each entry ---> (map) list of robots
typedef std::map<std::string,robots> clusters;
//map of areas
typedef std::map<std::string,clusters> areas;

areas general;

//get current system time in ms
long getCurrentTime(){

    struct timeval tp;
    gettimeofday(&tp, NULL);
    return (tp.tv_sec * 1000 + tp.tv_usec / 1000);
}

//aggiungere un area alla mappa generale 

void addArea(std::string areaCode) {

    clusters m;
    general[areaCode] = m;

}

//aggiungere un area alla mappa area 

void addCluster(std::string areaCode,std::string clusterCode) {

    robots r;
    (general[areaCode])[clusterCode] = r;

}


void printRobot(string area, string cluster, string robot){
    
    
    cout << "  Timestamp             Up/Down state \n \n";

    for(int k=0;k<=7;k++){
        
        cout<< "S" << to_string(k)<<"\n";

        sigLineMap currentSig = (((general[area])[cluster])[robot])["s"+to_string(k)];
    
        for(map<long,char>::iterator it = currentSig.begin(); it != currentSig.end(); ++it) {
                    
                   cout << it->first <<" :               " << it->second << "\n";

        }
    cout <<"\n";
    }
}

void printRobotObj(sigMap r){
    
    
    cout << "  Timestamp             Up/Down state \n \n";

    for(int k=0;k<=7;k++){

        cout<< "S" << to_string(k)<<"\n \n";

        sigLineMap currentSig = r["s"+to_string(k)];
    
        for(map<long,char>::iterator it = currentSig.begin(); it != currentSig.end(); ++it) {
                    
                   cout << it->first <<" :               " << it->second << "\n";

        }
    cout <<"\n";
    }
}       

void printRobotInstant(string area, string cluster, string robot,long timestamp){

    cout << ((((general[area])[cluster])[robot])["s1"])[1516903200000];
    cout << ((((general[area])[cluster])[robot])["s2"])[1516903200000];
    cout << ((((general[area])[cluster])[robot])["s3"])[1516903200000];
    cout << ((((general[area])[cluster])[robot])["s4"])[1516903200000];
    cout << ((((general[area])[cluster])[robot])["s5"])[1516903200000];
    cout << ((((general[area])[cluster])[robot])["s6"])[1516903200000];
    cout << ((((general[area])[cluster])[robot])["s7"])[1516903200000];

    

}

//aggiungere un robot alla mappa cluster 

void addRobot(std::string areaCode,std::string clusterCode,std::string robotCode,long timeStamp) {

    //getting current time
    //long timeStamp = getCurrentTime();

    //create sig map of a robot
    sigMap sm = *(new sigMap());

    //adding signal keys and binding to sigLineMaps
    sm["s1"] = *(new sigLineMap());
    sm["s2"] = *(new sigLineMap());
    sm["s3"] = *(new sigLineMap());
    sm["s4"] = *(new sigLineMap());
    sm["s5"] = *(new sigLineMap());
    sm["s6"] = *(new sigLineMap());
    sm["s7"] = *(new sigLineMap());

    //setting all signal UP (1) at current timeStamp
    sm["s1"][timeStamp] = '1';
    sm["s2"][timeStamp] = '1';
    sm["s3"][timeStamp] = '1';
    sm["s4"][timeStamp] = '1';
    sm["s5"][timeStamp] = '1';
    sm["s6"][timeStamp] = '1';
    sm["s7"][timeStamp] = '1';

    //selected single element of a cluster and assignes a signal map
    ((general[areaCode])[clusterCode])[robotCode] = sm;

}

//On new message received update robot sigMap

void updateRobot(sigMap r,Message m){



}

void printByArea(std::string areaCode){

    vector<string> v;
    
    cout<<"Aree Attive:  \n \n";

    for(map<string,clusters>::iterator it = general.begin(); it != general.end(); ++it) {
                v.push_back(it->first);
                cout << it->first << "\n";
    }
    
    v.clear();
    cout<<"\n";

    cout<<"Cluster Attivi in area  "<< areaCode <<" : \n \n";

    for(map<string,robots>::iterator it = (general[areaCode]).begin(); it != general[areaCode].end(); ++it) {
            v.push_back(it->first);
            cout << "" << it->first << "\n";
    }

    v.clear();
    cout<<"\n";

    for(map<string,robots>::iterator it = (general[areaCode]).begin(); it != general[areaCode].end(); ++it) {
            v.push_back(it->first);
            //cout << "\n" << it->first << "\n";
     

    v.clear();
    cout<<"\n";

    cout<<"Robot attivi "<< areaCode << "|" << it->first<<"\n \n";

    for(auto it2 = (it->second).cbegin(); it2 != (it->second).cend(); ++it2)
    {
        std::cout << it2-> first << " " << " \n";
    }

    v.clear();
    cout<<"\n";
    }

}

void createDummyTree(){

    cout<<"\nCreating "<<N_CLUSTERS<<" CLUSTERS with "<<N_ROBOTS<<" ROBOTS each, starting 15 MINUTES before current time. \n\n";
    clock_t tStart;
    
    tStart=clock();
    /*
    do{
        addCluster("A01","C"+to_string(i));
        i++;

    } while(i!=102); 
    */

    for(int j=1;j<=N_CLUSTERS;j++){
    
        for(int k=1;k<=N_ROBOTS;k++){
            
            //addRobot("A1","C"+to_string(j),"R"+to_string(k),getCurrentTime()-(BORN_TIME * 60000));   
            addRobot("A1","C"+to_string(j),"R"+to_string(k),getCurrentTime()-(rand() % 2700000+1));   
        }
    }
    string create = "Build time: " + std::to_string((double)(clock() - tStart)/CLOCKS_PER_SEC) + "\n";
 
    tStart = clock();
    
      
    cout << "System parsing time: " + std::to_string((double)(clock() - tStart)/CLOCKS_PER_SEC) + "\n";
    cout << create;
    //cout << "numero robot attivi: "<< count << "\n \n";

    tStart = clock();
    /*
    if(((general["A01"])["C69"])["R82"] != "") cout <<"risultato: "<<((general["A01"])["C69"])["R82"]<< "\n";
    else cout << "Robot non trovato. \n \n";
    */
    //cout << ((((general["A01"])["C69"])["R82"])["s1"])[getCurrentTime()-2000] << "\n";

    //((general["A01"])["C69"]).find("R1") == ((general["A01"])["C69"]).end();

    //cout << "Element search time: " + std::to_string((double)(clock() - tStart)/CLOCKS_PER_SEC) + "\n\n";

}

void addSingleRobot(){
    static int i=0,j=0;
    addRobot("A1","C"+i,"R"+j,1516903200000);
    i++;
    i++;
    j++;
    sleep(1);
    cout << "added \n";
}
/*
int main(void){

    //addArea("A01");
       
    while(true){
        createDummyTree();
        cin.get();
    }
}
*/

#endif