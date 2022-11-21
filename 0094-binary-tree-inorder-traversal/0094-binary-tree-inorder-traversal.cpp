class Solution {
public:
vector<int> inorderTraversal(TreeNode* root) {
    vector<int>ans;
    while(root){
        if(!root->left){
            ans.push_back(root->val);
            root=root->right;
        }
        else{
            TreeNode* r=root->left;
            while(r->right && r->right!=root){
                r=r->right;
            }
            if(!r->right){
                r->right=root;
                root=root->left;
            }
            else{
                r->right=NULL;
                ans.push_back(root->val);
                root=root->right;
            }
        }
    }
    return ans;
}
};