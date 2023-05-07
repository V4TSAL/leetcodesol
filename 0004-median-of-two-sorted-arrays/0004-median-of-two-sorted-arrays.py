class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans=[]
        i=0
        j=0
        l1=len(nums1)
        l2=len(nums2)
        x=l1+l2
        mid=x/2
        while i<l1 and j<l2:
            if nums1[i]<=nums2[j]:
                ans.append(nums1[i])
                i=i+1
            else:
                ans.append(nums2[j])
                j=j+1
        while i<l1:
            ans.append(nums1[i])
            i=i+1
        while j<l2:
            ans.append(nums2[j])
            j=j+1
        if (x)%2==0:
            return (ans[int(mid)]+ans[int(mid)-1])/2
        else:
            return ans[int(mid)]
        
        