CPP = clang++
CPP_FLAGS = -std=c++17
INCLUDE_OPT = -I ./headers/

main: ./src/main.cpp ./headers/Environment.hpp ./headers/Register.hpp ./headers/Instructions.hpp
	${CPP} ${CPP_FLAGS} ${INCLUDE_OPT} ./src/main.cpp ./src/Environment.cpp ./src/Register.cpp ./src/Instructions.cpp -o main

clean:
	rm *.out
	rm *.o
	rm main