#include <iostream>
using namespace std;

struct Node{
    char data;
    Node* next;
};

Node* CreateNode(char data){
    Node* newNode = new Node();
    newNode -> data = data;
    newNode ->next = nullptr;
    return newNode;
}

void push(Node* head, char data){
    Node* newNode = CreateNode(data);

}