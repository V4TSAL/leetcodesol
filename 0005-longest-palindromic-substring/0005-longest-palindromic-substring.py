class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        table = [[False for _ in range(n)] for _ in range(n)]
        max_length = 1
        start = 0
        for i in range(n):
            table[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                start = i
                max_length = 2
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if table[i + 1][j - 1] and s[i] == s[j]:
                    table[i][j] = True
                    if k > max_length:
                        start = i
                        max_length = k
        return s[start:start + max_length]

        