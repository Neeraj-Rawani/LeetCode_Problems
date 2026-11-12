class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int tang=1,giam=1,ketQua=1;
        for(int i=1;i<(int)nums.size();++i) {
            tang=nums[i]>nums[i-1]?tang+1:1;
            giam=nums[i]<nums[i-1]?giam+1:1;
            ketQua=max({ketQua,tang,giam});
        }
        return ketQua;
    }
};