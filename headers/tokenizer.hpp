#ifndef TOKENIZER_HPP
#define TOKENIZER_HPP

#include <initializer_list>
#include <iostream>
#include <regex>
#include <tuple>
#include <unordered_map>
#include <vector>

class Tokenizer {
public:
private:
    std::vector<std::tuple<std::regex, std::string>> patterns = {
        {std::regex("\s+"), "Whitespace"},
        {std::regex("\#.*"), "Comment"},
        {std::regex("[a-zA-Z]+\:"), "Label"},
        {std::regex("[a-zA-Z]+"), "Operator"},
        {std::regex("\,\s"), "Separator"},
        {std::regex("\.[a-z]+|\ \d+"), "Modifier"},
        {std::regex("\"([^\"]|\"\")*\""), "String"},
        {std::regex("\d+(\.\d*)?"), "Number"},
        {std::regex("\$[a-z0-9]{1,6}"), "Register"},
        {std::regex("."), "Error"}};
};

#endif