#ifndef CLUSTERJSON_H_
#define CLUSTERJSON_H_

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>

struct clustJson{
    std::string area_name;
    std::string cluster_name;
    std::string cluster_inef;
    std::map<std::string,int> robotIr;
};


#endif
