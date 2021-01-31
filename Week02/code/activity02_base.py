def rewrite_message(info):
    #notice that the order is not necessarily the same as the list
    return f"{info[0]} {info[1]} was born in {info[3]} {info[2]},{info[4]}."

def main():
    #If line 7 is used instead of line 10, the program crashes:
    #data = ("John", "Doe", 27, "September", 2006)

    #This data can be changed
    data = ["John", "Doe", 27, "September", 2006]
    
    message = rewrite_message(data)
    print(message)

    data[0] = input("What is your first name? ")
    data[1] = input("What is your last name? ")
    data[2] = int(input("What day were you born in? "))
    data[3] = input("What month were you born in? ")
    data[4] = int(input("What year were you born in? "))

    #adding data to list
    extra_data = input("What is your favourite colour? ")
    data.append(extra_data)

    #notice how rewrite_message() ignores extra indices, but
    #it needs at least 5 elements in the list to work properly
    message = rewrite_message(data)
    print(message)
    
    print("Data printed in for loop:")
    for i in range(len(data)):
        print(f"data[{i}]: {data[i]}")

if __name__ == "__main__":
    main()
