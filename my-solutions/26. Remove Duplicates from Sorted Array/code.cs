public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int insert_index = 1;

        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i] != nums[i-1])
            {
                nums[insert_index] = nums[i];
                insert_index += 1;
            }
        }

        return insert_index;
    }
}
