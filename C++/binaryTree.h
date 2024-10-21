#ifndef BINARYTREE_H
#define BINARYTREE_H

#include "Node.h"

class Tree{
private:
    Node* root;

public:
    enum Rec {IN, PRE, POST};
    Tree();
    void insert(Node* node, int value);
    void insert(int value);
    void showPOST(Node* node, int spc);
    void showPRE(Node* node, int spc);
    void showIN(Node* node, int spc);
    void show(Rec rec);
};

#endif