"""
Solution to Leetcode 

599. Minimum Index Sum of Two Lists

link to problem: https://leetcode.com/problems/minimum-index-sum-of-two-lists/

T stands for Time Complexity
 
"""

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strings: dict = {} 
        # get the list with the smaller length
        if len(list1) > len(list2):
            big_list = list1
            small_list = list2
        else:
            big_list = list2
            small_list = list1
        # iterate through the list with smaller length
        # add every string in small_list as key and the idx as value
        # in the common_strings hashmap
        for idx, s in enumerate(small_list):
            common_strings[s] = idx
        match = {}
        # iterate through the big_list
        # and check whether the string already
        # exist in the common_strings
        # if it already exists add it to the match hashmap as key
        # and its value will be the sum of the index of the string in small_list and big_list
        for idy, ss in enumerate(big_list):
            if ss in common_strings:
                match[ss] = common_strings[ss] + idy
        # match now contains only string in both small_list and big_list as key
        # and the sum of their index as value
        min_index_sum = min(match.values()) # store the minimum index sum
        common_strings_with_min_index_sum = []
        # iterate through the match hashmap
        # and store the key(string) whose value is less than or equal to
        # the minimum index sum
        for k, v in match.items():
            if v <= min_index_sum:
                common_strings_with_min_index_sum.append(k)
        return common_strings_with_min_index_sum
    
    

# T: O(N)
# S: O(N)

# Test
# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".

# print(Solution().findRestaurant(list1, list2)) #["Shogun"]