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
#include <cstring>

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

void addRobot(std::string areaCode,std::string clusterCode,std::string robotCode,long timeStamp,Message m) {

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
    if(m.S1=="0") sm["s1"][timeStamp-(BORN_TIME*60000)] = '0';
        else sm["s1"][timeStamp-(BORN_TIME*60000)] = '1';

    if(m.S2=="0") sm["s2"][timeStamp-(BORN_TIME*60000)] = '0';
        else sm["s2"][timeStamp-(BORN_TIME*60000)] = '1';
    
    if(m.S3=="0") sm["s3"][timeStamp-(BORN_TIME*60000)] = '0';
        else sm["s3"][timeStamp-(BORN_TIME*60000)] = '1';
    
    if(m.S4=="0") sm["s4"][timeStamp-(BORN_TIME*60000)] = '0';
        else sm["s4"][timeStamp-(BORN_TIME*60000)] = '1';
    
    if(m.S5=="0") sm["s5"][timeStamp-(BORN_TIME*60000)] = '0';
        else sm["s5"][timeStamp-(BORN_TIME*60000)] = '1';

    if(m.S6=="0") sm["s6"][timeStamp-(BORN_TIME*60000)] = '0';
        else sm["s6"][timeStamp-(BORN_TIME*60000)] = '1';
    
    if(m.S7=="0") sm["s7"][timeStamp-(BORN_TIME*60000)] = '0';
        else sm["s7"][timeStamp-(BORN_TIME*60000)] = '1';

    //selected single element of a cluster and assignes a signal map
    ((general[areaCode])[clusterCode])[robotCode] = sm;

}

//On new message received update robot sigMap

void updateRobot(std::string area,std::string cluster,std::string robot,long timeStamp,Message m){
    
    map<long, char>::iterator itr;

    //check if new value is the as the oldest
    itr = ((((general[area])[cluster])[robot])["s1"]).end();
    itr--;
    if(m.S1 == string(1,(itr->second))) {}
        else (((((general[area])[cluster])[robot])["s1"])[timeStamp]) = (m.S1)[0];
    
    itr = ((((general[area])[cluster])[robot])["s2"]).end();
    itr--;
    if(m.S2 == string(1,(itr->second))) {}
        else (((((general[area])[cluster])[robot])["s2"])[timeStamp]) = (m.S2)[0];


    itr = ((((general[area])[cluster])[robot])["s3"]).end();
    itr--;
    if(m.S3 == string(1,(itr->second))) {}
        else (((((general[area])[cluster])[robot])["s3"])[timeStamp]) = (m.S3)[0];

    itr = ((((general[area])[cluster])[robot])["s4"]).end();
    itr--;
    if(m.S4 == string(1,(itr->second))) {}
        else (((((general[area])[cluster])[robot])["s4"])[timeStamp]) = (m.S4)[0];


    itr = ((((general[area])[cluster])[robot])["s5"]).end();
    itr--;
    if(m.S5 == string(1,(itr->second))) {}
        else (((((general[area])[cluster])[robot])["s5"])[timeStamp]) = (m.S5)[0];

    itr = ((((general[area])[cluster])[robot])["s6"]).end();
    itr--;
    if(m.S6 == string(1,(itr->second))) {}
        else (((((general[area])[cluster])[robot])["s6"])[timeStamp]) = (m.S6)[0];

    itr = ((((general[area])[cluster])[robot])["s7"]).end();
    itr--;
    if(m.S7 == string(1,(itr->second))) {}
        else (((((general[area])[cluster])[robot])["s7"])[timeStamp]) = (m.S7)[0];
    
}

void printByArea(std::string areaCode){

    vector<string> v;
    
    cout<<"Aree Attive:  \n \n";

    for(map<string,clusters>::iterator it = general.begin(); it != general.end(); ++it) {
                v.push_back(it->first);
    }
    
    v.clear();
    cout<<"\n";

    cout<<"Cluster Attivi in area  "<< areaCode <<" : \n \n";

    for(map<string,robots>::iterator it = (general[areaCode]).begin(); it != general[areaCode].end(); ++it) {
            v.push_back(it->first);
    }

    v.clear();
    cout<<"\n";

    for(map<string,robots>::iterator it = (general[areaCode]).begin(); it != general[areaCode].end(); ++it) {
            v.push_back(it->first);
     
    v.clear();
    
    }
}

void createDummyTree(){

    cout<<"\nCreating "<<N_AREAS<<" AREAS WITH "<<N_CLUSTERS<<" CLUSTERS AND "<<N_ROBOTS<<" ROBOTS each. \n\n";
    clock_t tStart;
    
    tStart=clock();
    for(int x=1;x<=N_AREAS;x++){
        for(int j=1;j<=N_CLUSTERS;j++){
        
            for(int k=1;k<=N_ROBOTS;k++){
                Message m;
                //addRobot("A1","C"+to_string(j),"R"+to_string(k),getCurrentTime()-(BORN_TIME * 60000));   
                addRobot("A"+to_string(x),"C"+to_string(j),"R"+to_string(k),getCurrentTime(),m);   
            }
        }
    }
    
    cout << "Build time: " + std::to_string((double)(clock() - tStart)/CLOCKS_PER_SEC) + "\n";

}

void addSingleRobot(){
    static int i=0,j=0;
    Message m;
    addRobot("A1","C"+i,"R"+j,1516903200000,m);
    i++;
    i++;
    j++;
    sleep(1);
    cout << "added \n";
}

#endif