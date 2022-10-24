"""
Solution to 
2288. Apply Discount to Prices

Link to Problem: https://leetcode.com/problems/apply-discount-to-prices/
T stands for Time Complexity
S stands for Space Complexity
"""
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        list_of_words = sentence.split(" ")
        discounted_sentence: str = ""
        # iterate through the list_of_words
        # check if the word is a valid price
            # if it's a valid price, compute the discount price
            # format it to 2 decimal places
        # if it's not a valid price
        # simply append it to the discounted sentence string.
        for idx, word in enumerate(list_of_words): #T: O(n)
            is_valid_price = self.validate_price(word)
            if is_valid_price:
                price = int(word[1:])
                discounted_price = price - ((discount/100) * price)
                if idx == len(list_of_words) -1:
                    discounted_sentence += (f"${discounted_price:.2f}")
                else:
                    discounted_sentence += (f"${discounted_price:.2f} ")
            else:
                if idx == len(list_of_words) -1:
                    discounted_sentence += (f"{word}")
                else:
                    discounted_sentence += (f"{word} ")    
                
        return discounted_sentence
    
    
    def validate_price(self, word: str) -> bool: # T: O(m)
        """ check whether the word price passed in
        is a valid price.
        
        i.e it must start with dollar and 
        its length must not be greater than 11
        also any every string after the first letter must be a valid number"""
        if word[0] != "$" or len(word[1:]) > 10:
            return False
        try:
            int(word[1:])
        except ValueError:
            return False
        else:
            return True
        
# T: O(n x m)
# S: O(n)

# Test
# Input: 

sentence = "there are $1 $2 and 5$ candies in the shop"
discount = 50

# Output: "there are $0.50 $1.00 and 5$ candies in the shop"

print(Solution().discountPrices(sentence, discount)) # "there are $0.50 $1.00 and 5$ candies in the shop"