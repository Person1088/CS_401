#include <iostream>
#include <cstring>
using namespace std;
//increments "top", and sets the element at the "top" index of a char[] to "element"
void push(char element, char* stack, int &top){
    if((top+1)<sizeof(stack)){
        top++;
        *(stack + top) = element;
    }
    else{
        cout<<"stack is full"<<endl;
    }
} 
//sets element at the "top" index of a char[] to 0, then decrements "top"
void pop(char* stack, int &top){
    if(top>=0){
        *(stack + top) = 0;
        top--;
    }
    else{
        cout<<"stack is empty"<<endl;
    }
}
//tests if a string has balanced sets of braces, brackets, or parentheses
//"(){[]}" would return 1, "(){[]" would return 0
bool IsBalanced(string input){
    int top = -1;
    int inputLength = input.length();
    char *stack = new char[inputLength];
    memset(stack, 0 , inputLength);
    for(int i = 0; i < inputLength; i++){
        if(input[i] == '(' || input[i] == '{' || input[i] == '['){
            push(input[i], stack, top);
        }
        if(input[i] == ')' || input[i] == '}' || input[i] == ']'){
            if(top == -1){
                cout<<"aborted at 36"<<endl;
                return false;
            }
            else{
                if((*(stack+top) == '(' && input[i] == ')') ||
                (*(stack+top) == '{' && input[i] == '}') ||
                (*(stack+top) == '[' && input[i] == ']')){
                    pop(stack, top);
                }
                else{
                    cout<<"aborted at 46"<<endl;
                    return false;
                }
            }
        }
    }
    return true;

}

int main(){
    cout<<IsBalanced("i[s this] good")<<endl;
   
}



