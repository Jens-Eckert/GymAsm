#include "Environment.hpp"

Environment::Environment() {
    for (int i = 0; i < 18; i++) registers.emplace(std::pair{RegNames[i], Register(RegNames[i])});
}