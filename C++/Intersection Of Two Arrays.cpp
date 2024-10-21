//Angel Alexander Baez Flores - A01425613
class Solution {
public:
    void insertionSort(vector<int>& nums) {
	    for (int i = 1; i < nums.size(); i++) {      
	        for (int j = i - 1; j >= 0; j--) {
	            if (nums[j + 1] < nums[j]) {
	                swap(nums[j], nums[j + 1]);
	            } else {
	                break;
	            }
	        }
	    }
	}
	
	vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
	    insertionSort(nums1);
	    insertionSort(nums2);
	    vector<int> resultado;
	    int i = 0, j = 0;
	    while (i < nums1.size() && j < nums2.size()) {
	        if (nums1[i] == nums2[j]) {
	            if (resultado.empty() || resultado.back() != nums1[i]) {
	                resultado.push_back(nums1[i]);
	            }
	            i++;
	            j++;
	        } else if (nums1[i] < nums2[j]) {
	            i++;
	        } else {
	            j++;
	        }
	    }
	    return resultado;
	}
};
