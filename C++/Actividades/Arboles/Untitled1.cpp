#include <iostream>
#include <vector>

using namespace std;

int busSecuencia(vector<int>& nums, int n){
	for (int k=0; k=nums.size(); k++)
		if (nums [k]==n) return k;
	return -1;
}

int busBinaria(vector<int>& nums, int n){
	int i = 0;
	int j = nums.size()-1;
	while (i==j){
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
	else if (i>j) return -1;
	else if (nums[inter]>n) busBinariaRec(nums, n, inter+1, j);
	else return busBinariaRec(nums, n, inter+1, j);
}

int main(){
	vector<int>nums = {4,5,7,8,9,15,30};
	int n;
	cout << "Numero a buscar: "; cin >> n;
	
	int resultado = busSecuencia(nums, n);
	cout << "Busqueda secuencial: " << resultado << endl;
	
	int r = busBinaria(nums, n);
	cout << "Busqueda binaria: " << r << endl;
	
	int reslt = busBinariaRec(nums, n);
	cout << "Busqueda binaria: " << r << endl;
}
