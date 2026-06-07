class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        seen_digit = False
        seen_dot = False
        seen_e = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True

            elif ch in ['+', '-']:
                if i > 0 and s[i - 1].lower() != 'e':
                    return False

            elif ch == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True

            elif ch.lower() == 'e':
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False

            else:
                return False

        return seen_digit