class Solution {
    public List<List<Integer>> findSubsequences(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        
        Deque<Integer> path = new ArrayDeque<>();
        
        int length = nums.length;
        
        dfs(0, path, result, length, nums);
        
        return result;
    }

    public void dfs(int begin, Deque<Integer> path, List<List<Integer>> result, int length, int[] nums) {
        if (path.size() >= 2) {
            result.add(new ArrayList<> (path));
        }

        if (begin == length) {
            return;
        }

        HashMap<Integer, String> seen = new HashMap<Integer, String>();

        for (int i = begin; i < length; i++) {
            if (seen.get(nums[i]) == "1") {
                continue;
            }

            if (path.size() > 0 && path.peekLast() > nums[i]) {
                continue;
            }
            
            seen.put(nums[i], "1");
            
            path.addLast(nums[i]);

            dfs(i+1, path, result, length, nums);

            path.removeLast();
        }
    }
}
