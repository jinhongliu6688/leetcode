class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> result = new ArrayList<Integer>();
        
        for (int x : nums) {
            x = Math.abs(x);
            if (nums[x - 1] < 0) {
                result.add(x);
            } else {
                nums[x - 1] *= -1;
            }
        }

        return result;
    }
}
