class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        int lt = 0, freq = 0;
        for (int x : nums) {
            if (x < target) lt++;
            else if (x == target) freq++;
        }

        vector<int> result;
        result.reserve(freq);
        for (int i = 0; i < freq; i++) {
            result.push_back(lt + i);
        }
        return result;
    }
};