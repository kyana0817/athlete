class Solution(object):
    def containerWithMostWater(self, height: list[int]) -> int:
        li, ri = 0, len(height) - 1
        mw = 0
        
        while li < ri:
            mw = max(mw, (ri - li) * min(height[li], height[ri]))
            if height[li] > height[ri]:
                ri -= 1
            else:
                li += 1

        return mw




if __name__ == "__main__":
    solution = Solution()
    assert solution.containerWithMostWater([1,8,6,2,5,4,8,3,7]) == 49
    assert solution.containerWithMostWater([1,1]) == 1

    print('All tests passed!')
