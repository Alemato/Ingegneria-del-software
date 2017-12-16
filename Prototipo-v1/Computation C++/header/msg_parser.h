#include <iostream>
#ifndef "message.h"
#include <vector>
#include <string>
#include <sstream>



class Parser{
    public:
        Message parse(string); 
};


 Message Parser::parse(string s){

    string values[10]={};
    int i=0;
    Message msg;

    istringstream message ("A1,C77,YX49,0,1,0,1,0,1,0");

    vector<string> strings;    

    while (getline(message, s, ',')) {
        cout << s << endl;
        values[i] = (string) s;
        i++;
    }

    msg.init(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9]);
  

    return msg;
}