def rewrite_message(info):
    #notice that the order is not necessarily the same as the list
    return f"{info[0]} {info[1]} was born in {info[3]} {info[2]},{info[4]}."

def main():
    data = ["John", "Doe", 27, "September", 2006]
    
    message = rewrite_message(data)
    print(message)
    running = True #flag
    
    while running: #repeats code
        data[0] = input("What is your first name? ")
        data[1] = input("What is your last name? ")
        data[2] = int(input("What day were you born in? "))
        data[3] = input("What month were you born in? ")
        data[4] = int(input("What year were you born in? "))

        #data can be appended directly into the list.
        #It is good practice to validate it first, though
        data.append(input("What is your favourite colour? "))
        
        message = rewrite_message(data)
        print(message)

        print("Data printed in for loop:")
        for i in range(len(data)):
            print(f"data[{i}]: {data[i]}")
            
        #Notice that the rest of the program doesn't change
        #Console programming practice: use (Y/y/N/n) to prompt user to
        #tell user of Yes/No answers, shortened to "y" and "n"
        answer = input("Do you want to continue (Y/y/N/n)? ").lower()
        while answer != 'y' and answer != 'n':
            answer = input("Do you want to continue (Y/y/N/n)? ").lower()

        running = answer != "n" #turns "running" to False if answer is "no"
    print("bye")

if __name__ == "__main__":
    main()
