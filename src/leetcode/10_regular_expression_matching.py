# I saw someone else's solution

class Solution(object):
    def regularExpressionMatching(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        return dp[m][n]

if __name__ == "__main__":
    solution = Solution()
    assert solution.regularExpressionMatching("aa", "a") == False
    assert solution.regularExpressionMatching("aa", "a*") == True
    assert solution.regularExpressionMatching("ab", ".*") == True
    assert solution.regularExpressionMatching("aab","c*a*b") == True
    assert solution.regularExpressionMatching("mississippi", "mis*is*ip*.") == True
    assert solution.regularExpressionMatching("ab", "*c") == False


    print('All tests passed!')
