class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sett = []
        for i in nums1:
            sett.append(i)
        for j in nums2:
            sett.append(j)
        sset = sorted(sett)
        length = len(sett)
        if length % 2 != 0:
            div1 = length//2
            return sset[div1]
        else:
            div2 = length//2
            mid = (sset[div2] + sset[div2-1])/2
            return mid