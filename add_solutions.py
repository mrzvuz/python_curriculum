import json
from pathlib import Path


ROOT = Path(__file__).parent


SOLUTIONS = {
    "outputs": 'print("Adam")\nprint("Istanbul, Turkey")\nprint(10 + 15)',
    "comments": '# Store the learner name\nname = "Adam"\n\n# Add two numbers to calculate the total\ntotal = 10 + 15\nprint(name)\nprint(total)',
    "variables": 'name = "Adam"\nage = 25\nfavorite_language = "Python"\n\nprint(name)\nprint(age)\nprint(favorite_language)',
    "data-types": 'values = [\n    "Python",\n    100,\n    3.5,\n    True,\n    ["apple", "banana"],\n    ("red", "blue"),\n    {"python", "sql"},\n    {"name": "Adam", "age": 25},\n    None,\n]\n\nfor value in values:\n    print(value, type(value))',
    "numbers": "first_integer = 12\nsecond_integer = 8\nprint(first_integer + second_integer)\n\nfirst_float = 2.5\nsecond_float = 4.0\nprint(first_float * second_float)",
    "casting": 'number = int("100")\nprint(number + 50)\n\nscore = 95\nmessage = "Your score is " + str(score)\nprint(message)',
    "strings": 'full_name = "Adam Smith"\nprint(full_name[0])\nprint(full_name.upper())',
    "booleans": "is_learning = True\nis_finished = False\n\nprint(is_learning)\nprint(is_finished)\nprint(20 > 10)\nprint(5 == 9)",
    "none": 'current_task = None\n\nif current_task is None:\n    print("There is no current task.")\nelse:\n    print(current_task)',
    "operators": "a = 20\nb = 6\n\nprint(a + b)\nprint(a - b)\nprint(a * b)\nprint(a / b)\nprint(a // b)\nprint(a % b)\nprint(a ** b)\n\nprint(a > b)\nprint(a == b)",
    "if-else": 'age = 25\n\nif age < 13:\n    print("child")\nelif age < 20:\n    print("teenager")\nelif age < 65:\n    print("adult")\nelse:\n    print("senior")',
    "match": 'day = "Monday"\n\nmatch day:\n    case "Monday":\n        print("Start of the week")\n    case "Friday":\n        print("Almost weekend")\n    case "Saturday" | "Sunday":\n        print("Weekend")\n    case _:\n        print("Regular weekday")',
    "while-loops": 'number = 1\nwhile number <= 10:\n    print(number)\n    number += 1\n\ncountdown = 5\nwhile countdown >= 1:\n    print(countdown)\n    countdown -= 1',
    "for-loops": 'names = ["Adam", "Sara", "Lina", "Mehmet", "Zeynep"]\n\nfor name in names:\n    print(name)\n\nfor letter in "Python":\n    print(letter)',
    "range": "for number in range(1, 21):\n    print(number)\n\nfor number in range(5, 51, 5):\n    print(number)",
    "lists": 'foods = ["pizza", "soup", "salad", "rice", "pasta"]\nfoods.append("kebab")\nfoods[1] = "sandwich"\nprint(foods)',
    "tuples": 'cities = ("Istanbul", "Ankara", "Izmir")\nfirst_city, second_city, third_city = cities\n\nprint(cities)\nprint(first_city)\nprint(second_city)\nprint(third_city)',
    "sets": 'numbers = {1, 2, 2, 3, 4, 4}\nnumbers.add(5)\n\nprint(numbers)\nprint(3 in numbers)',
    "dictionaries": 'product = {"name": "Laptop", "brand": "Lenovo", "stock": 5}\nproduct["price"] = 1200\n\nprint(product["name"])\nprint(product)',
    "arrays": "from array import array\n\nnumbers = array('i', [10, 20, 30])\nnumbers.append(40)\n\nfor number in numbers:\n    print(number)",
    "remove-list-duplicates": "numbers = [1, 2, 2, 3, 4, 4, 5, 1]\nunique_numbers = []\nseen = set()\n\nfor number in numbers:\n    if number not in seen:\n        unique_numbers.append(number)\n        seen.add(number)\n\nprint(unique_numbers)",
    "functions": 'def full_name(first_name, middle_name, last_name):\n    return first_name + " " + middle_name + " " + last_name\n\nprint(full_name("Adam", "Ali", "Smith"))\n\n\ndef order_summary(product, quantity, price, tax_rate, discount):\n    subtotal = quantity * price\n    tax = subtotal * tax_rate\n    total = subtotal + tax - discount\n    return f"{product}: {total}"\n\nprint(order_summary("Book", 3, 12.5, 0.2, 5))',
    "built-in-functions": 'text = "Python"\nnumbers = [4, 10, 2, 8]\n\nprint(len(text))\nprint(sum(numbers))\nprint(sorted(numbers))',
    "user-input": 'first_number = int(input("Enter first number: "))\nsecond_number = int(input("Enter second number: "))\nprint(first_number + second_number)',
    "iterators": 'colors = ("red", "green", "blue")\ncolor_iterator = iter(colors)\n\nprint(next(color_iterator))\nprint(next(color_iterator))\nprint(next(color_iterator))',
    "oop": 'class Book:\n    def __init__(self, title, author, pages):\n        self.title = title\n        self.author = author\n        self.pages = pages\n\n    def describe(self):\n        return f"{self.title} by {self.author}, {self.pages} pages"\n\nbook = Book("Python Basics", "Adam", 150)\nprint(book.describe())',
    "classes-and-objects": 'class Phone:\n    def ring(self):\n        print("Ring ring")\n\nphone_one = Phone()\nphone_two = Phone()\n\nphone_one.ring()\nphone_two.ring()',
    "init-methods": 'class Product:\n    def __init__(self, name, category, price, stock):\n        self.name = name\n        self.category = category\n        self.price = price\n        self.stock = stock\n\nproduct = Product("Laptop", "Electronics", 1200, 5)\nprint(product.name)\nprint(product.category)\nprint(product.price)\nprint(product.stock)',
    "self-parameters": 'class Score:\n    def __init__(self):\n        self.points = 0\n\n    def add_point(self):\n        self.points += 1\n\nscore_one = Score()\nscore_two = Score()\n\nscore_one.add_point()\nscore_one.add_point()\nscore_two.add_point()\n\nprint(score_one.points)\nprint(score_two.points)',
    "class-properties": 'class Student:\n    school = "Python Academy"\n\n    def __init__(self, name):\n        self.name = name\n\nstudent_one = Student("Adam")\nstudent_two = Student("Sara")\n\nprint(student_one.name, student_one.school)\nprint(student_two.name, student_two.school)',
    "class-methods": 'class Course:\n    total_courses = 0\n\n    def __init__(self, title):\n        self.title = title\n        Course.total_courses += 1\n\n    @classmethod\n    def get_total_courses(cls):\n        return cls.total_courses\n\nCourse("Python")\nCourse("Pandas")\nprint(Course.get_total_courses())',
    "inheritance": 'class Vehicle:\n    def move(self):\n        return "The vehicle is moving"\n\nclass Car(Vehicle):\n    def move(self):\n        return "The car is driving"\n\ncar = Car()\nprint(car.move())',
    "polymorphism": 'class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n\n    def area(self):\n        return self.width * self.height\n\nclass Square:\n    def __init__(self, side):\n        self.side = side\n\n    def area(self):\n        return self.side * self.side\n\nclass Circle:\n    def __init__(self, radius):\n        self.radius = radius\n\n    def area(self):\n        return 3.14 * self.radius * self.radius\n\nshapes = [Rectangle(4, 5), Square(3), Circle(2)]\nfor shape in shapes:\n    print(shape.area())',
    "encapsulation": 'class Wallet:\n    def __init__(self, balance):\n        self.__balance = balance\n\n    def get_balance(self):\n        return self.__balance\n\n    def add_money(self, amount):\n        if amount > 0:\n            self.__balance += amount\n\nwallet = Wallet(100)\nwallet.add_money(50)\nprint(wallet.get_balance())',
    "inner-classes": 'class House:\n    class Room:\n        def __init__(self, name):\n            self.name = name\n\n        def describe(self):\n            return f"This is the {self.name}."\n\n    def __init__(self):\n        self.room = House.Room("kitchen")\n\nhouse = House()\nprint(house.room.describe())',
    "modules": 'import math\nimport random\n\nprint(math.ceil(4.2))\ncolors = ["red", "green", "blue"]\nprint(random.choice(colors))',
    "dates": "from datetime import date, timedelta\n\ntoday = date.today()\nnext_week = today + timedelta(days=7)\n\nprint(today)\nprint(next_week)",
    "math-module": "import math\n\nprint(math.pow(2, 3))\nprint(math.factorial(5))\nprint(math.pi)",
    "json": 'import json\n\nproduct = {"name": "Laptop", "price": 1200, "in_stock": True}\njson_text = json.dumps(product, indent=2)\nprint(json_text)\n\npython_data = json.loads(json_text)\nprint(python_data["name"])',
    "regex": 'import re\n\ntext = "Order numbers: 15, 29, and 103."\nprint(re.findall(r"\\d+", text))\n\nname = "Adam"\nprint(bool(re.match(r"[A-Z]", name)))',
    "random-module": 'import random\n\nprint(random.randint(1, 6))\n\nnames = ["Adam", "Sara", "Lina"]\nprint(random.choice(names))',
    "statistics-module": "import statistics\n\nnumbers = [10, 20, 30, 40, 50]\nprint(statistics.mean(numbers))\nprint(statistics.median(numbers))",
    "requests-module": 'import requests\n\nresponse = requests.get("https://api.github.com", timeout=10)\nprint(response.status_code)',
    "pip": '# Run these in the terminal, not inside normal Python code:\n# python3 -m pip list\n# python3 -m pip install requests\n\nprint("After installing, import the package in Python.")',
    "virtualenv": '# Run these in the terminal:\n# python3 -m venv .venv\n# source .venv/bin/activate\n# python3 -m pip install requests\n# deactivate\n\nprint("Virtual environment command examples are above.")',
    "try-except-error-handlers": 'try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print("You cannot divide by zero.")\n\nstudent = {"name": "Adam"}\ntry:\n    print(student["grade"])\nexcept KeyError:\n    print("The grade key does not exist.")',
    "exceptions": 'def check_age(age):\n    if age < 0:\n        raise ValueError("Age cannot be negative")\n    return age\n\ntry:\n    print(check_age(-5))\nexcept ValueError as error:\n    print("Error:", error)',
    "file-handling": 'from pathlib import Path\n\npath = Path("my_file.txt")\npath.write_text("Hello from Python", encoding="utf-8")\ncontent = path.read_text(encoding="utf-8")\nprint(content)',
    "read-files": 'from pathlib import Path\n\npath = Path("lines.txt")\npath.write_text("one\\ntwo\\nthree", encoding="utf-8")\nlines = path.read_text(encoding="utf-8").splitlines()\n\nfor line in lines:\n    print(line)\n\nprint("Line count:", len(lines))',
    "write-and-create-files": 'from pathlib import Path\n\npath = Path("todo.txt")\npath.write_text("Learn Python\\nPractice loops\\nBuild a project\\n", encoding="utf-8")\n\nwith path.open("a", encoding="utf-8") as file:\n    file.write("Review solutions\\n")\n\nprint(path.read_text(encoding="utf-8"))',
    "delete-files": 'from pathlib import Path\n\npath = Path("temporary.txt")\npath.write_text("temporary content", encoding="utf-8")\n\nif path.exists():\n    path.unlink()\n    print("Deleted temporary.txt")',
    "string-formatting": 'name = "Adam"\ncity = "Istanbul"\nprice = 19.987\n\nprint(f"{name} lives in {city}.")\nprint(f"Price: {price:.2f}")',
    "string-methods": 'text = "  Python is powerful  "\nprint(text.strip())\nprint(text.replace("powerful", "fun"))\nprint(text.strip().split())',
    "list-methods": 'numbers = [3, 1, 2]\nnumbers.append(4)\nnumbers.insert(0, 0)\nnumbers.remove(2)\nnumbers.sort()\nprint(numbers)\nnumbers.reverse()\nprint(numbers)',
    "dictionary-methods": 'student = {"name": "Adam", "age": 25}\nprint(student.get("grade", "No grade yet"))\nstudent.update({"grade": 95})\n\nfor key, value in student.items():\n    print(key, value)',
    "tuple-methods": 'values = ("red", "blue", "red", "green")\nprint(values.count("red"))\nprint(values.index("green"))',
    "set-methods": "a = {1, 2, 3}\nb = {3, 4, 5}\n\nprint(a.union(b))\nprint(a.intersection(b))",
    "file-methods": 'from pathlib import Path\n\npath = Path("file_method_solution.txt")\nwith path.open("w", encoding="utf-8") as file:\n    file.write("Line one\\nLine two\\n")\n\nwith path.open("r", encoding="utf-8") as file:\n    lines = file.readlines()\n\nprint(lines)',
    "keywords": "import keyword\n\nprint(keyword.kwlist)\nprint(keyword.iskeyword('for'))\nprint(keyword.iskeyword('adam'))",
    "glossary": 'glossary = {\n    "parameter": "a variable name in a function definition",\n    "argument": "a real value passed to a function",\n    "loop": "code that repeats",\n    "module": "a file or library you can import",\n    "exception": "an error Python can raise",\n}\n\nfor word, meaning in glossary.items():\n    print(word, "=>", meaning)',
    "built-in-modules": "import pathlib\nimport os\n\nprint(pathlib.Path.cwd())\nprint(os.getcwd())",
    "reverse-a-string": 'name = "Adam"\nprint(name[::-1])\n\n\ndef reverse_text(text):\n    return text[::-1]\n\nprint(reverse_text("Python"))',
    "add-two-numbers": 'first = float(input("Enter first number: "))\nsecond = float(input("Enter second number: "))\nprint(first + second)',
    "numpy-tutorial": "import numpy as np\n\nnumbers = np.array([1, 2, 3, 4, 5])\nprint(numbers * 10)\nprint(numbers.mean())",
    "pandas-tutorial": 'import pandas as pd\n\nproducts = pd.DataFrame({\n    "product": ["Book", "Pen", "Bag"],\n    "price": [12.5, 2.0, 35.0],\n})\n\nprint(products)\nprint(products["price"].mean())',
    "scipy-tutorial": "import numpy as np\nfrom scipy import stats\n\nnumbers = np.array([10, 20, 30, 40, 50])\nprint(stats.describe(numbers))\nprint(stats.zscore(numbers))",
    "matplotlib": "import matplotlib.pyplot as plt\n\nx = [1, 2, 3, 4]\ny = [5, 10, 7, 12]\nplt.plot(x, y)\nplt.show()",
    "pyplot": "import matplotlib.pyplot as plt\n\nplt.figure(figsize=(6, 4))\nplt.plot([1, 2, 3], [3, 6, 9])\nplt.title('My Pyplot Chart')\nplt.show()",
    "plotting": "import matplotlib.pyplot as plt\n\nmonths = ['Jan', 'Feb', 'Mar', 'Apr']\nvalues = [100, 120, 90, 150]\nplt.plot(months, values)\nplt.xlabel('Month')\nplt.ylabel('Value')\nplt.show()",
    "markers": "import matplotlib.pyplot as plt\n\nplt.plot([1, 2, 3], [10, 15, 12], marker='x', color='green')\nplt.show()\n\nplt.plot([1, 2, 3], [5, 9, 7], marker='s', color='purple')\nplt.show()",
    "line-labels": "import matplotlib.pyplot as plt\n\nplt.plot([1, 2, 3], [10, 20, 30], label='Sales')\nplt.plot([1, 2, 3], [5, 15, 25], label='Profit')\nplt.legend()\nplt.show()",
    "grid": "import matplotlib.pyplot as plt\n\nplt.plot([1, 2, 3], [10, 20, 15])\nplt.grid(axis='y')\nplt.show()",
    "subplot": "import matplotlib.pyplot as plt\n\nplt.subplot(1, 2, 1)\nplt.plot([1, 2, 3], [1, 2, 3])\nplt.title('Line 1')\n\nplt.subplot(1, 2, 2)\nplt.bar(['A', 'B', 'C'], [3, 7, 5])\nplt.title('Bars')\n\nplt.tight_layout()\nplt.show()",
    "scatter": "import matplotlib.pyplot as plt\n\nstudy_hours = [1, 2, 3, 4, 5]\nscores = [55, 60, 70, 80, 90]\nplt.scatter(study_hours, scores)\nplt.xlabel('Study Hours')\nplt.ylabel('Scores')\nplt.show()",
    "bars": "import matplotlib.pyplot as plt\n\nfoods = ['Pizza', 'Soup', 'Salad']\nvotes = [10, 5, 7]\nplt.bar(foods, votes)\nplt.title('Favorite Foods')\nplt.show()",
    "histograms": "import matplotlib.pyplot as plt\n\nscores = [55, 60, 65, 70, 75, 80, 85, 90, 95]\nplt.hist(scores, bins=4)\nplt.show()",
    "pie-charts": "import matplotlib.pyplot as plt\n\nlabels = ['Rent', 'Food', 'Transport', 'Savings']\nvalues = [40, 25, 15, 20]\nplt.pie(values, labels=labels, autopct='%1.1f%%')\nplt.show()",
    "django-tutorial": '# Run these commands in the terminal:\n# python3 -m venv .venv\n# source .venv/bin/activate\n# python3 -m pip install django\n# django-admin startproject mysite\n# cd mysite\n# python3 manage.py runserver\n\nprint("Django setup commands are listed above.")',
}


def insert_solution(path):
    slug = path.stem
    solution = SOLUTIONS.get(slug)

    if solution is None:
        raise KeyError(f"No solution found for {path}")

    notebook = json.loads(path.read_text(encoding="utf-8"))
    cells = notebook["cells"]

    cells = [
        cell
        for cell in cells
        if not (
            cell["cell_type"] == "markdown"
            and "".join(cell["source"]).strip() == "## Possible Solution"
        )
        and not (
            cell["cell_type"] == "code"
            and "".join(cell["source"]).startswith("# Possible solution")
        )
    ]

    cells.append(
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Possible Solution"],
        }
    )
    cells.append(
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ("# Possible solution\n" + solution + "\n").splitlines(keepends=True),
        }
    )

    notebook["cells"] = cells
    path.write_text(json.dumps(notebook, indent=2), encoding="utf-8")


def main():
    notebook_paths = sorted(ROOT.glob("*/*.ipynb"))

    for path in notebook_paths:
        insert_solution(path)

    print(f"Added solutions to {len(notebook_paths)} notebooks")


if __name__ == "__main__":
    main()
