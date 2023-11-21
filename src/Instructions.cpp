#include "Instructions.hpp"

void add(Register* r1, Register* r2, Register* r3) {
    r1->value = r2->value + r3->value;
}

void addi(Register* r1, int i) {
    r1->value += i;
}

void sub(Register* r1, Register* r2, Register* r3) {
    r1->value = r2->value - r3->value;
}

void subi(Register* r1, int i) {
    r1->value -= i;
}

void mult(Register* r1, Register* r2, Register* r3) {
    r1->value = r2->value * r3->value;
}

void multi(Register* r1, int i) {
    r1->value *= i;
}

void divr(Register* r1, Register* r2, Register* r3) {
    r1->value = r2->value / r3->value;
}

void divi(Register* r1, int i) {
    r1->value /= i;
}