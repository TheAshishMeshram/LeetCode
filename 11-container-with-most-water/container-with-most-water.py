class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        answer = 0

        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width

            answer = max(answer, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return answer