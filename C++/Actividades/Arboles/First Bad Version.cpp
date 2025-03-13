//Angel Alexander Báez Flores - A01425613
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int inicio = 1, fin = n;

        while (inicio < fin) {
            int medio = inicio + (fin - inicio) / 2;
            if (isBadVersion(medio)) {
                fin = medio;
            } else {
                inicio = medio + 1;
            }
        }
        return inicio;
    }
};
