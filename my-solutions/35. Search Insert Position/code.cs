public class Solution {
    public int SearchInsert(int[] nums, int target) {
        if (target > nums[nums.Length - 1])
        {
            return nums.Length;
        }
        else if (target < nums[0])
        {
            return 0;
        }

        for (int i = 0; i <= nums.Length - 1; i++)
        {
            if (nums[i] == target)
            {
                return i;
            }
            else if (nums[i] < target && nums[i+1] > target)
            {
                return i + 1;
            }
        }

        return 0;
    }
}
