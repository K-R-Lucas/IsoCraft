#include "ConfigManager.hpp"

void ConfigManager::ReadData(std::string _path)
{
    std::fstream fileRead (_path, std::fstream::in);

    fileRead.close();
}