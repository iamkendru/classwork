# Question 1

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
full_name = f"{f_name} {l_name}"
print(f"Hello, {full_name}! Welcome to Python programming.")

# Question 2

user_height = float(input("Enter your height in cm: "))
user_weight = float(input("Enter your weight in kg: "))

bmi = user_weight / ((user_height / 100) ** 2)
print(f"User's BMI is: {bmi:.2f}")

# Question 3 (check if number is prime)
number = int(input("Enter a number: "))

flag = False

if number < 2:
    flag = True
else:
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            flag = True
            break
if flag:
    print(f"{number} is not a prime number.")
else:
    print(f"{number} is a prime number.")
