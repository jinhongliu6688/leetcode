public class Solution 
{
    public int[] TwoSum(int[] nums, int target) 
    {
        Dictionary<int, int> map_1 = new Dictionary<int, int>();

        for(int i = 0; i < nums.Length; i++)
        {
            int current_num = nums[i];

            if (map_1.ContainsKey(target - current_num))
            {
                return new int[] {i, map_1[target - current_num]};
            } 
            else 
            {
                if (!map_1.ContainsKey(current_num))
                {
                    map_1.Add(current_num, i);
                }
            }
        }

        // If no solution is found, return null
        return null;
    }
}
