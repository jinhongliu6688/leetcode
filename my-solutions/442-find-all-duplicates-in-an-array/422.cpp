class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> result;
        for (int x : nums) {
            x = abs(x);
            if (nums[x - 1] < 0) {
                result.push_back(x);
            } else {
                nums[x - 1] *= -1;
            }
        }

        return result;
    }
};
