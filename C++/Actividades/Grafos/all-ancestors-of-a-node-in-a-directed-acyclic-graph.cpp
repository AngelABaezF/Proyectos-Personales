// Ángel Alexander Báez Flores
class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            indegree[edge[1]]++;
        }
        queue<int> q;
        vector<set<int>> ancestors(n);
        for (int i = 0; i < n; ++i) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            for (int neighbor : graph[node]) {
                ancestors[neighbor].insert(node);
                ancestors[neighbor].insert(ancestors[node].begin(), ancestors[node].end());
                if (--indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        vector<vector<int>> result(n);
        for (int i = 0; i < n; ++i) {
            result[i] = vector<int>(ancestors[i].begin(), ancestors[i].end());
        }
        return result;
    }
};