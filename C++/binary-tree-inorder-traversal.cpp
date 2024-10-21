// Ángel Alexander Báez Flores - A01425613
class Solution {
public:
    void inorder(TreeNode* node, vector<int>& output){
        if(node->left != nullptr) inorder(node->left, output);
        output.push_back(node->val);
        if(node->right != nullptr) inorder(node->right, output);
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> output;

        if(root != nullptr) inorder(root, output);

        for(int i=0; i<output.size(); i++){
            cout << output[i] << " ";
        }

        return output;
    }
};