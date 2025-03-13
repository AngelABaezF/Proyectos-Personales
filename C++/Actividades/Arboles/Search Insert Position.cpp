//Angel Alexander Báez Flores - A01425613
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int izquierda = 0;
        int derecha = nums.size() - 1;
        
        while (izquierda <= derecha) {
            int medio = izquierda + (derecha - izquierda) / 2;
            
            if (nums[medio] == target) {
                return medio;
            }
            else if (nums[medio] < target) {
                izquierda = medio + 1;
            }
            else {
                derecha = medio - 1;
            }
        }
        
        return izquierda;
    }
};
