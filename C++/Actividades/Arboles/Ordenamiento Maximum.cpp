// Angel Baez - A01425613
class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        //selection sort
        int n = nums.size();
        for (int i = 0; i < n - 1; ++i) {
            int max_idx = i;
            for (int j = i + 1; j < n; ++j) {
                if (nums[j] > nums[max_idx]) {
                    max_idx = j;
                }
            }
            swap(nums[i], nums[max_idx]);
        }
        //dos mayores
        int max1 = nums[0];
        int max2 = nums[1];
        //dos menores
        int min1 = nums[n - 1];
        int min2 = nums[n - 2];
        return (max1 * max2) - (min1 * min2);
    }
};
