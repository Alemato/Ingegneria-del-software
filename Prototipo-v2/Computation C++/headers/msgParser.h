#ifndef MSGPARSER_H_
#define MSGPARSER_H_

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include "message.h"



class Parser{
    public:
        Message* parse(string); 
  };


    Message* Parser::parse(string s){

    string values[10]={};
    int i=0;

    istringstream message (s);

    vector<string> strings;    

    while (getline(message, s, ',')) {
        //cout << s << endl;
        values[i] = (string) s;
        i++;
    }

    Message* msg = new Message(
                                (string) values[0],
                                (string) values[1],
                                (string) values[2],
                                (string) values[3],
                                (string) values[4],
                                (string) values[5],
                                (string) values[6],
                                (string) values[7],
                                (string) values[8],
                                (string) values[9]
                              );

    return msg;
}
#endif
