name       = input("What is your name? ")
birth_year = int(input("Enter your birth year: "))

current_year = 2025
age = current_year - birth_year

print(f"\nHello, {name}!")
print(f"You are {age} years old.")

if age < 13:
    group = "a child"
elif age < 18:
    group = "a teenager"
elif age < 60:
    group = "an adult"
else:
    group = "a senior"

print(f"You are {group}.")
print(f"In 10 years you will be {age + 10}.")