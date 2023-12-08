#include "environment.hpp"

Environment::Environment() {
    for (int i = 0; i < 18; i++) registers.emplace(std::pair{RegNames[i], Register(RegNames[i])});
}

void Environment::loadProgram(std::string fileName) {
    std::ifstream file;

    file.open(fileName);

    if (!file.is_open()) {
        std::cerr << "Error opening file " << fileName << std::endl;
        exit(EXIT_FAILURE);
    }

    
}