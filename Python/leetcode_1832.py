"""
Solution to 
1832. Check if the Sentence Is Pangram

Link to Problem: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
T stands for Time Complexity
S stands for Space Complexity
"""
from ctypes import sizeof


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ascii_lowercase = ["a", "b","c", "d", "e","f","g", "h", "i", "j", "k", "l", "m","n" ,"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        assert len(ascii_lowercase) == 26 # check to ensure no letter is missing from the ascii_lowercase 
        for l in ascii_lowercase:
            if sentence.count(l) <= 0:
                return False
        return True
        
# T: O(N)
# S: O(1)

# If you are wondering why the time complexity is O(N) and not O(N**2). Then read this below:

# The first loop runs 26 times irrespective of the sentence passed. i.e its not dependent or affected by the input size
# so that its O(26), the inner loop is sentence.count(l). The time complexity is O(N) so to get the overall time complexity.
# That is O(26N). Since we drop constant time, that makes the total time complexity to be O(N).
# I hope this clears out your doubt.

# Test
# Input: 
sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

print(Solution().checkIfPangram(sentence)) #True