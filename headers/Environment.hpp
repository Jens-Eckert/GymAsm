#ifndef ENV_HPP
#define ENV_HPP

#include <functional>
#include <typeinfo>
#include <unordered_map>

#include "Instructions.hpp"
#include "Register.hpp"

class Environment {
public:
    Environment();

private:
    std::unordered_map<std::string, Register> registers;

    const std::unordered_map<std::string, RType> RTypeInstructions = {
        std::pair{"add", RType(add)},
        std::pair{"sub", RType(sub)},
        std::pair{"mult", RType(mult)},
        std::pair{"div", RType(divr)},
    };

    const std::unordered_map<std::string, IType> ITypeInstructions = {
        std::pair{"addi", IType(addi)},
        std::pair{"subi", IType(subi)},
        std::pair{"multi", IType(multi)},
        std::pair{"divi", IType(divi)},
    };
    // std::unordered_map<std::string, JType> JTypeInstructions;

    const std::unordered_map<int, std::string> program;
};

#endif