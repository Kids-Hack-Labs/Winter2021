"""
    Notice that this code is more modular, as it uses functions to
    format output, calculate signs, and even confirm if the user wants
    to keep running the program.

    Note: The get_index_ functions are basically two versions of the
    same algorithm. One uses ternary if statements, which uses the
    "value_if_true if condition else value_if_false" pattern, and the
    other takes advantage of the fact that Booleans are integer types
    and applies it in a multiplication instead of branching the code.
"""
def output_sign(name, month, day, sign):
    return f"{name} was born in {month} {day}, so they're a(n) {sign}."

def get_index_ternary(day, change_date, index):
    return index if day >= change_date[index] else index-1

def get_index_branchless(day, change_date, index):
    return index -1*(day < change_date[index])

def confirm_answer():
        answer = input("Do you want to check someone else's sign "+
                       "(Y/y/N/n)? ").lower()
        while answer != 'y' and answer != 'n':
            answer = input("Do you want to check someone else's sign "+
                           "(Y/y/N/n)? ").lower()
        return answer != "n"

def main():
    months = ("January","February","March","April","May","June","July",
              "August","September","October","November","December")
    dates = (21, 20, 19, 20, 21, 22, 22, 22, 22, 22, 21, 22)
    zodiac_signs = ("Aquarius","Pisces","Aries","Taurus","Gemini","Cancer",
                    "Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn")
    running = True

    while running:
        name = input("What is your name? ")
        month = input("What month were you born in? ")
        day = int(input("What day were you born in? "))

        #The two lines below produce the same result. It is enough to
        #use a single one
        i = get_index_ternary(day, dates, months.index(month))
        #i = get_index_branchless(day, dates, months.index(month))
        sign = zodiac_signs[i]
    
        print(output_sign(name, month, day, sign))

        running = confirm_answer()
    print("bye") 

if __name__ == "__main__":
    main()
