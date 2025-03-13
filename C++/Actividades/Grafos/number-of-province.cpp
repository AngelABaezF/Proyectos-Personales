 // Ángel Alexander Báez Flores - A01425613

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<int> visited(n, 0);
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(isConnected, visited, i, n);
                count++;
            }
        }
        return count;
    }
    void dfs(vector<vector<int>>& isConnected, vector<int>& visited, int u, int nodes) {
        visited[u] = 1;
        for (int v = 0; v < nodes; v++) {
            if (u != v && isConnected[u][v] == 1 && !visited[v]) {
                dfs(isConnected, visited, v, nodes);
            }
        }
    }
};