class Solution {
/* 
	Es iterativa de complejidad O(n)
*/
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int izquierda = 0;
        int derecha = numbers.size() - 1;
        while (izquierda < derecha){
            int suma = numbers[izquierda] + numbers[derecha];
            if (suma == target){
                return {izquierda + 1, derecha + 1};
            } else if (suma<target){
                izquierda++;
            } else {
                derecha--;
            }
        }
        return {};
    }
};
