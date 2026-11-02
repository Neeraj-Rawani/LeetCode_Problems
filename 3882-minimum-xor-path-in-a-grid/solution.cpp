class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        const int V = 1024;
        vector<vector<char>> dp(n, vector<char>(V, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int g = grid[i][j];
                vector<char> next(V, 0);
                if (i == 0 && j == 0) {
                    next[g] = 1;
                } else {
                    for (int x = 0; x < V; x++) {
                        if (dp[j][x] || (j > 0 && dp[j - 1][x])) {
                            next[x ^ g] = 1;
                        }
                    }
                }
                dp[j] = move(next);
            }
        }
        for (int x = 0; x < V; x++) {
            if (dp[n - 1][x]) return x;
        }
        return -1;
    }
};