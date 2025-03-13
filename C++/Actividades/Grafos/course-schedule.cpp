 // Ángel Alexander Báez Flores - A01425613

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        vector<int> inDegree(numCourses, 0);
        for (auto& pre : prerequisites) {
            graph[pre[1]].push_back(pre[0]);
            inDegree[pre[0]]++;
        }
        stack<int> zeroInDegree;
        for (int i = 0; i < numCourses; ++i) {
            if (inDegree[i] == 0) {
                zeroInDegree.push(i);
            }
        }
        int count = 0;
        while (!zeroInDegree.empty()) {
            int course = zeroInDegree.top();
            zeroInDegree.pop();
            count++;
            for (int neighbor : graph[course]) {
                if (--inDegree[neighbor] == 0) {
                    zeroInDegree.push(neighbor);
                }
            }
        }
        return count == numCourses;
    }
};