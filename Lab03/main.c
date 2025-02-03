#include <stdio.h>
#include "factorial.h"

//Compile with gcc main.c factorial.c -o run
//Execute using ./run


int main(int argc, char** argv[]){
    int iterative = ItFactorial(8);
    int recursive = RecFactorial(8);
    printf("Iterative: %d\nRecursive: %d\n", iterative, recursive);
}