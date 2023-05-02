class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l,r,A):
            i=0
            j=0
            k=0
            l_l=len(l)
            l_r=len(r)
            while i<l_l and j<l_r:
                if l[i]<=r[j]:
                    A[k]=l[i]
                    i=i+1
                else:
                    A[k]=r[j]
                    j=j+1
                k=k+1
            while i<l_l:
                A[k]=l[i]
                i=i+1
                k=k+1
            while j<l_r:
                A[k]=r[j]
                k=k+1
                j=j+1
            return A
        def mergeSort(A):
            gg=len(A)
            if gg<2:
                return 
            mid=int(gg/2)
            l=A[:mid]
            r=A[mid:]
            mergeSort(l)
            mergeSort(r)
            merge(l,r,A)
        mergeSort(nums)
        return nums
                        
        