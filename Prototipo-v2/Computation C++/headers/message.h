#ifndef MESSAGE_H_
#define MESSAGE_H_
#include <iostream>
#include <vector>
#include <string>
#include <sstream>


class Message{

public:
  
  std::string Id_Area;
  std::string Id_Cluster;
  std::string Name_Robot;
  std::string S1,S2,S3,S4,S5,S6,S7;
  std::string timeStamp;

public:
  Message ( std::string timeStamp,
            std::string Area,
            std::string Cluster,
            std::string Robot,
            std::string S_1, std::string S_2, std::string S_3,
            std::string S_4, std::string S_5, std::string S_6, std::string S_7)
              : timeStamp (timeStamp),
                Id_Area (Area),
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
  void init(std::string,std::string,std::string,std::string,std::string,std::string,std::string,std::string,std::string,std::string,std::string);
  void info();

};


  void Message::info(){

    std::cout << "TimeStamp: " << timeStamp << std::endl;
    std::cout << "Id_Area: " << Id_Area << std::endl;
    std::cout << "Id_Cluster: " << Id_Cluster << std::endl;
    std::cout << "Name_Robot: " << Name_Robot << std::endl;

    std::cout << "SEGNALI \n";
    
    std::cout << "S1: " << S1 << std::endl;
    std::cout << "S2: " << S2 << std::endl;
    std::cout << "S3: " << S3 << std::endl;
    std::cout << "S4: " << S4 << std::endl;
    std::cout << "S5: " << S5 << std::endl;
    std::cout << "S6: " << S6 << std::endl;
    std::cout << "S7: " << S7 << std::endl;

  }

#endif
