#include <iostream>
#include <vector>
using namespace std;

void show(vector<int>& nums){
    for (int k:nums) cout << k << " ";
    cout << endl;
}

void show(vector<int>& nums, int i, int j){
    for (int k=i; k<=j; k++) cout << nums[k] << " ";
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
            else break;
        show(nums);
    }
}

void bubbleSort(vector<int>& nums){
    for (int i=1; i<nums.size(); i++){
    	bool flag = false;  
        for (int j=0; j<nums.size()-i; j++)
            if (nums[j+1] < nums[j]) swap(nums[j+1], nums[j]){
            	swap();
            	
			}
        show(nums);
    }
}

void mezcla(vector<int>& nums, int inicio, int fin){
    int centro = (inicio+fin) / 2;
    int j = inicio; 
    int k = centro + 1;
    int size = fin-inicio+1; 

    vector<int>tmp(size);
    for (int i=0; i<size; i++){
        if (j<=centro && k<=fin){
            if (nums[j] < nums[k]) tmp[i] = nums[j++];
            else tmp[i] = nums[k++];
        }else if (j<=centro)
            tmp[i] = nums[j++];
        else
            tmp[i] = nums[k++];
    }
    for (int m=0; m<size; m++) nums[inicio+m] = tmp[m];
}

void mergeSort(vector<int>& nums, int inicio, int fin){
    if (inicio < fin){
        int centro = (inicio+fin)/2;
        mergeSort(nums, inicio, centro);
        mergeSort(nums, centro+1, fin);
        mezcla(nums, inicio,fin);
        show(nums, inicio, fin);
    }
}

int part(vector<int>& nums, int start, int end){
    int piv = nums[start];
    int i = start+1;
    for(int j=start+1; j <= end; j++) {
        if (nums[j] < piv){
            swap(nums[i], nums[j]);
            i++;
        }
    }
    swap(nums[start], nums[i-1]);
    return i-1;
}

void quickSort(vector<int>& nums, int inicio, int fin){
    if (inicio < fin){
        int posP = part(nums, inicio, fin);
        quickSort(nums,inicio,posP-1);
        quickSort(nums,posP+1, fin);
        showQuickSort(nums, inicio, fin);
    }
}

int main(){
    vector<int>nums = {10, 8, 6, 4, 3};
    cout << "Selection sort" << endl;
    selectionSort(nums);
    
    nums = {10, 8, 6, 4, 3};
    cout << "Insertion sort" << endl;
    insertionSort(nums);

    nums = {10, 8, 6, 4, 3};
    cout << "Bubble sort" << endl;
    bubbleSort(nums);

    nums = {10, 8, 6, 4, 3};
    cout << "Merge sort" << endl;
    mergeSort(nums, 0, nums.size()-1);

    nums = {10, 8, 6, 4, 3};
    cout << "Quick sort" << endl;
    quickSort(nums, 0, nums.size()-1);

    return 0;
}
