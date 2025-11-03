class Solution(object):
    def zigzagConversion(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        idx, d = 0, 1
        rows = [''] * numRows

        

        for char in s:
            rows[idx] += char
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        return ''.join(rows)
        

if __name__ == "__main__":
    solution = Solution()
    # assert solution.zigzagConversion("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert solution.zigzagConversion("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert solution.zigzagConversion("A", 1) == "A"
    print('All tests passed!')
