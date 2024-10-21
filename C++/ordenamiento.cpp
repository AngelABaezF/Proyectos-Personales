#include <iostream>
#include <vector>
using namespace std;

void show(vector<int>& nums){
    for (int k:nums) cout << k << " ";
    cout << endl;
}

void selectionSort(vector<int>& nums){
    for (int i=0; i<nums.size()-1; i++){
        int menor = i;
        for (int j=i+1; j<nums.size(); j++)
            if (nums[j] < nums[menor]) menor = j;
        swap(nums[i], nums[menor]);
        show(nums);
    }
}

void insertionSort(vector<int>& nums){
    for (int i=1; i<nums.size(); i++){        
        for (int j = i-1; j>=0; j--)
            if (nums[j+1] < nums[j]) swap(nums[j], nums[j+1]);
        show(nums);
    }
}

int main(){
    vector<int>nums = {10, 8, 6, 4, 3};
    cout << "Selection sort" << endl;
    selectionSort(nums);
    nums = {10, 8, 6, 4, 3};
    cout << "Insertion sort" << endl;
    insertionSort(nums);

    return 0;
}