class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l = 0

        if not nums:
            return 0

        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1

        if val not in nums:
            return len(nums)

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1

        return l


Sol = Solution()
res = Sol.removeElement([2], 3)
print(res)
