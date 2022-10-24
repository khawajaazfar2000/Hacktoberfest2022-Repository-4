"""
Solution to 
38. Count and Say

Link to Problem: https://leetcode.com/problems/count-and-say/
T stands for Time Complexity
S stands for Space Complexity
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1" # base case
        count_and_say_output = self.countAndSay(n - 1)
        sub_strings = []
        ss = ""
        # iterate through the count_and_say_output
        # obtain substring that contains exactly one unique digit.
            # store the current character in ss
            # if the last char in ss does not match the current char
            # that means the current ss is a valid substring
            # and we restart ss with the current char
        for c in count_and_say_output:
            if ss == "":
                ss += c
            elif ss[-1] != c:
                sub_strings.append(ss)
                ss = c
            else:
                ss += c
        sub_strings.append(ss)
        # sub_strings contains the valid substrings
        count_and_say_output = ""
        # iterate through the sub_strings
        # and perform the count and say sequence operation
        # i.e the length of the sub_string concatenated with the digit
        # for example; 22 -> 22, 11111 -> 51
        for sub_s in sub_strings:
            count_and_say_output += str(len(sub_s)) + sub_s[0]
        return count_and_say_output
    
# T: O(N + M)
# S: O(N)

# Test
# Input: 
n = 4
# Output: "1211"

print(Solution().countAndSay(n)) # "1211"
