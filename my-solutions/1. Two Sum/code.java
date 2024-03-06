class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        Map<Integer, Integer> map_1 = new HashMap<>();

        for (int i = 0; i < nums.length; i++) 
        {
            int current_num = nums[i];

            if (map_1.containsKey(target - current_num))
            {
                return new int[] {i, map_1.get(target - current_num)};
            }
            else
            {
                map_1.put(current_num, i);
            }
        }

        return null;
    }
}
