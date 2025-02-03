#include <stdio.h>
#include "factorial.h"

int ItFactorial(int num){
    int sum = num;
    for(int i = 1;i<num;i++){
        sum = sum * (num-i);
    }
    return sum;
}

int RecFactorial(int num){
    if(num == 1){
        return num;
    }
    else{
        num = num * RecFactorial(num-1);
    }
    return(num);

}

