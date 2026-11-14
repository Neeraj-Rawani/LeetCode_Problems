class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int n = nums.size(), best = INT_MAX;
        for (int i = 0; i < n; ++i) {
            int s = 0;
            for (int j = i; j < min(i + r, n); ++j) {  // nums[i..j] at most r long
                s += nums[j];
                if (j - i + 1 >= l && 0 < s && s < best)
                    best = s;
            }
        }
        return best == INT_MAX ? -1 : best;
    }
};