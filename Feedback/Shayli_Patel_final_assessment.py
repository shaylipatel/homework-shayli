"""
Grade: 78%
Like always similar to prev submissions, you've done an amazing job
Fantastic work! Your answers were on-point at each specific part, it was
a pleasure to see and mark. It's been incredibly lovely having you
on the course as well, you've been a fantastic student - all the best
for the future!
"""

"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
import random

class CFGStudent:

    def __init__(self, name, surname, age, email, id=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = id or self.generate_id()

    @staticmethod
    def generate_id():
        id = str(random.randrange(1000, 10000))
        return id

    def get_id(self):
        return self.student_id

    def get_fullname(self):
        return '{} {}'.format(self.name, self.surname)


class NanoStudent(CFGStudent):

    def __init__(self, specialisation, **kwargs ):
        # 'your code goes here'

        self.specialization = specialisation
        self.course_grades = {} #  dictionary

    @staticmethod
    def generate_id():
        id = 'NANO' + str(random.randrange(1000, 10000))
        return id


    def add_new_grade(self, assignment, mark):
        self.course_grades[assignment] = mark

    def get_course_grades(self):
        return self.course_grades



############################################

# Example run

# s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
# print(s.get_fullname())
# # returns 'Anna Smith'
# print(s.student_id())
# # returns '3868' or some other random number
#
# cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
# print(cfg_s.get_fullname())
# # returns 'Mia Papandopulu'
# print(cfg_s.get_id())
# # returns 'NANO6180' or some other random number
#
# cfg_s.add_new_grade('theory', 95)
# cfg_s.add_new_grade('project', 78)
# print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}

# 20/25
# Check the Nano subclass!

"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""

def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def even_fibonacci_sum(limit):
    indexes = [i for i in range(limit)]
    print('The indexes are: {}'.format(indexes))
    even_values = []
    for i in range(limit):
        if fib(i)%2 ==0:
            even_values.append(fib(i))
    print('The even values in the sequence are:{}'.format(even_values))
    sum = 0
    for i in even_values:
        sum += i
    return sum

# 25/25

##### TESTS ####
#
# print(even_fibonacci_sum(limit=10))  # should be 44
# print(even_fibonacci_sum(limit=15))  # should be 188
# print(even_fibonacci_sum(limit=1))   # should be 0





"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""
def is_valid_subsequence(array, sequence):
    s_index = 0
    for value in array: #look for each value of the array
        if s_index == len(sequence):    # if at the end of the sequence, break
            break
        elif value == sequence[s_index]: # if value in array is in sequence, move to next value in array
            s_index +=1
    return s_index == len(sequence) #boolean - True - if fully iterated through sequence.

# 25/25

#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""
# How can this code be improved? Is there anything missing or maybe it needs to be refactored.

#  in def update_department, use object name 'department' not 'department name' to stay consistent with object names __init__.

# Active status - use object name 'status' in __init__ and in update_status, not 'is_active' or 'new_is_active' as the employee doesn't have to be new to be active and using object name 'is_active' suggests the default is 'yes' or 'active' which may not be the default expected.

# if you are removing a employees record, then you need to delete all objects not just name and id. The ative status, department will remain unless specified.

# db_engine should be a child class to the employee class as the employee class sets the employee information and the db_engine class can save and remove (and do other actions such as amend& add).
# This break the class down into 2 distinct classes with different uses and simplifies the purposes of the employee class and db_engine class.
#The db_engine class can inherit the characteristics of the parent class (employee) so that any employee that saved or removed from the db engine easily.

"""
Grade: 8/25
Can you go into depth into the following areas:
SOLID / SRP principles (already moving forward with last area)
Exception / error handling!

Overall good answer tho - definitely go into more depth! Try to change your recommendations to be more
in tune of code-keeping rules (e.g. code should have error handling altho you have already moved towards this, code
should adhere to xyz principle which is a principle that advocates 123, etc)
"""
