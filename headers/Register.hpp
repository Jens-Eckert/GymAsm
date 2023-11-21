#ifndef REGISTER_HPP
#define REGISTER_HPP

#include <functional>
#include <string>

const std::string RegNames[] = {"$0", "$zero", "$45", "$90", "$135",
                                "$180", "$bar1", "$bar2", "$bar3", "$bar4",
                                "$pr1", "$pr2", "$bnch", "$sqat", "$dlft",
                                "$curl", "$rep", "$rack"};

struct Register {
    Register(std::string);
    std::string name;
    int value;
};

#endif