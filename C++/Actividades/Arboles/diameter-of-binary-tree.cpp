//Ángel Alexander Báez Flores
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    int maxDiametro; 
public:
    Solution() : maxDiametro(0) {}
    int diameterOfBinaryTree(TreeNode* root) {
        maxDiametro = 0;
        calcularDiametro(root);
        return maxDiametro;
    }
private:
    int calcularDiametro(TreeNode* nodo) {
        if (nodo == nullptr) return 0;
        int izquierdaAlt = calcularDiametro(nodo->left);
        int derechaAlt = calcularDiametro(nodo->right);
        int diametroActl = izquierdaAlt + derechaAlt;
        maxDiametro = max(maxDiametro, diametroActl);
        return max(izquierdaAlt, derechaAlt) + 1;
    }
};