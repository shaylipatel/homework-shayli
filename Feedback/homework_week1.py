"""
Grade: 100%
Great work! Left comments around the file, lmk your thoughts / I hope they help out!
"""

"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""

class CashRegister:

    def __init__(self):

        self.total_items = None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):

        if self.total_items is None:
            self.total_items = {}

        self.total_items[item] = price
        self.total_price += price

    def remove_item(self, item, price):
        self.total_items.pop(item)
        self.total_price -= price

    def apply_discount(self,discount):
        if 0 <= discount < 100: # Good error handling! 
            self.discount = discount
            total_with_discount = self.total_price * ((100 - self.discount)/100)
            print('{}% discount applied\nDiscounted price: GBP{}'.format( str(self.discount), str(total_with_discount)))
        else:
            raise Exception('invalid discount')
    def get_total(self):
        print('Total: GBP {}'.format(str(self.total_price)))

    def show_items(self):
        for item in self.total_items:
            print(item)

    def reset_register(self):
        self.total_items = None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0



# EXAMPLE code run:
cashy = CashRegister()

# ADD items

cashy.add_item('chewing gum', 0.95)
cashy.add_item('chocolate bar', 1)
cashy.add_item('newspaper', 2.25)

# print total price of all items
cashy.get_total() # this technically prints out total instead of getting value?
# it depends on style of naming conventions - get_attribute is usually for just grabbing that attribute in a defensive-programming-way /
# secure way like its a private variable. however, this is a niche naming convention and not universally applicable, but regardless tho
# it may be useful note!

# print all of items
cashy.show_items()

#apply 30% discount
cashy.apply_discount(30)
# apply invalid discount to raise exception
# cashy.apply_discount(105)
# reset register
cashy.reset_register()
# check that it has reset
print(cashy.total_items)
print(cashy.total_price)
# """
#
# TASK 2
#
# Write a base class to represent a student. Below is a starter code.
# Feel free to add any more new features to your class.
# As a minimum a student has a name and age and a unique ID.
#
# Create a new subclass from student to represent a concrete student doing a specialization, for example:
# Software Student and Data Science student.
#
# """
#
#
class Student:

    def __init__(self, name, age, id, email, slack_username):
        self.name = name
        self.age = age
        self.id = id
        self.email = email
        self.slack_username = slack_username
        self.subjects = dict()

class CFGStudent(Student): # ✓

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade

    def remove_subject(self, subject):
        self.subjects.pop(subject)

    def view_subjects(self):
        for subject in self.subjects:
            print(subject)

    def average_grade(self):
        number_of_subjects = len(self.subjects)
        total_grade = sum(self.subjects.values())
        average_grade = total_grade/number_of_subjects
        print(average_grade)

    # Consider encapsulating the above methods into the normal Student class instead
    # Since none of these are specifically unique to a CFG Student / all these functions are universal to students
    # Hence better to inherit from a class that implements common-behaviours already; to set CFGStudent apart, you
    # can then add unique behaviour parts like 'stream' that a student is in (since that's only specific to CFG) or
    # a slack channel that they're in, etc

# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

shayli = CFGStudent('Shayli',26,1234, 'shayls1@aol.com', 'shaylipatel')

# add subjects and grades
shayli.add_subject('Software Specialisation', 100)
shayli.add_subject('Foundation Course', 50)
# get average for student
shayli.average_grade()
# ✓✓