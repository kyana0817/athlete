class Solution(object):
    def mergeSortedArray(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
        if m == 0:
            nums1[:] = nums2
            return
        if n == 0:
            return
        
        j = 0
        for i in range(len(nums1)):
            if len(nums1) <= i or len(nums2) <= j:
                break
            if nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1

        if len(nums2) > j:
            l = len(nums2) - j
            nums1[-l:] = nums2[j:]


if __name__ == "__main__":
    solution = Solution()
    l=[1,2,3,0,0,0]
    solution.mergeSortedArray(l, 3, [2,5,6], 3)
    assert l == [1,2,2,3,5,6]
    l=[1]
    solution.mergeSortedArray(l, 1, [], 0)
    assert l == [1]
    l=[0]
    solution.mergeSortedArray(l, 0, [1], 1)
    assert l == [1]
    l=[2,0]
    solution.mergeSortedArray(l, 1, [1], 1)
    assert l == [1,2]
    l=[1,2,3,0,0,0]
    solution.mergeSortedArray(l, 3, [4,5,6], 3)
    assert l == [1,2,3,4,5,6]
    l=[4,5,6,0,0,0]
    solution.mergeSortedArray(l, 3, [1,2,3], 3)
    assert l == [1,2,3,4,5,6]
    l=[1,2,4,5,6,0]
    solution.mergeSortedArray(l, 5, [3], 1)
    assert l == [1,2,3,4,5,6]
    l=[0,0,3,0,0,0,0,0,0]
    solution.mergeSortedArray(l, 3, [-1,1,1,1,2,3], 6)
    assert l == [-1,0,0,1,1,1,2,3,3]

    print('All tests passed!')


