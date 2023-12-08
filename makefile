CPP = clang++
CPP_FLAGS = -std=c++17
DEBUG_FLAGS = -std=c++17 -g3 -O0
INCLUDE_OPT = -I ./headers/

main: ./src/main.cpp ./headers/environment.hpp ./headers/register.hpp ./headers/instructions.hpp
	${CPP} ${CPP_FLAGS} ${INCLUDE_OPT} ./src/main.cpp ./src/environment.cpp ./src/register.cpp ./src/instructions.cpp -o main.o
	./main.o test.gasm
	# rm main.o

debug: ./src/main.cpp ./headers/environment.hpp ./headers/register.hpp ./headers/instructions.hpp
	${CPP} ${DEBUG_FLAGS} ${INCLUDE_OPT} ./src/main.cpp ./src/environment.cpp ./src/register.cpp ./src/instructions.cpp -o main.o
	gdb -q main.o