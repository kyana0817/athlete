class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in num_dict:
                return [num_dict[comp], i]
            num_dict[nums[i]] = i
        return []

if __name__ == "__main__":
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    print('All tests passed!')
