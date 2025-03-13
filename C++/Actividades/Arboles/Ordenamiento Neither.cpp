// Angel Baez - A01425613
class Solution {
public:
    int findNonMinOrMax(vector<int>& nums) {
        if (nums.size() <= 2) {
            return -1;
        }
        //min y max
        int min_val = nums[0], max_val = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] < min_val) {
                min_val = nums[i];
            }
            if (nums[i] > max_val) {
                max_val = nums[i];
            }
        }
        //nmin y nmax
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != min_val && nums[i] != max_val) {
                return nums[i];
            }
        }
        return -1;
    }
};
