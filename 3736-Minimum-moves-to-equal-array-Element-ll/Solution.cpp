class Solution {
public:
    int minMoves(vector<int>& nums) {
        int max = 0;
        for(int i = 0; i < nums.size(); ++i) {
            if(max < nums[i]) max = nums[i];
        }

        int steps = 0;
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] < max) steps += max - nums[i]; 
        }

        return steps;
    }
};