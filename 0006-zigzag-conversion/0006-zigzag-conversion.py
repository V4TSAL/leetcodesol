class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows  # Create a list of strings to store each row
        index, step = 0, 1  # Initialize index and step variables
        for char in s:
            rows[index] += char  # Append the character to the appropriate row
            if index == 0:  # If at the top row, change direction to move down
                step = 1
            elif index == numRows - 1:  # If at the bottom row, change direction to move up
                step = -1
            index += step  # Update index to move to the next row

        return ''.join(rows)