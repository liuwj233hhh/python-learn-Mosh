import converters
from utils import find_max
from ecommerce.shipping import cal_shipping
import random
from pathlib import Path


# python的编译形式与Java类似，先翻译成python字节码，再编译成机器码
# 除了Cython之外，还有Jython，将python文件先翻译成Java字节码，再编译成机器码


def greet(first_name, last_name):
    # 这里的f很重要
    print(f"Hello {first_name} {last_name}")
    print("Welcome")


def get_greeting(name):
    return f"Hi {name}"

# 增加默认值


def increment(number, by=1):
    return number + by


def mulitiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


def save_user(**user):
    print(user)


greet("Kitty", "John")
message = get_greeting("Lily")
print(message)

# 增加可读性
print(increment(2, 5))

print(mulitiply(2, 3, 4, 5))

save_user(id=1, name="John", age=22)

zeros = [0] * 5
letters = ["a", "b", "c"]

print(zeros + letters)

# list是用来切分的
numbers = list(range(20))
chars = list("Hello")
first, second, *other = numbers

print(numbers + chars)
print(numbers[::2])
print(numbers[::-1])
print(first, second)

for index, letter in enumerate(letters):
    print(index, letter)

# 增加字符
# letters.append("d")
# letters.insert(0, "-")
# letters.pop(0)
# letters.remove("b")
# letters.clear()
# print(letters)

if "d" in letters:
    print(letters.index("d"))
print(letters.count("d"))

# 排序
numbers = [0, 4, 3, 6, 10]
print(sorted(numbers))

items = [
    ("product1", 10),
    ("product2", 3),
    ("product3", 13),
]

items.sort(key=lambda item: item[1])
print(items)

# lambda表达式
filtered = list(filter(lambda item: item[1] > 10, items))
print(filtered)

prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items if item[1] >= 10]
print(prices)

# 字典
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
print(customer.get("birthdate"))

customer["birthdate"] = "Jan 1 2010"
print(customer["birthdate"])


# LEARN emoji的转换
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "🥲"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word)
    return output


print(emoji_converter("hello :)"))
print(emoji_converter("I am sad :("))


# LEARN 函数的用法
def function(name):
    print("这里是函数")
    print(f"Hi {name}")


def greet_user(first_name, last_name):
    print(f"Hi {first_name}, {last_name} !")


function("Kitty")
# keyword arg可以不顾定义的顺序，并且增加代码可读性
greet(last_name="Lau", first_name="Kitty")


def square(number):
    return number * number


print(square(3))


# LEARN 异常机制
def try_catch(Age):
    try:
        age = int(Age)
        print(age)
    except ValueError:
        print("Invalid value")


try_catch(12)
try_catch("abs")


# LEARN 定义和使用类
# 类的变量名为大驼峰
class Point:
    # 构造函数
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
print(point1.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person = Person("Kitty Lau")
person.talk()


# LEARN 继承
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def miao(self):
        print("喵~")


dog = Dog()
dog.walk()

cat = Cat()
cat.miao()

# LEARN 模块
# 替换变量快捷键 command shift D
print(converters.kg_to_lbs(100))
numbers = [2, 3, 6, 2]
print(find_max(numbers))
print(max(numbers))
cal_shipping()

# package中module的function的两种导入方法：
# 1. from package import module
# 调用：module.function
# 2. from package.module import function
# 调用：function

for i in range(3):
    print(random.randint(10, 20))

members = ['Lily', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


# Dice类的roll()方法会生成随机点的元组
class Dice:
    def roll(self):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        return (x, y)
        # return x, y
        # 默认是元组


dice = Dice()  # 括号不能丢掉
point = dice.roll()
print(point)

# python自带模块，比如pathlib
path = Path("ecommerce")
print(path.exists())

path = Path()
for file in path.glob('*.py'):
    print(file)

# 测试是否添加成功