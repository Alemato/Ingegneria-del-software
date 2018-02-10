#ifndef UPDATE_H_
#define UPDATE_H_

#define TIME_WINDOW 60 // Time in minutes | Calc IR based on (downtime/time-window)*100
//#define DEBUG 0 // Enable debug messages

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


void systemUpdate(){


    //for each area
    for(map<string,clusters>::iterator it = general.begin(); it != general.end(); ++it) {
            std::cout << it->first << "\n";
            std::string area = it->first;
    
        //for each cluster in area
        for(map<string,robots>::iterator it = (general[area]).begin(); it != general[area].end(); ++it) {
                std::cout << it->first << "\n";
                std::string cluster = it->first;
        
            for(map<string,sigMap>::iterator it = ((general[area])[cluster]).begin(); it != ((general[area])[cluster]).end(); ++it) {
                    std::cout << it->first;
                    std::cout<<"mammete \n"; 
            }
        }
    }

}

void addJson(){



}


void createJson(){


}

#endif