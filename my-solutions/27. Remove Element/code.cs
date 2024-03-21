public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int i = 0;
        int j = 0;

        int length = nums.Length;

        while (i < length && j < length)
        {
            while (i < length && nums[i] != val)
            {
                i += 1;
            }

            while (j < length && nums[j] == val)
            {
                j += 1;
            }

            if (i < j && i < length && j < length)
            {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
            else
            {
                j += 1;
            }
        }

        return i;
    }
}
