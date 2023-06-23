/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    n=nums.length
    var val=fn(init,nums[0]);
    if (n==0){
        return init
    }
    for(let i=1;i<n;i++){
        val=fn(val,nums[i])
    }
    return val
};