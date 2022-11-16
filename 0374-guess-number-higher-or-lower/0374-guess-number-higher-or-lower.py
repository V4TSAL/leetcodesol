class Solution:
    def guessNumber(self, n, s=1):
        
        while s <= n:
            m = (n + s) // 2          # [1] Take the middle point...
            g = guess(m)              # [2] ...and guess!
            if g == 0 : return m      # [3] Yay, we found the number!
            if g < 0  : n = m - 1     # [4] Nope, it's smaller...
            if g > 0  : s = m + 1     # [5] ...or larger.