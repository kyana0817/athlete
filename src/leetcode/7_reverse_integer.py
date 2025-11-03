class Solution(object):
    def reverseInteger(self, x: int) -> int:
        r = 0
        f = 1
        if x < 0:
            x = -x
            f = -1
        for idx, c in enumerate(str(x)):
            r += int(c) * (10 ** idx)
        r *= f

        if r <= -2147483648 or r >= 2147483647: return 0
        return r




if __name__ == "__main__":
    solution = Solution()
    assert solution.reverseInteger(123) == 321
    assert solution.reverseInteger(-123) == -321
    assert solution.reverseInteger(120) == 21
    print('All tests passed!')
