#ifndef IRENGINE_H_
#define IRENGINE_H_


#include <string>
#include <stdio.h>
#include <map>
#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
#include "robotTree.h"
#include <math.h>
#include "./clusterJson.h"
#include "./parameters.h"

using namespace std;



 struct sector{
    long start;
    long end;
    char value;
  };


vector<char> upDown (vector<long>,int,sector*,sigMap,vector<long>,string,long);

int secDuration(sector*,int);


int getBotIr(sigMap currentBot,long istant){

    //all keys combined
    vector<long> allKeys;
    
    //contain all state change timestamps for each signal
    vector<long> v1;
    vector<long> v2;
    vector<long> v3;
    vector<long> v4;
    vector<long> v5;
    vector<long> v6;
    vector<long> v7;


    vector<char> s1;
    vector<char> s2;
    vector<char> s3;
    vector<char> s4;
    vector<char> s5;
    vector<char> s6;
    vector<char> s7;

    int downTime = 0;
    int upTime = 0;
    
    //adding range keys to v1 from signal s1
    for(map<long,char>::iterator it = (currentBot["s1"]).begin(); it != (currentBot["s1"]).end(); ++it) {
                //find all keys < istant 
                if((it->first) <= istant && (it->first) >= istant - 3600000 ){ 
                    //add key to tail position in vector
                    v1.push_back(it->first);
                    allKeys.push_back(it->first);
                }
    }
    
    //adding range keys to v2 from signal s2
    for(map<long,char>::iterator it = (currentBot["s2"]).begin(); it != (currentBot["s2"]).end(); ++it) {
                
                //find all keys < istant 
                if((it->first) <= istant && (it->first) >= istant - 3600000 ){ 
                    //add key to tail position in vector
                    v2.push_back(it->first);
                    allKeys.push_back(it->first);

                }
    }
    
    //adding range keys to v3 from signal s3
    for(map<long,char>::iterator it = (currentBot["s3"]).begin(); it != (currentBot["s3"]).end(); ++it) {
                
                //find all keys < istant 
                if((it->first) <= istant && (it->first) >= istant - 3600000 ){ 
                    //add key to tail position in vector
                    v3.push_back(it->first);
                    allKeys.push_back(it->first);

                }
    }

       //adding range keys to v4 from signal s4
    for(map<long,char>::iterator it = (currentBot["s4"]).begin(); it != (currentBot["s4"]).end(); ++it) {
                
                //find all keys < istant 
                if((it->first) <= istant && (it->first) >= istant - 3600000 ){ 
                    
                    //add key to tail position in vector
                    v4.push_back(it->first);
                    allKeys.push_back(it->first);

                }
    }

        //adding range keys to v5 from signal s5
    for(map<long,char>::iterator it = (currentBot["s5"]).begin(); it != (currentBot["s5"]).end(); ++it) {
                
                //find all keys < istant 
                if((it->first) <= istant && (it->first) >= istant - 3600000 ){ 
                    
                    //add key to tail position in vector
                   
                    v5.push_back(it->first);
                    allKeys.push_back(it->first);

                }
    }

        //adding range keys to v6 from signal s6
    for(map<long,char>::iterator it = (currentBot["s6"]).begin(); it != (currentBot["s6"]).end(); ++it) {
                
                //find all keys < istant 
                if((it->first) <= istant && (it->first) >= istant - 3600000 ){ 
                    
                    //add key to tail position in vector
                   
                    v6.push_back(it->first);
                    allKeys.push_back(it->first);

                }
    }

        //adding range keys to v6 from signal s6
    for(map<long,char>::iterator it = (currentBot["s7"]).begin(); it != (currentBot["s7"]).end(); ++it) {
                
                //find all keys < istant 
                if((it->first) <= istant && (it->first) >= istant - 3600000 ){ 
                    
                    //add key to tail position in vector
                   
                    v7.push_back(it->first);
                    allKeys.push_back(it->first);

                }
    }
    
    //adding instant to keys
    allKeys.push_back(istant);
    
    std::sort(v1.begin(), v1.end());
    std::sort(v2.begin(), v2.end());
    std::sort(v3.begin(), v3.end());
    std::sort(v4.begin(), v4.end());
    std::sort(v5.begin(), v5.end());
    std::sort(v6.begin(), v6.end());
    std::sort(v7.begin(), v7.end());

    std::sort(allKeys.begin(), allKeys.end());


    /* will split timeline in sectors */

    //remove duplicates
    
    allKeys.erase( unique( allKeys.begin(), allKeys.end() ), allKeys.end() );  
    

    //divide timeline in sectors using timestamps ranges

    sector sec[allKeys.size()];
    

    //cout << "Sectors are: \n";
    for(int i=0;i<allKeys.size()-1;i++){
        if(allKeys[i]!= allKeys[i+1]){

         sec[i].start = allKeys[i]; 
         sec[i].end = allKeys[i+1];

        } 
        else{

         sec[i].start = allKeys[i]; 
         sec[i].end = allKeys[i+2];

        }
    }

    if(DEBUG){
                for(int i=0;i<allKeys.size()-1;i++){
                    cout<<"Sectors are: \n";
                    cout<< sec[i].start<<"-"<<sec[i].end<<"\n";
                }
        cout<<"Chiamata |upDown| \n";
    }

    
    
    
    s1 = upDown(allKeys,allKeys.size(),sec,currentBot,v1,"s1",istant);

    s2 = upDown(allKeys,allKeys.size(),sec,currentBot,v2,"s2",istant);
   
    s3 = upDown(allKeys,allKeys.size(),sec,currentBot,v3,"s3",istant);

    s4 = upDown(allKeys,allKeys.size(),sec,currentBot,v4,"s4",istant);
   
    s5 = upDown(allKeys,allKeys.size(),sec,currentBot,v5,"s5",istant);

    s6 = upDown(allKeys,allKeys.size(),sec,currentBot,v6,"s6",istant);

    s7 = upDown(allKeys,allKeys.size(),sec,currentBot,v7,"s7",istant);
    
    /* checking down sector and adding duration to downTime */

    for(int i=0;i < allKeys.size()-1;i++){
        
        if(allKeys.size() > 1){
            
            /* Finds a sector where all signal are down */
            
            if((s1[i]=='0')|(s2[i]=='0')|(s3[i]=='0')|(s4[i]=='0')|(s5[i]=='0')|(s6[i]=='0')|(s7[i]=='0'))
                {
                    downTime += secDuration(sec,i);
                    upTime = 60 - downTime;
                }

            else {
                    upTime += secDuration(sec,i);
                    
                    /*There's only one sector e.g. Robot has just started or 
                    has not changed status for at least 1 hour(may change) */
                    
                    if(allKeys.size() == 2) downTime = 60 - upTime;
                
                }
        }
    
        if(DEBUG){
                    cout<<"sec"<<to_string(i)<<": ";                
                    cout<<"Uptime: "<< to_string(upTime)<<" ";
                    cout<<"DownTime: "<< to_string(downTime)<<"\n";
        }

    }
    
    int iR = (int)round(((float) downTime / (float) TIME_WINDOW)*100);
    
    if(DEBUG){
                cout <<"DownTime Totale: "<<downTime<<"\n";
                cout <<"UpTime Totale: "<< upTime<<"\n";
                cout<<"Robot IR: "<< iR <<" \% \n";
                cout<<"ALL DONE ! \n";
    }

    return iR;
}

/* returns duration of a sector */

int secDuration(sector* s,int i){

    return ((s[i].end - s[i].start)/60000);

}


//find for each sector up/down value of signals
vector<char> upDown (             
                vector<long> allKeys,
                int secNumber,             
                sector* sec,
                sigMap currentBot,
                vector<long> v,
                string sig,
                long istant
            )
{
        /*if prima chiave minore dell'inizio del primo settore 
        &&  seconda chiave <= fine primo settore
        allora valore up/down settore = val s1[prima chiave]
    */
        int currentKey=0;

        vector<char> result;


        //printRobotObj(currentBot);

        sigLineMap sMap = currentBot[sig];

        for(int i=0;i<=allKeys.size()-1;i++){
        
        long validKey = v[currentKey];
        long inizioSettore = sec[i].start;
        long fineSettore = sec[i].end;
        char s='\0';
    
        
        //check horse-key
        if(i==0 && v[i] > istant-3600000){

            if((sMap[v[0]]) == '1') s = '0';
                else s = '1';
        }
               
        else if(v[currentKey] == sec[i].start){
            
            s = sMap[v[currentKey]];
           
        } 

        else if(v[currentKey+1] == sec[i].end){ 
            
            s = sMap[v[currentKey]];
            currentKey++;
            
        }

        else if(v[currentKey+1] > sec[i].end){
           
            s = sMap[v[currentKey]];
            
        }
     
        else{
           
            s = sMap[v[currentKey]];
            
        }
    
        sec[i].value = s;

    }
    
    for (int i=0;i<secNumber-1;i++) {
        
        if(DEBUG){
            cout<<"settore "<<i<<": "<<(sec[i].value)<<"\n";
            cout<<"settore "<<i<<" start: "<<sec[i].start<<" end: "<<sec[i].end<<"\n";
            cout<<"durata settore: "<<secDuration(sec,i)<<"\n";
            cout<<"valore settore:"<<sec[i].value<<"\n";
        }

        result.push_back(sec[i].value);
    }

    return result;

}

#endif