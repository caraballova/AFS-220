# Like many programming languages, Python uses variables to store information. A variable has a name and a value. It is the value that determines what type of variable it is, NOT the name.  Examples of types in Python are strings, floats, Booleans (true/false), integers, lists, etc.

# One thing to remember about Python variables is that the variable name is associated with a pointer that shows the program where the value is stored in memory.

x = ["A", "B", "C"]     # Python list uses [ ]

y = x                   # y and x now point to the same location

# The value determines the type:

a = 12                  # integer

b = "12"                # string

c = 1.2                 # float

d = [12, "12", 1.2]     # list


# Python Operators

# Math Operators
2 + 2              # addition

2 - 2              # subtraction

2 * 2              # multiplication

2 / 2              # division

3 // 2             # 1 (division to get the integer quotient only)

3 ** 2             # 9 (3 raised to the 2nd power)


# Modular Math Returns Remainders
6 % 4              # 2  (6 modulo 4 has a remainder of 2)

12 % 4             # 0 (12 modulo 4 has a remainder of 0)


# Comparisons for numbers
2 < 1                          # False, 2 is not less than 1

2 <= 2                         # True, 2 is equal to 2

2 > 1                          # True, 2 is greater than 1

2 >= 1                         # True, 2 is greater than 1

2 == 1                         # False, 2 is not equal to 1

2 != 1                         # True, 2 is not equal to 1


# Python Modules

# Python scripts stored in separate files may be referred to as 'modules.'  It is common to make separate modules if you want to re-use the code in various places or even in a different project.  Some modules are built in to the Python language, and some are created by developers to accomplish common tasks.  To use a module in your current script, it must be imported first.

import time                     # time is a module that has functions related to computer clock timing

start_time = time.time()

end_time = time.time()

elapsed_time = end_time - start_time


# Python Classes
# Python classes are used to create objects which have functions and data that are related to a real-world object.  Different instances of a class have the same characteristics or parameters, but can have different values for the variables of the class.
# A good rule of thumb is to name classes with a noun that represents a real-world object, and name the functions in the class with verbs that represent actions or operations related to the object.  Lets use an Employee class as an example.

class Employee:

    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.status = ""

    def set_status(self, status):
        self.status = status

# Every instance of the class 'Employee' is going to have the same variables, but different values because each real-world Employee is different.

# Create an instance of the class with an instance name 'emp1' like this:

emp1 = Employee("Alice", 28)    # Initializes the class

# At this point, the new Employee class has a null value for the 'status' variable because during the init function, status was set to "".  To change it, you use the function called set_status with a value that you pass to the function.

emp1.set_status("trained")

# Then, if you print the variable, the new value will display:

print(emp1.first_name)       # Outputs  Alice
print(emp1.status)           # Outputs  trained


# Jira is a project management tool used widely by software developers. The makers of Jira offer a free, self-paced learning path for beginners that contains three short courses plus an assessment (total time: about 90 minutes). If you score 80% or higher on the assessment, you will get a Jira Badge!

# The courses are:

# Get started with Jira
# Basic Jira navigation
# Jira best practices
# You will complete one course per week in Weeks 1-3, and the Jira Fundamentals Assessment in Week 4. This will give you a valuable understanding of Jira and how it is used in project    management. Follow the instructions below to complete the first course: Get started with Jira.


