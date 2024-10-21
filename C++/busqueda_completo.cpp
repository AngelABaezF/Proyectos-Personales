#include <iostream>
#include <vector>
using namespace std;

int busSequencial(vector<int>& nums, int n){
    for (int k=0; k<nums.size(); k++)
        if (nums[k]==n) return k;
    return -1; 
}

int busBinariaIter(vector<int>& nums, int n){
    int i = 0;
    int j = nums.size()-1;
    while (i<=j){
        int inter = (i+j)/2;
        if (nums[inter]==n) return inter;
        else if (nums[inter]>n) j = inter-1;
        else i = inter+1;
    }
    return -1;
}

int busBinariaRec(vector<int>& nums, int n, int i, int j){
    int inter = (i+j)/2;
    if (nums[inter]==n) return inter;
    if (i>j) return -1;
    if (nums[inter]>n) return busBinariaRec(nums, n, i, inter-1);
    else return busBinariaRec(nums, n, inter+1, j);    
}

class MyHash {
private:
    vector<pair<int,int>> table;
    int hash(int n){
        int i = n % table.size();
        return i;
    }
    bool esPrimo(int n){
        if (n==2) return true;
        if (n%2==0) return false;
        int lim = sqrt(n);
        for (int k=3; k<=lim; k++)
            if (n%k==0) return false;
        return true;
    }
public:
    MyHash(vector<int>& nums){
        int prime = (nums.size()*2) + 1;        
        while (!esPrimo(prime)) prime = prime + 1;
        //cout << "Primo: " << prime << endl;
        table.resize(prime, {-1,-1});
        for (int k=0; k<nums.size(); k++){
            int index = hash(nums[k]);
            while (table[index].first != -1) index = (index + 1) % table.size();
            table[index] = {nums[k], k};
        }
    }

    void showTable(){
        for (int k=0; k<table.size(); k++)
            cout << "{" << table[k].first << "," << table[k].second << "} ";
        cout << endl;
    }

    int find(int n){
        int index = hash(n);
        while (table[index].first != -1){
            if (table[index].first == n) return table[index].second;
            index = (index+1) % table.size();
        }
        return -1;
    }
};


int main(){
    vector<int>nums = {4,5,7,8,9,15,30,21};
    int n;
    cout << "Número a buscar: "; cin >> n;

    int resultado = busSequencial(nums, n);
    cout << "Búsqueda secuencial: " << resultado << endl;

    resultado = busBinariaIter(nums, n);
    cout << "Búsqueda binaria iterativa: " << resultado << endl;

    resultado = busBinariaRec(nums, n, 0, nums.size()-1);
    cout << "Búsqueda binaria recursiva: " << resultado << endl;

    MyHash hash(nums);
    hash.showTable();
    resultado = hash.find(n);
    cout << "Búsqueda tabla hash: " << resultado << endl;

    return 0;
}