#include <iostream>
#include "binaryTree.h"

using namespace std;

int main(){
    Tree tree;

    tree.insert(500);
    tree.insert(350);
    tree.insert(700);
    tree.insert(800);
    tree.insert(100);
    tree.insert(50);
    tree.insert(150);
    tree.insert(600);
    cout << "IN\n";
    tree.show(Tree::IN);
    cout << "PRE\n";
    tree.show(Tree::PRE);
    cout << "POST\n";
    tree.show(Tree::POST);
    return 0;
}