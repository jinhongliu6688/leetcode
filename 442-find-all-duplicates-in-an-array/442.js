/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    const result = [];
    for (let i = 0; i < nums.length; i++) {
        const cur_num = Math.abs(nums[i])
        if (nums[cur_num - 1] < 0) {
            result.push(cur_num)
        } else {
            nums[cur_num - 1] *= -1
        }
    }

    return result
};
