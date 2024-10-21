//Angel Alezander Baez Flores - A01425613
class Solution {
public:
    void mezcla(vector<int>& nums1, int inicio, int fin) {
        int centro = (inicio + fin) / 2;
        int i = inicio;
        int j = centro + 1;
        vector<int> aux(fin - inicio + 1);
        int k = 0;
        while (i <= centro && j <= fin) {
            if (nums1[i] <= nums1[j]) {
                aux[k++] = nums1[i++];
            } else {
                aux[k++] = nums1[j++];
            }
        }
        while (i <= centro) {
            aux[k++] = nums1[i++];
        }
        while (j <= fin) {
            aux[k++] = nums1[j++];
        }
        for (int l = 0; l < aux.size(); l++) {
            nums1[inicio + l] = aux[l];
        }
    }

    void mergeSort(vector<int>& nums1, int inicio, int fin) {
        if (inicio < fin) {
            int centro = (inicio + fin) / 2;
            mergeSort(nums1, inicio, centro);
            mergeSort(nums1, centro + 1, fin);
            mezcla(nums1, inicio, fin);
        }
    }

    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for (int i = 0; i < n; i++) {
            nums1[m + i] = nums2[i];
        }
        mergeSort(nums1, 0, m + n - 1);
    }
};
