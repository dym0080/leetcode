
/**
 * javascript方案1
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection1 = function(nums1, nums2) {
    var set1 = new Set(nums1);
    var set2 = new Set(nums2);
    var result = new Set([...set1].filter(x => set2.has(x)));
    return [...result]
};

/**
 * javascript方案2
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection2 = function(nums1, nums2) {
    var set1 = new Set(nums1);
    var set2 = new Set(nums2);
    var result = [];
    if(set1.size < set2.size){
        for(let item of set1){
            if(set2.has(item)){
                result.push(item);
            }
        }
        return result;
    }else{
        for(let item of set2){
            if(set1.has(item)){
                result.push(item);
            }
        }
        return result;
    }
};