class Solution(object):
    def integerToRoman(self, num: int) -> str:
        ROMAN_TUPLES = [
            ('M', 1000),
            ('D', 500),
            ('C', 100),
            ('L', 50),
            ('X', 10),
            ('V', 5),
            ('I', 1)
        ]

        res = ''
        t = num
        for (c, v) in ROMAN_TUPLES:
            tc = t // v
            res += c * tc
            t -= tc * v

        res = res.replace('DCCCC', 'CM')
        res = res.replace('CCCC', 'CD')
        res = res.replace('LXXXX', 'XC')
        res = res.replace('XXXX', 'XL')
        res = res.replace('VIIII', 'IX')
        res = res.replace('IIII', 'IV')

        return res

if __name__ == "__main__":
    solution = Solution()
    assert solution.integerToRoman(3749) == "MMMDCCXLIX"
    assert solution.integerToRoman(58) == "LVIII"
    assert solution.integerToRoman(1994) == "MCMXCIV"

    print('All tests passed!')
