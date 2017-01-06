
## Related Work

[1] says that C++14release is already out and some or ost of the features are in the compilers clang  g++ and visual studio. So of the prominent features 
features are ***Return Type Deduction***, *** Generic Lambdas ***, ***Initialized Lambda Captures***.

[2] talks about latest changes in the c++17 specification changes and addition of new features introduced by the specification
Some feature are *** std::variant *** , *** if and swith statements with initialiser ***, *** if constexpr ***,  ***auto in templates ***, *** structured bindings ***,  
```c++
#include<stdio.h>
#include<iostream>
using namespace std;

auto function(){  \\ return type deduction
    if (auto a=1;a == 1){
       return 's';
    }
    auto adder = [](auto arg1, auto arg2){return arg1 + arg2 }
    if constexpr (){
     printf("compile time static if!");
    }
    variant<int, char> v;
    return 'a';
}
```
## References

1. _http://www.drdobbs.com/cpp/the-c14-standard-what-you-need-to-know/240169034_
2. _https://meetingcpp.com/index.php/br/items/final-features-of-c17.html_
