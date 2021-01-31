def output_sign(name, month, day, sign):
    return f"{name} was born in {month} {day}, so they're a(n) {sign}."

def main():
    months = ("January","February","March","April","May","June","July",
              "August","September","October","November","December")
    dates = (21, 20, 19, 20, 21, 22, 22, 22, 22, 22, 21, 22)
    signs = ("Aquarius","Pisces","Aries","Taurus","Gemini","Cancer","Leo",
             "Virgo","Libra","Scorpio","Sagittarius","Capricorn")

    name = input("What is your name? ")
    month = input("What month were you born in? ")
    day = int(input("What day were you born in? "))

    sign = ""
    i = months.index(month)
    if day < dates[i]:
        #This code works even if i is zero: negative indices loop from the
        #end of the sequence type
        sign = signs[i-1] 
    else:
        sign = signs[i]

    message = output_sign(name, month, day, sign)
    print(message)

if __name__ == "__main__":
    main()
