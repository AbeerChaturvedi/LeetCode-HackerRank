class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lent = len(nums)
        li = []
        for i in range(lent):
            for j in range(lent):
                if i == j:
                    continue
                else:
                    if nums[i] + nums[j] == target:
                        li.append(i)
                        li.append(j)
                        return li