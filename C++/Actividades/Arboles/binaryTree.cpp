#include <iostream>
#include "binaryTree.h"

Tree::Tree(){
    root = nullptr;
}

void Tree::insert(Node* node, int value){
    if(node->value > value){
        if(node->right == nullptr)
            node->right = new Node(value);
        else        
            insert(node->right, value);
    }else if(node->value < value){
        if(node->left == nullptr)
            node->left = new Node(value);
        else
            insert(node->left, value);
    }
}

void Tree::insert(int value){
    if(root == nullptr){
        root = new Node(value);
        return;
    }

    insert(root, value);
}

void Tree::showIN(Node* node, int spc){
    if(node->right != nullptr) showIN(node->right, spc+4);
    std::cout << std::string(spc, ' ') << node->value << std::endl;
    if(node->left != nullptr) showIN(node->left, spc+4);
}

void Tree::showPRE(Node* node, int spc){
    std::cout << std::string(spc, ' ') << node->value << std::endl;
    if(node->right != nullptr) showPRE(node->right, spc+4);
    if(node->left != nullptr) showPRE(node->left, spc+4);
}

void Tree::showPOST(Node* node, int spc){
    if(node->right != nullptr) showPOST(node->right, spc+4);
    if(node->left != nullptr) showPOST(node->left, spc+4);
    std::cout << std::string(spc, ' ') << node->value << std::endl;
}

void Tree::show(Rec rec){
    if(rec == IN) showIN(root, 0);
    if(rec == PRE) showPRE(root, 0);
    if(rec == POST) showPOST(root, 0);
}