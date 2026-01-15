# # # Program that takes a single string as its input and sort its characters from the lowest Unicode value to the highest Unicode value.

# user_input = input("")
# sort = sorted(user_input)
# result = "".join(sort)
# print(result)

# # # 2

# a = int(input(""))
# b = int(input(""))

# sum = a+b
# diff = a-b
# product = a*b
# div = a/b
# rem = a%b
# power = a**b

# print(f"{a} + {b} is {sum}")
# print(f"{a} - {b} is {diff}")
# print(f"{a} * {b} is {product}")
# print(f"{a} / {b} is {div}")
# print(f"{a} % {b} is {rem}")
# print(f"{a} ^ {b} is {power}")

# # # Program that prints a dictionary where the keys are numbers between 1 and N, and the values are square of keys.

# key = int(input(""))
# dictionary = {}
# for i in range(1, key+1):
#     sq = i * i
#     dictionary[i] =sq

# print(dictionary)

# # # program that takes a positive integer, n, as input and then displays the sum of all of the integers from 1 to n. The sum of the first n positive integers can be computed using the formula: sum = n * (n+1)/2

n = int(input(""))
sum = n*(n+1)/2
print(f"The sum of the first {num} positive integers is {sum}")

# Program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

s = input().lower()
count = 0

vowels = 'aeiou'

for chr in s:
    if chr in vowels:
        count += 1
print(f"Number of vowels: {count}")

# Program that sums all of the numbers taken as input, while ignoring any input that is not a valid number.

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

# Write a function called "custom_encoder" that accepts a string text as parameter and for each char of the text it calculates its 0-based position.

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
