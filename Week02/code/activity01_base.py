def rewrite_message(first, last, day, month, year):
    return f"{first} {last} was born in {month} {day}, {year}."

first_name = "John"
last_name = "Doe"
day = 27 #int
month = "September"
year = 2016

message = rewrite_message(first_name, last_name, day, month, year)
print(message)

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
day = int(input("What day were you born in? "))
month = input("What month were you born in? ")
year = int(input("What year were you born in? "))

print(message)

message = rewrite_message(first_name, last_name, day, month, year)
print(message)
