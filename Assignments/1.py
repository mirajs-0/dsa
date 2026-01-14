# # Program that takes a single string as its input and sort its characters from the lowest Unicode value to the highest Unicode value.

user_input = input("")
sort = sorted(user_input)
result = "".join(sort)
print(result)

# # 2

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

# # Program that prints a dictionary where the keys are numbers between 1 and N, and the values are square of keys.

key = int(input(""))
dictionary = {}
for i in range(1, key+1):
    sq = i * i
    dictionary[i] =sq

print(dictionary)