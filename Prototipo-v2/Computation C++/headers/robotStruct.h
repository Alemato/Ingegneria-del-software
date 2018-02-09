#ifndef ROBOTSTRUCT_H_
#define ROBOTSTRUCT_H_
#include <string>
#include <stdio.h>
#include <map>
#include <iostream>
#include <vector>
#include <string.h>

//map of robot

using namespace std;

typedef std::map<int,char> timeMap;
typedef std::map<std::string,timeMap> robotMap;
typedef std::map<int, robotMap> container ;

container cont;
bool created;


int call = 0;


void allocateTimelines(){


    clock_t tStart = clock();
    
    if(!created)
        for(int i=1;i<=9000;i++){
            

            robotMap r;

            r["s1"] = *(new timeMap());
            r["s2"] = *(new timeMap());
            r["s3"] = *(new timeMap());
            r["s4"] = *(new timeMap());
            r["s5"] = *(new timeMap());
            r["s6"] = *(new timeMap());
            r["s7"] = *(new timeMap());

            cont[i] = r;

            //cout << "Address container  for robot: " << i <<" | " << &(cont[i]) << "\n";
            //cout << "Address TimeMap s1 for robot: " << i <<" | "<< &((cont[i])["s1"]) << "\n";

        // ((cont[i])["s1"])[(int) 13546375463799] = '1';
        }

    //((cont[134])["s1"])[(int) 13546375463799] = '1'; 
    created=true;
    cout << "Tempo report: " + std::to_string((double)(clock() - tStart)/CLOCKS_PER_SEC) + "\n";
}

void postMessage(){
    
    clock_t tStart = clock();
    
    int timeStamp = (int) 13546375463799;
    
    int count=0;
    
    //insert 100 timestamps
    for(int j=1;j<=1;j++){
        
        //insert in each robot    
        for(int i=1;i<=1;i++){
                            
            ((cont[i])["s1"])[(int) timeStamp] = '1';
            ((cont[i])["s2"])[(int) timeStamp] = '1';
            ((cont[i])["s3"])[(int) timeStamp] = '1';
            ((cont[i])["s4"])[(int) timeStamp] = '1';
            ((cont[i])["s5"])[(int) timeStamp] = '1';
            ((cont[i])["s6"])[(int) timeStamp] = '1';
            ((cont[i])["s7"])[(int) timeStamp] = '1';
            
            count++;
                    
        }
        
        timeStamp++;
        
    }
    
    cout << "Tempo post 100 messages for each robot: " + std::to_string((double)(clock() - tStart)/CLOCKS_PER_SEC) + "\n";
    cout << "Count: " << count << "\n";
    cout << "Sent "<< to_string((int) (count/((double)(clock() - tStart)/CLOCKS_PER_SEC)))<<" Messsages per second."<<"\n";
    
    //((cont[45867])["s1"])[(int) 13546375463799] ='0';
    //cont.clear();
    if(cont.empty()) cout<<"empty";

    cout << call <<"\n";

    call++;
}

void readState(){
   
       
    int timeStamp = (int) 13546375463799;
    
    
        for(int i=1;i<=90000;i++){
            
            cout << ((cont[i])["s1"])[(int) timeStamp] << "\n";
            cout << ((cont[i])["s2"])[(int) timeStamp] << "\n";
            cout << ((cont[i])["s3"])[(int) timeStamp] << "\n";
            cout << ((cont[i])["s4"])[(int) timeStamp] << "\n";
            cout << ((cont[i])["s5"])[(int) timeStamp] << "\n";
            cout << ((cont[i])["s6"])[(int) timeStamp] << "\n";
            cout << ((cont[i])["s7"])[(int) timeStamp] << "\n";
            
        }
    

}


/*

FOR TEST PURPOSE

int main(void){

    allocateTimelines();
    postMessage();
    
    cout << "Query example: \n";
    cout << ((cont[45867])["s1"])[(int) 13546375463799] << "\n";
    
    
    //cout << "\n" << ((cont[134])["s1"])[(int) 13546375463799] << "\n";
    //cout << "\n" << ((cont[134])["s1"])[(int) 13546375463798] << "\n";
    //cout << "\n" << ((cont[45000])["s1"])[(int) 13546375463799] << "\n";
    
}

*/

#endif

