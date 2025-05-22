class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        final_int = 0
        curr_max = 0

        for i in range(len(s) - 1, -1, -1):
            curr = roman_map[s[i]]
            if curr >= curr_max:
                curr_max = curr
                final_int += curr
            else:
                final_int -= curr

        return final_int
