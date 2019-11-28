public class Solution1 {
    public int[] Intersection(int[] nums1, int[] nums2) {
        var set1 = new HashSet<int>(nums1);
        set1.IntersectWith(new HashSet<int>(nums2));
        return set1.ToArray();
    }
}

public class Solution2 {
    public int[] Intersection(int[] nums1, int[] nums2) {
        var arr1 = DelRepeatData(nums1);
        var arr2 = DelRepeatData(nums2);
        var result = new List<int>();
        foreach(int item in arr1){
            if(Array.IndexOf(arr2,item) > -1){
                result.Add(item);
            }
        }
        return result.ToArray();
    }

    public int[] DelRepeatData(int[] arr)
    {
        return arr.GroupBy(p => p).Select(p => p.Key).ToArray();
    }
}