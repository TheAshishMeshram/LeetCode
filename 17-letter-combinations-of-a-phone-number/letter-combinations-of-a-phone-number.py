class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            "2":"abc","3":"def","4":"ghi",
            "5":"jkl","6":"mno","7":"pqrs",
            "8":"tuv","9":"wxyz"
        }

        res = [""]

        for digit in digits:
            temp = []
            for prefix in res:
                for ch in phone[digit]:
                    temp.append(prefix + ch)
            res = temp

        return res