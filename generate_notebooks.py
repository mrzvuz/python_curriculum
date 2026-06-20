import json
from pathlib import Path


ROOT = Path(__file__).parent


def slugify(text):
    cleaned = []
    previous_dash = False

    for character in text.lower():
        if character.isalnum():
            cleaned.append(character)
            previous_dash = False
        elif not previous_dash:
            cleaned.append("-")
            previous_dash = True

    return "".join(cleaned).strip("-")


def markdown_cell(text):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": text.splitlines(keepends=True),
    }


def code_cell(code):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": code.splitlines(keepends=True),
    }


def notebook(title, explanation, example, exercises):
    return {
        "cells": [
            markdown_cell(
                f"# {title}\n\n"
                f"## Explanation\n\n"
                f"{explanation}\n"
            ),
            markdown_cell("## Example\n\nRun the code cell below and then change the values."),
            code_cell(example),
            markdown_cell(
                "## Exercises\n\n"
                + "\n".join(f"{index}. {exercise}" for index, exercise in enumerate(exercises, 1))
            ),
            code_cell("# Write your solution here.\n"),
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.x",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def topic(title, category, explanation, example, exercises):
    return {
        "title": title,
        "category": category,
        "explanation": explanation,
        "example": example,
        "exercises": exercises,
    }


TOPICS = [
    topic(
        "Outputs",
        "01_basics",
        "Output means showing information to the user. In Python, the most common output tool is print(). You can print text, numbers, variables, and results of calculations.",
        'print("Hello, Python!")\nname = "Adam"\nage = 25\nprint("Name:", name)\nprint("Age next year:", age + 1)',
        ["Print your name.", "Print your city and country.", "Print the result of 10 + 15."],
    ),
    topic(
        "Comments",
        "01_basics",
        "Comments are notes for humans. Python ignores comments when running code. Use comments to explain why something exists, not every tiny step.",
        '# This is a single-line comment\nname = "Adam"  # This comment explains this variable\n\n"""\nThis is a multi-line string.\nIt is often used as a longer note or docstring.\n"""\nprint(name)',
        ["Add a comment above a variable.", "Write a short comment explaining a calculation."],
    ),
    topic(
        "Variables",
        "01_basics",
        "Variables are names that store values. A variable can point to text, numbers, booleans, lists, dictionaries, objects, and more.",
        'first_name = "Adam"\nage = 25\nis_learning = True\n\nprint(first_name)\nprint(age)\nprint(is_learning)',
        ["Create variables for your name, age, and favorite language.", "Print all three variables."],
    ),
    topic(
        "Data Types",
        "01_basics",
        "A data type tells Python what kind of value something is. Common types include str, int, float, bool, list, tuple, set, dict, and NoneType.",
        'values = ["Python", 42, 3.14, True, ["a", "b"], ("x", "y"), {"red", "blue"}, {"name": "Adam"}, None]\n\nfor value in values:\n    print(value, "=>", type(value))',
        ["Create one value for each major data type.", "Use type() to print each value's type."],
    ),
    topic(
        "Numbers",
        "01_basics",
        "Python has integers for whole numbers, floats for decimal numbers, and complex numbers for advanced math.",
        "age = 25\nprice = 19.99\ncomplex_number = 2 + 3j\n\nprint(type(age), age)\nprint(type(price), price)\nprint(type(complex_number), complex_number)",
        ["Create two integers and add them.", "Create two floats and multiply them."],
    ),
    topic(
        "Casting",
        "01_basics",
        "Casting converts one data type into another. Common casting functions are int(), float(), str(), list(), tuple(), and set().",
        'number_text = "42"\nnumber = int(number_text)\nprice = float("19.99")\nmessage = str(100)\n\nprint(number + 8)\nprint(price * 2)\nprint("Score: " + message)',
        ["Convert the string '100' to an integer.", "Convert a number to a string and join it with text."],
    ),
    topic(
        "Strings",
        "01_basics",
        "A string is text. Strings can be indexed, sliced, joined, formatted, uppercased, lowercased, and searched.",
        'language = "Python"\n\nprint(language[0])\nprint(language[1:4])\nprint(language.upper())\nprint(language.lower())\nprint("I am learning " + language)',
        ["Create a string with your full name.", "Print the first letter.", "Print the uppercase version."],
    ),
    topic(
        "Booleans",
        "01_basics",
        "A boolean is either True or False. Booleans are used heavily in conditions, comparisons, and control flow.",
        "is_python_fun = True\nis_snowing = False\n\nprint(is_python_fun)\nprint(10 > 5)\nprint(3 == 7)\nprint(bool(\"hello\"))\nprint(bool(\"\"))",
        ["Create two boolean variables.", "Print the result of 20 > 10 and 5 == 9."],
    ),
    topic(
        "None",
        "01_basics",
        "None means no value. It is useful when a variable exists, but does not have a meaningful value yet.",
        'selected_user = None\n\nif selected_user is None:\n    print("No user selected yet")\nelse:\n    print(selected_user)',
        ["Create a variable set to None.", "Use if to check whether it is None."],
    ),
    topic(
        "Operators",
        "02_operators_control_flow",
        "Operators perform actions on values. Python has arithmetic, assignment, comparison, logical, identity, membership, and bitwise operators.",
        "a = 10\nb = 3\n\nprint(a + b)\nprint(a - b)\nprint(a * b)\nprint(a / b)\nprint(a // b)\nprint(a % b)\nprint(a > b)\nprint(a > 5 and b < 5)",
        ["Try every arithmetic operator.", "Create two comparisons that return True and False."],
    ),
    topic(
        "If Else",
        "02_operators_control_flow",
        "if, elif, and else let your program choose different paths based on conditions.",
        'score = 82\n\nif score >= 90:\n    print("A")\nelif score >= 80:\n    print("B")\nelif score >= 70:\n    print("C")\nelse:\n    print("Needs practice")',
        ["Create an age checker.", "Print child, teenager, adult, or senior depending on age."],
    ),
    topic(
        "Match",
        "02_operators_control_flow",
        "match is Python's pattern matching statement. It is useful when you want clean alternatives for one value. It requires Python 3.10 or newer.",
        'command = "start"\n\nmatch command:\n    case "start":\n        print("Starting")\n    case "stop":\n        print("Stopping")\n    case "pause":\n        print("Pausing")\n    case _:\n        print("Unknown command")',
        ["Create a match statement for days of the week.", "Add a default case with _."],
    ),
    topic(
        "While Loops",
        "02_operators_control_flow",
        "A while loop repeats while a condition is True. Be careful to change something inside the loop so it eventually stops.",
        'count = 1\n\nwhile count <= 5:\n    print("Count:", count)\n    count += 1',
        ["Print numbers from 1 to 10 using while.", "Create a countdown from 5 to 1."],
    ),
    topic(
        "For Loops",
        "02_operators_control_flow",
        "A for loop repeats once for every item in a sequence such as a list, tuple, string, dictionary, or range.",
        'fruits = ["apple", "banana", "cherry"]\n\nfor fruit in fruits:\n    print(fruit)\n\nfor letter in "Python":\n    print(letter)',
        ["Loop through a list of five names.", "Loop through a word and print each letter."],
    ),
    topic(
        "Range",
        "02_operators_control_flow",
        "range() creates a sequence of numbers. It is often used with for loops.",
        "for number in range(1, 6):\n    print(number)\n\nfor even_number in range(2, 11, 2):\n    print(even_number)",
        ["Print numbers 1 to 20.", "Print only multiples of 5 from 5 to 50."],
    ),
    topic(
        "Lists",
        "03_collections",
        "A list is an ordered, changeable collection. Lists can contain any data type and allow duplicate values.",
        'colors = ["red", "green", "blue"]\ncolors.append("yellow")\ncolors[1] = "black"\n\nprint(colors)\nprint(colors[0])\nprint(len(colors))',
        ["Create a list of five foods.", "Add one food.", "Change the second food."],
    ),
    topic(
        "Tuples",
        "03_collections",
        "A tuple is an ordered, unchangeable collection. Tuples are useful for values that should stay fixed.",
        'coordinates = (10, 20)\nname, age, city = ("Adam", 25, "Istanbul")\n\nprint(coordinates)\nprint(name, age, city)',
        ["Create a tuple with three city names.", "Unpack a tuple into variables."],
    ),
    topic(
        "Sets",
        "03_collections",
        "A set is an unordered collection of unique values. Sets are useful for removing duplicates and doing membership checks.",
        'numbers = {1, 2, 2, 3, 4, 4}\nnumbers.add(5)\n\nprint(numbers)\nprint(3 in numbers)',
        ["Create a set with duplicate values.", "Add a new value.", "Check if a value exists."],
    ),
    topic(
        "Dictionaries",
        "03_collections",
        "A dictionary stores key-value pairs. Use a key to look up a value.",
        'student = {"name": "Adam", "age": 25, "course": "Python"}\nstudent["grade"] = 95\n\nprint(student["name"])\nprint(student.get("course"))\nprint(student)',
        ["Create a dictionary for a product.", "Add a price key.", "Print one value using its key."],
    ),
    topic(
        "Arrays",
        "03_collections",
        "Python lists are usually used as arrays. For numeric arrays, NumPy is the common choice. The built-in array module can also store typed arrays.",
        "from array import array\n\nscores = array('i', [80, 90, 75, 100])\nscores.append(85)\n\nfor score in scores:\n    print(score)",
        ["Create an integer array.", "Append a number.", "Loop through the array."],
    ),
    topic(
        "Remove List Duplicates",
        "03_collections",
        "Duplicates can be removed with set(), but that may not preserve order. A loop with a seen set can preserve order.",
        'items = ["apple", "banana", "apple", "cherry", "banana"]\nunique_items = []\nseen = set()\n\nfor item in items:\n    if item not in seen:\n        unique_items.append(item)\n        seen.add(item)\n\nprint(unique_items)',
        ["Remove duplicates from a list of numbers.", "Keep the original order."],
    ),
    topic(
        "Functions",
        "04_functions_oop",
        "A function is reusable code. Parameters are the input names in the definition. Arguments are the real values passed into the function.",
        'def calculate_total(product, quantity, price, tax_rate):\n    subtotal = quantity * price\n    tax = subtotal * tax_rate\n    return product, subtotal + tax\n\nname, total = calculate_total("Book", 3, 12.5, 0.2)\nprint(name, total)',
        ["Create a function with 3 parameters.", "Create a function with 5 parameters.", "Return a value from each function."],
    ),
    topic(
        "Built-in Functions",
        "04_functions_oop",
        "Built-in functions are always available in Python. Examples include print(), len(), type(), sum(), min(), max(), sorted(), input(), and range().",
        'numbers = [10, 4, 7, 20]\n\nprint(len(numbers))\nprint(sum(numbers))\nprint(min(numbers))\nprint(max(numbers))\nprint(sorted(numbers))',
        ["Use len() on a string.", "Use sum() on a list of numbers.", "Use sorted() on a list."],
    ),
    topic(
        "User Input",
        "04_functions_oop",
        "input() reads text typed by the user. It always returns a string, so cast it when you need a number.",
        'name = input("Enter your name: ")\nage = int(input("Enter your age: "))\n\nprint("Hello", name)\nprint("Next year you will be", age + 1)',
        ["Ask the user for two numbers.", "Convert them to integers.", "Print their sum."],
    ),
    topic(
        "Iterators",
        "04_functions_oop",
        "An iterator is an object that gives values one at a time. iter() creates an iterator and next() gets the next value.",
        'numbers = [10, 20, 30]\niterator = iter(numbers)\n\nprint(next(iterator))\nprint(next(iterator))\nprint(next(iterator))',
        ["Create an iterator from a tuple.", "Use next() to print each value."],
    ),
    topic(
        "OOP",
        "04_functions_oop",
        "Object-oriented programming groups data and behavior together. Classes describe things. Objects are specific examples of those things.",
        'class Car:\n    def __init__(self, brand, model, year):\n        self.brand = brand\n        self.model = model\n        self.year = year\n\n    def describe(self):\n        return f"{self.year} {self.brand} {self.model}"\n\ncar = Car("Toyota", "Corolla", 2020)\nprint(car.describe())',
        ["Create a Book class.", "Give it title, author, and pages.", "Add a method that describes the book."],
    ),
    topic(
        "Classes and Objects",
        "04_functions_oop",
        "A class is a blueprint. An object is a real instance created from that blueprint.",
        'class Dog:\n    def bark(self):\n        print("Woof")\n\nmy_dog = Dog()\nmy_dog.bark()',
        ["Create a Phone class.", "Create two phone objects.", "Call a method on each object."],
    ),
    topic(
        "__init__ Methods",
        "04_functions_oop",
        "__init__ runs automatically when a new object is created. Use it to set starting values.",
        'class Student:\n    def __init__(self, name, age, course, grade):\n        self.name = name\n        self.age = age\n        self.course = course\n        self.grade = grade\n\nstudent = Student("Adam", 25, "Python", 95)\nprint(student.name, student.grade)',
        ["Create a Product class with __init__.", "Use at least 4 parameters.", "Print the object properties."],
    ),
    topic(
        "Self Parameters",
        "04_functions_oop",
        "self refers to the current object. It lets each object keep its own data.",
        'class Counter:\n    def __init__(self):\n        self.value = 0\n\n    def increase(self):\n        self.value += 1\n\ncounter_one = Counter()\ncounter_two = Counter()\ncounter_one.increase()\ncounter_one.increase()\ncounter_two.increase()\n\nprint(counter_one.value)\nprint(counter_two.value)',
        ["Create two objects from one class.", "Change one object.", "Show that the other object is separate."],
    ),
    topic(
        "Class Properties",
        "04_functions_oop",
        "Class properties belong to the class. Instance properties belong to each object.",
        'class Employee:\n    company = "Python Corp"\n\n    def __init__(self, name, role):\n        self.name = name\n        self.role = role\n\nemployee = Employee("Adam", "Developer")\nprint(employee.name)\nprint(employee.company)',
        ["Create a class property called school.", "Create two student objects.", "Print the shared school value."],
    ),
    topic(
        "Class Methods",
        "04_functions_oop",
        "A class method receives the class as cls. It is often used for alternate constructors or class-level behavior.",
        'class User:\n    user_count = 0\n\n    def __init__(self, name):\n        self.name = name\n        User.user_count += 1\n\n    @classmethod\n    def total_users(cls):\n        return cls.user_count\n\nUser("Adam")\nUser("Sara")\nprint(User.total_users())',
        ["Create a class method that returns a class variable.", "Create objects and watch the class variable change."],
    ),
    topic(
        "Inheritance",
        "04_functions_oop",
        "Inheritance lets one class reuse another class. The child class gets methods and properties from the parent class.",
        'class Animal:\n    def speak(self):\n        return "Some sound"\n\nclass Cat(Animal):\n    def speak(self):\n        return "Meow"\n\ncat = Cat()\nprint(cat.speak())',
        ["Create a Vehicle parent class.", "Create a Car child class.", "Override one method."],
    ),
    topic(
        "Polymorphism",
        "04_functions_oop",
        "Polymorphism means different objects can use the same method name but behave differently.",
        'class Email:\n    def send(self):\n        print("Sending email")\n\nclass SMS:\n    def send(self):\n        print("Sending SMS")\n\nmessages = [Email(), SMS()]\n\nfor message in messages:\n    message.send()',
        ["Create three shape classes with an area() method.", "Loop through them and call area()."],
    ),
    topic(
        "Encapsulation",
        "04_functions_oop",
        "Encapsulation protects internal data and exposes controlled methods. Python uses naming conventions like _protected and __private.",
        'class BankAccount:\n    def __init__(self, owner, balance):\n        self.owner = owner\n        self.__balance = balance\n\n    def deposit(self, amount):\n        if amount > 0:\n            self.__balance += amount\n\n    def get_balance(self):\n        return self.__balance\n\naccount = BankAccount("Adam", 100)\naccount.deposit(50)\nprint(account.get_balance())',
        ["Create a class with a private variable.", "Add a getter method.", "Add a method that changes it safely."],
    ),
    topic(
        "Inner Classes",
        "04_functions_oop",
        "An inner class is a class defined inside another class. It can be useful when one object only makes sense inside another.",
        'class Computer:\n    class CPU:\n        def info(self):\n            return "CPU is processing"\n\n    def __init__(self, brand):\n        self.brand = brand\n        self.cpu = Computer.CPU()\n\ncomputer = Computer("Lenovo")\nprint(computer.brand)\nprint(computer.cpu.info())',
        ["Create an outer class called House.", "Create an inner class called Room.", "Create and use the inner object."],
    ),
    topic(
        "Modules",
        "05_standard_library",
        "A module is a Python file or library you can import. Modules help organize and reuse code.",
        "import math\nimport random\n\nprint(math.sqrt(25))\nprint(random.randint(1, 10))",
        ["Import math and use ceil().", "Import random and choose a random item from a list."],
    ),
    topic(
        "Dates",
        "05_standard_library",
        "The datetime module helps you work with dates and times.",
        "from datetime import datetime, date, timedelta\n\nnow = datetime.now()\ntoday = date.today()\ntomorrow = today + timedelta(days=1)\n\nprint(now)\nprint(today)\nprint(tomorrow)",
        ["Print today's date.", "Create a date 7 days from today."],
    ),
    topic(
        "Math Module",
        "05_standard_library",
        "The math module provides useful mathematical functions and constants.",
        "import math\n\nprint(math.sqrt(64))\nprint(math.ceil(4.2))\nprint(math.floor(4.9))\nprint(math.pi)",
        ["Use math.pow().", "Use math.factorial().", "Print math.pi."],
    ),
    topic(
        "JSON",
        "05_standard_library",
        "JSON is a common format for sharing structured data. The json module converts between Python objects and JSON strings.",
        'import json\n\nuser = {"name": "Adam", "age": 25, "skills": ["Python", "Pandas"]}\njson_text = json.dumps(user, indent=2)\nprint(json_text)\n\nback_to_python = json.loads(json_text)\nprint(back_to_python["name"])',
        ["Convert a dictionary to JSON.", "Convert JSON back into a dictionary."],
    ),
    topic(
        "RegEx",
        "05_standard_library",
        "Regular expressions search for text patterns. Python uses the re module for RegEx.",
        'import re\n\ntext = "Email me at adam@example.com"\nmatch = re.search(r"\\w+@\\w+\\.\\w+", text)\n\nif match:\n    print(match.group())',
        ["Find all numbers in a string.", "Check whether a string starts with a capital letter."],
    ),
    topic(
        "Random Module",
        "05_standard_library",
        "The random module creates random numbers and random choices.",
        'import random\n\nprint(random.randint(1, 6))\nprint(random.choice(["red", "green", "blue"]))\nprint(random.sample(range(1, 50), 6))',
        ["Simulate rolling a dice.", "Choose a random name from a list."],
    ),
    topic(
        "Statistics Module",
        "05_standard_library",
        "The statistics module calculates mean, median, mode, and other statistics.",
        "import statistics\n\nscores = [80, 90, 75, 90, 100]\nprint(statistics.mean(scores))\nprint(statistics.median(scores))\nprint(statistics.mode(scores))",
        ["Calculate the average of five numbers.", "Calculate the median of a list."],
    ),
    topic(
        "Requests Module",
        "05_standard_library",
        "requests is a popular third-party module for HTTP requests. Install it with pip if needed. Network calls may fail without internet.",
        'import requests\n\nurl = "https://api.github.com"\nresponse = requests.get(url, timeout=10)\nprint(response.status_code)\nprint(response.headers["content-type"])',
        ["Install requests if needed.", "Fetch a public API.", "Print the response status code."],
    ),
    topic(
        "PIP",
        "06_environment_files_errors",
        "pip installs and manages Python packages. Use it from the terminal, not usually inside Python code.",
        '# Terminal examples:\n# python3 -m pip install requests\n# python3 -m pip list\n# python3 -m pip freeze > requirements.txt\n\nprint("Use pip from your terminal to install packages.")',
        ["Run python3 -m pip list in the terminal.", "Install a small package such as requests."],
    ),
    topic(
        "VirtualEnv",
        "06_environment_files_errors",
        "A virtual environment keeps project packages separate from your global Python installation.",
        '# Terminal examples:\n# python3 -m venv .venv\n# source .venv/bin/activate\n# python3 -m pip install pandas\n# deactivate\n\nprint("Virtual environments keep dependencies organized.")',
        ["Create a virtual environment.", "Activate it.", "Install one package inside it."],
    ),
    topic(
        "Try Except Error Handlers",
        "06_environment_files_errors",
        "try and except let your program handle errors instead of crashing immediately.",
        'try:\n    number = int("abc")\nexcept ValueError:\n    print("That text cannot become an integer")\nfinally:\n    print("This always runs")',
        ["Handle division by zero.", "Handle a missing dictionary key."],
    ),
    topic(
        "Exceptions",
        "06_environment_files_errors",
        "Exceptions are errors Python raises when something goes wrong. You can catch built-in exceptions or raise your own.",
        'def divide(a, b):\n    if b == 0:\n        raise ValueError("b cannot be zero")\n    return a / b\n\ntry:\n    print(divide(10, 0))\nexcept ValueError as error:\n    print("Error:", error)',
        ["Raise a ValueError for invalid age.", "Catch the error and print a friendly message."],
    ),
    topic(
        "File Handling",
        "06_environment_files_errors",
        "File handling means opening, reading, writing, appending, and closing files. The with statement closes files automatically.",
        'from pathlib import Path\n\npath = Path("sample.txt")\npath.write_text("Hello file", encoding="utf-8")\ncontent = path.read_text(encoding="utf-8")\nprint(content)',
        ["Create a text file.", "Read it back.", "Print the content."],
    ),
    topic(
        "Read Files",
        "06_environment_files_errors",
        "Reading a file loads existing content from disk. pathlib makes simple file reading clear.",
        'from pathlib import Path\n\npath = Path("sample_read.txt")\npath.write_text("Line 1\\nLine 2", encoding="utf-8")\n\nfor line in path.read_text(encoding="utf-8").splitlines():\n    print(line)',
        ["Read a file line by line.", "Count how many lines are in the file."],
    ),
    topic(
        "Write and Create Files",
        "06_environment_files_errors",
        "Writing creates a file if it does not exist or replaces content if it does. Appending adds to the end.",
        'from pathlib import Path\n\npath = Path("notes.txt")\npath.write_text("First line\\n", encoding="utf-8")\n\nwith path.open("a", encoding="utf-8") as file:\n    file.write("Second line\\n")\n\nprint(path.read_text(encoding="utf-8"))',
        ["Create a file called todo.txt.", "Write three lines to it.", "Append one more line."],
    ),
    topic(
        "Delete Files",
        "06_environment_files_errors",
        "Files can be deleted with pathlib's unlink() or os.remove(). Always check that the file exists before deleting.",
        'from pathlib import Path\n\npath = Path("temporary_file.txt")\npath.write_text("Delete me", encoding="utf-8")\n\nif path.exists():\n    path.unlink()\n    print("File deleted")',
        ["Create a temporary file.", "Check if it exists.", "Delete it safely."],
    ),
    topic(
        "String Formatting",
        "07_methods_reference",
        "String formatting inserts values into text. f-strings are the modern, readable choice.",
        'name = "Adam"\nage = 25\nprice = 19.987\n\nprint(f"My name is {name} and I am {age}.")\nprint(f"Price: ${price:.2f}")',
        ["Format your name and city.", "Format a float to two decimal places."],
    ),
    topic(
        "String Methods",
        "07_methods_reference",
        "String methods are actions attached to string values, such as upper(), lower(), strip(), replace(), split(), and startswith().",
        'text = "  Python is fun  "\n\nprint(text.strip())\nprint(text.upper())\nprint(text.replace("fun", "powerful"))\nprint(text.strip().split())',
        ["Use strip() on messy text.", "Replace one word.", "Split a sentence into words."],
    ),
    topic(
        "List Methods",
        "07_methods_reference",
        "List methods modify or inspect lists. Common methods include append(), extend(), insert(), remove(), pop(), sort(), and reverse().",
        'numbers = [3, 1, 2]\nnumbers.append(4)\nnumbers.sort()\nprint(numbers)\n\nremoved = numbers.pop()\nprint(removed)\nprint(numbers)',
        ["Use append(), insert(), and remove().", "Sort a list.", "Reverse a list."],
    ),
    topic(
        "Dictionary Methods",
        "07_methods_reference",
        "Dictionary methods help access and update key-value data. Common methods include get(), keys(), values(), items(), update(), and pop().",
        'person = {"name": "Adam", "age": 25}\n\nprint(person.get("name"))\nprint(person.keys())\nprint(person.values())\nperson.update({"city": "Istanbul"})\nprint(person)',
        ["Use get() for a missing key.", "Loop through items().", "Update a dictionary."],
    ),
    topic(
        "Tuple Methods",
        "07_methods_reference",
        "Tuples are immutable, so they have fewer methods. The main methods are count() and index().",
        'values = ("a", "b", "a", "c")\n\nprint(values.count("a"))\nprint(values.index("c"))',
        ["Count how many times a value appears.", "Find the index of a value."],
    ),
    topic(
        "Set Methods",
        "07_methods_reference",
        "Set methods support unique values and math-like operations such as union, intersection, and difference.",
        'a = {1, 2, 3}\nb = {3, 4, 5}\n\nprint(a.union(b))\nprint(a.intersection(b))\nprint(a.difference(b))',
        ["Create two sets.", "Find their union.", "Find their intersection."],
    ),
    topic(
        "File Methods",
        "07_methods_reference",
        "File objects have methods like read(), readline(), readlines(), write(), and close(). The with statement is preferred because it closes automatically.",
        'from pathlib import Path\n\npath = Path("file_methods_demo.txt")\nwith path.open("w", encoding="utf-8") as file:\n    file.write("First line\\nSecond line\\n")\n\nwith path.open("r", encoding="utf-8") as file:\n    print(file.readline())',
        ["Use write() to create content.", "Use readlines() to read all lines."],
    ),
    topic(
        "Keywords",
        "07_methods_reference",
        "Keywords are reserved words in Python. You cannot use them as variable names.",
        "import keyword\n\nprint(keyword.kwlist)\nprint(keyword.iskeyword('class'))\nprint(keyword.iskeyword('student'))",
        ["Print all Python keywords.", "Check if 'for' is a keyword.", "Check if your name is a keyword."],
    ),
    topic(
        "Glossary",
        "07_methods_reference",
        "A glossary helps you remember common programming words: variable, function, parameter, argument, class, object, method, module, package, exception, and loop.",
        'glossary = {\n    "variable": "a name that stores a value",\n    "function": "reusable code",\n    "class": "a blueprint for objects",\n    "object": "an instance of a class",\n}\n\nfor word, meaning in glossary.items():\n    print(word, "=>", meaning)',
        ["Add five new words to the glossary.", "Loop through and print them."],
    ),
    topic(
        "Built-in Modules",
        "07_methods_reference",
        "Python includes many built-in modules such as math, random, datetime, json, pathlib, os, sys, statistics, and re.",
        "import sys\nimport pathlib\nimport statistics\n\nprint(sys.version)\nprint(pathlib.Path.cwd())\nprint(statistics.mean([1, 2, 3]))",
        ["Import pathlib and print the current folder.", "Import os and print the current working directory."],
    ),
    topic(
        "Reverse a String",
        "08_small_challenges",
        "Strings can be reversed with slicing. The slice [::-1] means start at the end and move backwards.",
        'text = "Python"\nreversed_text = text[::-1]\nprint(reversed_text)',
        ["Reverse your name.", "Create a function that reverses any string."],
    ),
    topic(
        "Add Two Numbers",
        "08_small_challenges",
        "Adding numbers is simple, but remember that input() returns strings, so cast input values before math.",
        'a = 10\nb = 15\nprint(a + b)\n\ndef add_numbers(first, second):\n    return first + second\n\nprint(add_numbers(5, 7))',
        ["Ask the user for two numbers.", "Convert both to float.", "Print the sum."],
    ),
    topic(
        "NumPy Tutorial",
        "09_data_science",
        "NumPy is used for fast numerical arrays. It is the foundation for much of Python data science.",
        "import numpy as np\n\nnumbers = np.array([1, 2, 3, 4, 5])\nprint(numbers)\nprint(numbers * 2)\nprint(numbers.mean())",
        ["Create a NumPy array.", "Multiply it by 10.", "Find its mean."],
    ),
    topic(
        "Pandas Tutorial",
        "09_data_science",
        "Pandas is used for tabular data. DataFrames are like powerful spreadsheets in Python.",
        'import pandas as pd\n\ndata = {\n    "name": ["Adam", "Sara", "Lina"],\n    "score": [90, 85, 95],\n}\n\ndf = pd.DataFrame(data)\nprint(df)\nprint(df["score"].mean())',
        ["Create a DataFrame with products and prices.", "Print the average price."],
    ),
    topic(
        "SciPy Tutorial",
        "09_data_science",
        "SciPy builds on NumPy and provides scientific tools for optimization, statistics, signal processing, and more.",
        "import numpy as np\nfrom scipy import stats\n\nscores = np.array([80, 90, 90, 100, 70])\nprint(stats.describe(scores))",
        ["Use scipy.stats to describe a list of numbers.", "Calculate a z-score."],
    ),
    topic(
        "Matplotlib",
        "10_visualization",
        "Matplotlib is a popular plotting library. It can create line charts, scatter plots, bar charts, histograms, and pie charts.",
        "import matplotlib.pyplot as plt\n\nx = [1, 2, 3, 4]\ny = [10, 15, 13, 20]\n\nplt.plot(x, y)\nplt.show()",
        ["Create a simple line chart.", "Change the x and y values."],
    ),
    topic(
        "Pyplot",
        "10_visualization",
        "pyplot is the common Matplotlib interface imported as plt.",
        "import matplotlib.pyplot as plt\n\nplt.figure(figsize=(6, 4))\nplt.plot([1, 2, 3], [2, 4, 6])\nplt.title('Simple Pyplot Example')\nplt.show()",
        ["Create a figure.", "Add a title.", "Show the plot."],
    ),
    topic(
        "Plotting",
        "10_visualization",
        "Plotting turns data into visual form. Start with simple line charts before moving to specialized charts.",
        "import matplotlib.pyplot as plt\n\nmonths = ['Jan', 'Feb', 'Mar']\nsales = [100, 150, 120]\n\nplt.plot(months, sales)\nplt.xlabel('Month')\nplt.ylabel('Sales')\nplt.show()",
        ["Plot your own monthly values.", "Add x and y labels."],
    ),
    topic(
        "Markers",
        "10_visualization",
        "Markers show individual data points on a plot.",
        "import matplotlib.pyplot as plt\n\nplt.plot([1, 2, 3, 4], [10, 20, 15, 30], marker='o')\nplt.show()",
        ["Try marker='x'.", "Try marker='s'.", "Change the line color."],
    ),
    topic(
        "Line Labels",
        "10_visualization",
        "Labels and legends explain what your chart shows.",
        "import matplotlib.pyplot as plt\n\nplt.plot([1, 2, 3], [10, 20, 30], label='Sales')\nplt.plot([1, 2, 3], [8, 15, 25], label='Profit')\nplt.legend()\nplt.show()",
        ["Create two lines.", "Give each line a label.", "Show the legend."],
    ),
    topic(
        "Grid",
        "10_visualization",
        "A grid helps readers compare values on a chart.",
        "import matplotlib.pyplot as plt\n\nplt.plot([1, 2, 3], [5, 10, 7])\nplt.grid(True)\nplt.show()",
        ["Add a grid to a chart.", "Try grid(axis='y')."],
    ),
    topic(
        "Subplot",
        "10_visualization",
        "Subplots let you show multiple charts in one figure.",
        "import matplotlib.pyplot as plt\n\nplt.subplot(1, 2, 1)\nplt.plot([1, 2, 3], [1, 4, 9])\nplt.title('Squares')\n\nplt.subplot(1, 2, 2)\nplt.plot([1, 2, 3], [1, 8, 27])\nplt.title('Cubes')\n\nplt.tight_layout()\nplt.show()",
        ["Create two subplots.", "Put a different chart in each subplot."],
    ),
    topic(
        "Scatter",
        "10_visualization",
        "Scatter plots show relationships between two numeric variables.",
        "import matplotlib.pyplot as plt\n\nheights = [160, 170, 180, 190]\nweights = [55, 65, 80, 90]\n\nplt.scatter(heights, weights)\nplt.xlabel('Height')\nplt.ylabel('Weight')\nplt.show()",
        ["Create a scatter plot for study hours and scores.", "Add labels."],
    ),
    topic(
        "Bars",
        "10_visualization",
        "Bar charts compare categories.",
        "import matplotlib.pyplot as plt\n\nproducts = ['A', 'B', 'C']\nsales = [30, 50, 20]\n\nplt.bar(products, sales)\nplt.show()",
        ["Create a bar chart of favorite foods.", "Add a title."],
    ),
    topic(
        "Histograms",
        "10_visualization",
        "Histograms show the distribution of numeric data.",
        "import matplotlib.pyplot as plt\n\nages = [18, 20, 21, 21, 22, 25, 30, 31, 35, 40]\n\nplt.hist(ages, bins=5)\nplt.show()",
        ["Create a histogram of scores.", "Try different bin values."],
    ),
    topic(
        "Pie Charts",
        "10_visualization",
        "Pie charts show parts of a whole. Use them only when there are a few categories.",
        "import matplotlib.pyplot as plt\n\nlabels = ['Rent', 'Food', 'Savings']\nvalues = [50, 30, 20]\n\nplt.pie(values, labels=labels, autopct='%1.1f%%')\nplt.show()",
        ["Create a pie chart for a monthly budget.", "Use autopct to show percentages."],
    ),
    topic(
        "Django Tutorial",
        "11_web",
        "Django is a full-stack web framework. It helps you build web apps with URLs, views, templates, models, forms, authentication, and an admin panel.",
        '# Terminal examples:\n# python3 -m pip install django\n# django-admin startproject mysite\n# cd mysite\n# python3 manage.py runserver\n\nprint("Django projects are usually created from the terminal.")',
        ["Install Django in a virtual environment.", "Create a new Django project.", "Run the development server."],
    ),
]


README_INTRO = """# Python Notebook Curriculum

This folder contains separate Jupyter notebooks for Python topics.

Each notebook has:

1. Explanation
2. Runnable example
3. Exercises
4. Empty code cell for your solution
5. Possible solution

Recommended order:

"""


def write_notebooks():
    for item in TOPICS:
        category_dir = ROOT / item["category"]
        category_dir.mkdir(exist_ok=True)

        filename = f"{slugify(item['title'])}.ipynb"
        path = category_dir / filename
        content = notebook(
            item["title"],
            item["explanation"],
            item["example"],
            item["exercises"],
        )
        path.write_text(json.dumps(content, indent=2), encoding="utf-8")


def write_readme():
    grouped = {}
    for item in TOPICS:
        grouped.setdefault(item["category"], []).append(item)

    lines = [README_INTRO]

    for category, items in grouped.items():
        title = category.replace("_", " ").title()
        lines.append(f"## {title}\n")

        for item in items:
            filename = f"{slugify(item['title'])}.ipynb"
            lines.append(f"- [{item['title']}]({category}/{filename})")

        lines.append("")

    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    write_notebooks()
    write_readme()
    from add_solutions import main as add_solutions

    add_solutions()
    print(f"Created {len(TOPICS)} notebooks in {ROOT}")


if __name__ == "__main__":
    main()
