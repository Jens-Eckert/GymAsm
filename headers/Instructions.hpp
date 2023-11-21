#ifndef INSTRUCTIONS_HPP
#define INSTRUCTIONS_HPP

#include "Register.hpp"

const std::string InstructionNames[] = {"add", "addi", "sub", "subi",
                                        "mult", "multi", "div", "divi"};

typedef std::function<void(Register*, Register*, Register*)> RType;
typedef std::function<void(Register*, int)> IType;
// typedef JType, idk yet

void add(Register*, Register*, Register*);
void addi(Register*, int);
void sub(Register*, Register*, Register*);
void subi(Register*, int);
void mult(Register*, Register*, Register*);
void multi(Register*, int);
void divr(Register*, Register*, Register*);
void divi(Register*, int);

#endif