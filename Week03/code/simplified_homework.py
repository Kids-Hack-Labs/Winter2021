def supply(inventory):
    item = input("Sure, what do you want to add to my stock? ").lower()
    if item in inventory.keys():
        print(f"Sorry, {item} is already in my stock.")
    else:
        price = float(input(f"What is {item}'s price? "))
        inventory[item] = price

def retrieve(inventory):
    item = input("Sure, what do you want to retrieve from my stock? ").lower()
    if item not in inventory.keys():
        print(f"Sorry, {item} is currently not in my stock.")
    else:
        print(f"Okay, I'll remove {item} from my inventory.")
        inventory.pop(item)

def check(inventory):
    print("This is a list of what I currently have:")
    for item in inventory.items():
        print(f"{item[0]}: {item[1]}")

def main():
    shop = {"rusty sword":100.00,
            "molten sand":51.93,
            "empty can":0.75,
            "inflatable rubber duck":150.00,
            "planetary ring": 1000000.00}

    supplying = True

    print("Welcome, supplier!")

    while supplying:
        answer = input("What do you want to do today? (supply, retrieve, "+\
                       "check, leave): ").lower()
        if answer == "supply":
            supply(shop)
        elif answer == "retrieve":
            retrieve(shop)
        elif answer == "check":
            check(shop)
        elif answer == "leave":
            supplying = False

    print("Thanks for stopping by, supplier!")

if __name__ == "__main__":
    main()
