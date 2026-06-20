"""
Beginner Python lesson:
- for loops
- functions
- classes

Run this file with:
    python for_loops_functions_classes_lesson.py

The goal is not to memorize everything.
The goal is to understand how Python thinks.
"""


# ---------------------------------------------------------------------------
# 1. FOR LOOPS
# ---------------------------------------------------------------------------

# A for loop repeats an action for every item inside a group of items.
#
# Think:
# "For each item in this list, do something."

students = ["Adam", "Sara", "Mehmet", "Lina"]

print("\n1. Basic for loop")

for student in students:
    print("Hello,", student)

# Explanation:
# - students is a list.
# - student is a temporary variable.
# - On each loop, Python puts one value from students into student.
#
# First loop:  student = "Adam"
# Second loop: student = "Sara"
# Third loop:  student = "Mehmet"
# Fourth loop: student = "Lina"


print("\n2. For loop with numbers")

prices = [10, 25, 40, 5]
total = 0

for price in prices:
    total = total + price
    print("Current price:", price, "| Running total:", total)

print("Final total:", total)

# Explanation:
# total starts at 0.
# Each time the loop runs, we add the current price to total.


print("\n3. For loop using range")

for number in range(1, 6):
    print("Number:", number)

# range(1, 6) means:
# start at 1
# stop before 6
#
# So it gives:
# 1, 2, 3, 4, 5


print("\n4. For loop with index and value")

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

for index, product in enumerate(products):
    print(index, product)

# enumerate gives you two things:
# - the index position
# - the actual value
#
# index 0 means the first item.
# Python lists start counting from 0.


# ---------------------------------------------------------------------------
# 2. FUNCTIONS
# ---------------------------------------------------------------------------

# A function is a reusable block of code.
#
# Think:
# "I want to give Python some inputs, let it do work, and maybe return a result."


def greet_user(first_name, last_name, city):
    """Example function with 3 parameters."""
    message = f"Hello {first_name} {last_name} from {city}!"
    return message


print("\n5. Function with 3 parameters")

greeting = greet_user("Adam", "Smith", "Istanbul")
print(greeting)

# Parameters are the names inside the function definition:
# first_name, last_name, city
#
# Arguments are the real values you pass when calling the function:
# "Adam", "Smith", "Istanbul"


def calculate_order_total(product_name, quantity, price_each, tax_rate):
    """Example function with 4 parameters."""
    subtotal = quantity * price_each
    tax = subtotal * tax_rate
    total_price = subtotal + tax

    print("Product:", product_name)
    print("Subtotal:", subtotal)
    print("Tax:", tax)

    return total_price


print("\n6. Function with 4 parameters")

order_total = calculate_order_total("Notebook", 3, 15, 0.20)
print("Total price:", order_total)

# In this example:
# product_name = "Notebook"
# quantity = 3
# price_each = 15
# tax_rate = 0.20


def create_student_report(name, math_score, english_score, science_score, attendance):
    """Example function with 5 parameters."""
    average_score = (math_score + english_score + science_score) / 3

    report = {
        "name": name,
        "math": math_score,
        "english": english_score,
        "science": science_score,
        "average": average_score,
        "attendance": attendance,
    }

    return report


print("\n7. Function with 5 parameters")

student_report = create_student_report("Sara", 90, 85, 95, "Excellent")
print(student_report)

# Functions help you avoid repeating yourself.
# If you need another student report, just call the function again:

another_report = create_student_report("Mehmet", 75, 80, 70, "Good")
print(another_report)


# ---------------------------------------------------------------------------
# 3. CLASSES
# ---------------------------------------------------------------------------

# A class is a blueprint for creating objects.
#
# Think:
# A class is like a recipe.
# An object is the actual meal made from that recipe.
#
# A class groups data and actions together.


class Student:
    """A Student class with 5 parameters."""

    def __init__(self, name, age, city, course, grade):
        self.name = name
        self.age = age
        self.city = city
        self.course = course
        self.grade = grade

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old and I study {self.course}."

    def is_passing(self):
        return self.grade >= 50


print("\n8. Class with 5 parameters")

student_one = Student("Adam", 25, "Istanbul", "Python", 88)
student_two = Student("Lina", 22, "Ankara", "Data Analysis", 45)

print(student_one.introduce())
print("Is passing?", student_one.is_passing())

print(student_two.introduce())
print("Is passing?", student_two.is_passing())

# Explanation:
# Student is the class.
# student_one and student_two are objects created from the class.
#
# __init__ runs automatically when you create a new Student.
#
# self means:
# "this specific object"
#
# student_one.name is "Adam"
# student_two.name is "Lina"
#
# They use the same class, but store different data.


class BankAccount:
    """A class with data and behavior."""

    def __init__(self, owner, bank_name, account_type, balance):
        self.owner = owner
        self.bank_name = bank_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Not enough money"

        self.balance = self.balance - amount
        return self.balance

    def account_summary(self):
        return f"{self.owner} has {self.balance} in a {self.account_type} account at {self.bank_name}."


print("\n9. Class with methods")

account = BankAccount("Adam", "Python Bank", "Savings", 1000)

print(account.account_summary())
print("After deposit:", account.deposit(250))
print("After withdrawal:", account.withdraw(400))
print(account.account_summary())

# A method is a function inside a class.
#
# deposit, withdraw, and account_summary are methods.
# They belong to BankAccount objects.


# ---------------------------------------------------------------------------
# 4. PUTTING EVERYTHING TOGETHER
# ---------------------------------------------------------------------------


class Product:
    """Product class with 4 parameters."""

    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def total_stock_value(self):
        return self.price * self.stock


print("\n10. For loop + function + class together")

store_products = [
    Product("Laptop", "Electronics", 1200, 5),
    Product("Mouse", "Electronics", 25, 50),
    Product("Notebook", "Stationery", 4, 100),
    Product("Chair", "Furniture", 80, 10),
]


def print_product_summary(product_name, category, price, stock, total_value):
    """Function with 5 parameters."""
    print(
        f"{product_name} | Category: {category} | Price: {price} | "
        f"Stock: {stock} | Total value: {total_value}"
    )


for product in store_products:
    print_product_summary(
        product.name,
        product.category,
        product.price,
        product.stock,
        product.total_stock_value(),
    )

# What happened above?
#
# 1. Product is a class.
# 2. Each Product(...) creates one product object.
# 3. store_products is a list of product objects.
# 4. The for loop goes through each product.
# 5. The function prints a clean summary for each product.


# ---------------------------------------------------------------------------
# 5. QUICK MEMORY GUIDE
# ---------------------------------------------------------------------------

# for loop:
# Use it when you want to repeat something for every item.
#
# function:
# Use it when you want reusable code that can receive inputs.
#
# class:
# Use it when you want to represent a real thing with data and actions.
#
# Example:
# - A student has data: name, age, city, course, grade
# - A student can do actions: introduce, check if passing


print("\nLesson complete. Try changing the values and running the file again.")
