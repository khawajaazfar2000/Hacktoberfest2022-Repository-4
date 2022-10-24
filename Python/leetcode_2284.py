from typing import List
"""
Solution to 
2284. Sender With Largest Word Count

Link to Problem: https://leetcode.com/problems/sender-with-largest-word-count/
T stands for Time Complexity
S stands for Space Complexity
"""
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        sender_message: dict = {}
        # iterate through the messages
        # add the sender of a message as key and the length of their message as value
        # if a sender has more than one message
        # add the length of the message to the prev one
        for idx in range(len(messages)):
            if senders[idx] in sender_message:
                sender_message[senders[idx]] += len(messages[idx].split(" "))
            else:
                sender_message[senders[idx]] = len(messages[idx].split(" "))
        # find the sender with the largest word count
        # keep track of the current largest word count
        # iterate through the sender_message hashmap
        # if there is a sender with a word count greater than the current one
        # update the largest word count and the sender
        # if two senders have the same largest word count
        # return the one with lexicographically largest name
        largest_word_count, sender_of_largest_word_count = 1, senders[0]
        for sender in sender_message:
            if  sender_message[sender] > largest_word_count:
                largest_word_count = sender_message[sender]
                sender_of_largest_word_count = sender
            elif sender_message[sender] == largest_word_count and sender > sender_of_largest_word_count:
                largest_word_count = sender_message[sender]
                sender_of_largest_word_count = sender
        return sender_of_largest_word_count

# T: O(N x M)
# S: O(N)
# Where N is the length of messages and senders & 
#       M is the length of the longest sentence in messages list

#  Test
# Input: 
messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]
senders = ["Alice","userTwo","userThree","Alice"]
# Output: "Alice"

print(Solution().largestWordCount(messages, senders)) # "Alice"