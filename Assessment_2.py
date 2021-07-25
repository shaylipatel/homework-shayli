# 3. Palindrome

word = 'madam'

def Palindrome(word):
    Lindex = 0
    if Lindex == 0:
        Rindex = 0
    else:
        Rindex = - Lindex
    while Lindex < Rindex:
        if word[Lindex] != word[Rindex]:   #if left letter and right letter are not equal
            print('False')
        Lindex += 1   # then move to the next index to the right
    print('True')
Palindrome('madam')
# Palindrome('hannah')

# 4. Palindrome Unit testing
# As this is usually done in another file, the below import is usually found.
from unittest import TestCase, main
# from Nanodegree.Assessments.Assessment_2 import Palindrome

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








