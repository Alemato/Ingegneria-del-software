#ifndef MESSAGE_H_
#define MESSAGE_H_
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

class Message{

public:
  
  string Id_Area;
  string Id_Cluster;
  string Name_Robot;
  string S1,S2,S3,S4,S5,S6,S7;

public:
  Message ( string Area,
            string Cluster,
            string Robot,
            string S_1, string S_2, string S_3,string S_4, string S_5, string S_6, string S_7)
              : Id_Area (Area),
                Id_Cluster (Cluster),
                Name_Robot (Robot),
                S1 (S_1),
                S2 (S_2),
                S3 (S_3),
                S4 (S_4),
                S5 (S_5),
                S6 (S_6),
                S7 (S_7)
              {}
  Message () {}
  void init(string,string,string,string,string,string,string,string,string,string);
  void info();

};


  void Message::info(){

    cout << "Id_Area: " << Id_Area << endl;
    cout << "Id_Cluster: " << Id_Cluster << endl;
    cout << "Name_Robot: " << Name_Robot << endl;

    cout << "SEGNALI \n";
    
    cout << "S1: " << S1 << endl;
    cout << "S2: " << S2 << endl;
    cout << "S3: " << S3 << endl;
    cout << "S4: " << S4 << endl;
    cout << "S5: " << S5 << endl;
    cout << "S6: " << S6 << endl;
    cout << "S7: " << S7 << endl;

  }

#endif
