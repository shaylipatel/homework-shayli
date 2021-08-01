"""
Feedback below, mark in PDF
"""
# 3. Palindrome

word = 'madam'

def Palindrome(word):
    Lindex = 0
    if Lindex == 0: # <--- this will activate anyway since the LIndex is set to 0 above?
        Rindex = 0 # <-- may as well set this without conditional statement?
    else:
        Rindex = - Lindex
    while Lindex < Rindex:
        if word[Lindex] != word[Rindex]:   #if left letter and right letter are not equal
            print('False')
        Lindex += 1   # then move to the next index to the right
        # ^ Where is the right index moved though? Would it not be in one stationary place?
        # You should start the right index at the very end of the word, and move it left (
        # so Rindex -= 1) per iteration
        # This is a v good approach for palindrome tho - index-based checking is more efficient
        # than doing [::-1] string reverse

    print('True')
Palindrome('madam')
# Palindrome('hannah')

# 4. Palindrome Unit testing
# As this is usually done in another file, the below import is usually found.
from unittest import TestCase, main
# from Nanodegree.Assessments.Assessment_2 import Palindrome

"""
Unfortunately don't think the unit tests will run correctly - the palindrome
function from above will only print a output, it will not return anything back to whatever is calling it
- hence, there is nothing to compare for the 'True' or 'False' expected variables

I understand where you're going tho, be catious regarding how these functions return values tho!
"""

class TestPalindrome(TestCase):
    def testevenpalindrome(self):
        expected = 'True'
        result = Palindrome('hannah')
        self.assertEqual(expected, result)

    def testoddpalindrome(self):
        expected = 'True'
        result = Palindrome('madam')
        self.assertEqual(expected,result)

    def testnonpalindrome(self):
        expected = 'False'
        result = Palindrome('tester')
        self.assertEqual(expected,result)

    def one_letter(self):
        expected = 'True'
        result = Palindrome('a')
        self.assertEqual(expected,result)

if __name__ == '__main__':
    main()


# You will be asked to write a function that will accept an array of numbers and an integer representing a target sum
# if any 2 numbers from the accepted number sum up to the target sun, then your function should return then in an array, in any order.
# if no 2 numbers sum up, the function should return an empty array
# Note that the target sum has to be obtained by summing 2 different numbers in the array.
# You cannot add a single integer to itself to obtain the target sum.

# Example input integer
my_numbers = [3,5,-4,8,11,1,-1,6]
target_sum = 10
# Example output returned - [-1,11]

# Test Input for multiple pairs to be in output.
# my_numbers = [30, -40, 15, -25, 7 , -17, 8, 19, -50, 46]
# target_sum = -10
new_list = []
# create an empty list. The contents will be what be printed in the output.
list_count_before = len(my_numbers)
def two_number_sum(my_numbers, target_sum, new_list):
    for number in my_numbers:           # used for loop to check all elements in my_numbers list
        target_number = target_sum - number         #to to calculate which number I would be looking for if there was a pair
        if target_number != number and target_number in my_numbers:     # this eliminates any number that is repeated and only continues if target_numbers in the my_numbers list
            new_list.append(number)                         # now we have confirmed the numbers are in the list and sum to target value, add them to the new list
            new_list.append(target_number)
            print(new_list)                 # prints the 2 numbers in a new list.
            my_numbers.remove(number)       # removes the number just checked so no future variation of the sum will print in the for loop and is only printed once
            new_list = []                   # sets the new list so it is once again empty for the next loop.
    if list_count_before == len(my_numbers):    # this checks if the number of elements before the for loop is the same after, meaning that no pairs for found for the sum
        print(new_list)                         # prints empty list

two_number_sum(my_numbers, target_sum, new_list)

"""
Good approach - this is a efficient approach to the two sum problem

Consider:
- is target_number != number needed? What if you have a list of [15, 15] and the sought value is 30? You may not
be able to get it (from my understanding) as you do not execute that if condition sees that 15 == 15
- Function should return something, ideally not print
- why remember every number using my_numbers, instead of adding to it as you go? E.g. for each iteration. append the
number you visited to the list so you can 'remember' what you have already visited before. Approach taken like this
unfortunately may be vulnerable to glitches potentially / requires more resiliency to ensure you're not double-counting
the very same number (e.g. instead of needing target_number != number which filters out the same numbers, you may need
to check based on index to ensure you are not double-counting the very same number you are using that very moment)
"""









