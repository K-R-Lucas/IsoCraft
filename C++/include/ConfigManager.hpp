#pragma once

#include <map>
#include <string>
#include <any>
#include <fstream>
#include <iostream>

class ConfigManager
{
private:
    std::map<std::string, std::any> volitialeData;

protected:
    void ReadData(std::string _path);

};