from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        ans = 0

        for row in matrix:
            for j in range(n):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []
            temp = heights + [0]

            for i, h in enumerate(temp):
                while stack and temp[stack[-1]] > h:
                    height = temp[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1

                    ans = max(ans, height * width)

                stack.append(i)

        return ans