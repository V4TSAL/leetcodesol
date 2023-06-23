/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var fliteredArr=[];
    for(let i=0;i<arr.length;i++)
        {
            if(fn(arr[i],i)){
                fliteredArr.push(arr[i])
            }
        }
    return fliteredArr
};