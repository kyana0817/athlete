class Solution(object):
    def stringToIntegerAtoi(self, s: str) -> int:
        re = ""
        for c in s:
            if c.isdigit():
                re += c
            else:
                if len(re) == 0:
                    if c == ' ':
                        continue
                    if c in {'+', '-'}:
                        re = c
                        continue
                break
        if len(re) == 0: return 0
        if re[0] in {'+', '-'} and len(re) == 1: return 0
        if re[0] == '+':
            return min(max(-2147483648, int(re[1:])), 2147483647)
        return min(max(-2147483648, int(re)), 2147483647)




if __name__ == "__main__":
    solution = Solution()
    assert solution.stringToIntegerAtoi("42") == 42
    assert solution.stringToIntegerAtoi(" -042") == -42
    assert solution.stringToIntegerAtoi("1337c0d3") == 1337
    assert solution.stringToIntegerAtoi("0-1") == 0
    assert solution.stringToIntegerAtoi("words and 987") == 0
    assert solution.stringToIntegerAtoi(".1") == 0
    assert solution.stringToIntegerAtoi("+-12") == 0
    assert solution.stringToIntegerAtoi("-+12") == 0
    print('All tests passed!')

