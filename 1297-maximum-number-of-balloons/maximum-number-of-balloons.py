from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text):
        cnt = Counter(text)

        return min(
            cnt['b'],
            cnt['a'],
            cnt['l']//2,
            cnt['o']//2,
            cnt['n']
        )