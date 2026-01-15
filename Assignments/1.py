# 1. Program that takes a single string as its input and sort its characters from the lowest Unicode value to the highest Unicode value.

user_input = input("")
sort = sorted(user_input)
result = "".join(sort)
print(result)

# 2.

a = int(input(""))
b = int(input(""))

sum = a+b
diff = a-b
product = a*b
div = a/b
rem = a%b
power = a**b

print(f"{a} + {b} is {sum}")
print(f"{a} - {b} is {diff}")
print(f"{a} * {b} is {product}")
print(f"{a} / {b} is {div}")
print(f"{a} % {b} is {rem}")
print(f"{a} ^ {b} is {power}")

# 3. Program that prints a dictionary where the keys are numbers between 1 and N, and the values are square of keys.

key = int(input(""))
dictionary = {}
for i in range(1, key+1):
    sq = i * i
    dictionary[i] =sq

print(dictionary)

# 4. Program that takes a positive integer, n, as input and then displays the sum of all of the integers from 1 to n. The sum of the first n positive integers can be computed using the formula: sum = n * (n+1)/2

n = int(input(""))
sum = n*(n+1)/2
print(f"The sum of the first {num} positive integers is {sum}")

# 5. Program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

s = input().lower()
count = 0

vowels = 'aeiou'

for chr in s:
    if chr in vowels:
        count += 1
print(f"Number of vowels: {count}")

# 6. Program that sums all of the numbers taken as input, while ignoring any input that is not a valid number.

sum = 0

while True:
    num = input()
    try:
        num = int(num)
        if num == 0:
            print(f"The grand total is {float(sum)}")
            break
        else:
            sum += num
            print(f"The total is now {float(sum)}")
    except ValueError:
        print(f"That wasn’t a number.")

# 7. Write a function called "custom_encoder" that accepts a string text as parameter and for each char of the text it calculates its 0-based position.

from operator import indexOf

def custom_encoder(str):
    result = []
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    for char in str.lower():
        if char in reference_string:
            result.append(indexOf(reference_string, char))
        else:
            result.append(-1)

    return result

# 8. Write a class Person that has a member function hello()

class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, my name is {self.name}")


# 9. Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")


# 10. Make a class called `User`. Create the following attributes: first_name and last_name, email, and location. Make a method called describe_user() that prints a summary of the user's information. Make another method called greet_user() that prints a personalized greeting to the user.

class User:
    def __init__(self, first_name, last_name,username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}\n"
                f"Username: {self.username}\n"
                f"Email: {self.email}\n"
                f"Location: {self.location}")
    
    def greet_user(self):
        print(f"Welcome back {self.username}!")