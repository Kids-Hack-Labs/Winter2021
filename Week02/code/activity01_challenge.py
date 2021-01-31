def rewrite_message(first, last, day, month, year):
    return f"{first} {last} was born in {month} {day}, {year}"

def main():
    first_name = "John"
    last_name = "Doe"
    day = 27 #int
    month = "September"
    year = 2016
    
    message = f"{first_name} {last_name} was born in {month} {day}, {year}."
    print(message)
    running = True #flag
    
    while running: #repeats code
        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")
        day = int(input("What day were you born in? "))
        month = input("What month were you born in? ")
        year = int(input("What year were you born in? "))
        
        message = rewrite_message(first_name, last_name, day, month, year)
        print(message)

        #Console programming practice: use (Y/y/N/n) to prompt user to
        #tell user of Yes/No answers, shortened to "y" and "n"
        answer = input("Do you want to continue (Y/y/N/n)? ").lower()
        while answer != 'y' and answer != 'n':
            answer = input("Do you want to continue (Y/y/N/n)? ").lower()

        running = answer != "n" #turns "running" to False if answer is "no"
    print("bye")

if __name__ == "__main__":
    main()
