class Solution {
    int count = 0;

    public int findTargetSumWays(int[] nums, int target) {
        int length = nums.length;
        dfs(0, length, 0, target, nums);
        return count;
    }

    public void dfs(int cur_num, int length, int index, int target, int[] nums) {
        if (index > length - 1) {
            if (cur_num == target) {
                count += 1;
            }
            return;
        }

        dfs(cur_num + nums[index], length, index + 1, target, nums);
        dfs(cur_num - nums[index], length, index + 1, target, nums);
    }
}
