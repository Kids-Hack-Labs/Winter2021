def supply(inventory):
    item = input("Sure, what do you want to add to my stock? ").lower()
    if item in inventory.keys():
        amt = int(input(f"How many {item}s do you want"+
                        "to add to my stock? "))
        while amt < 1:
            amt = int(input(f"How many {item}s do you want "+
                            "to add to my stock? "))
        inventory[item][2] += amt
    else:
        desc = input(f"What is {item}'s description? ").lower()
        price = float(input(f"What is {item}'s price? "))
        amt = int(input(f"How many {item}s do you want "+
                        "to add to my stock? "))
        inventory[item] = [desc,price,amt]

def retrieve(inventory):
    item = input("Sure, what do you want to retrieve from my stock? ").lower()
    if item not in inventory.keys():
        print(f"Sorry, {item} is currently not in my stock.")
    else:
        amt = int(input(f"How many {item}s do you want "+
                        "to remove from my inventory? "))
        while amt < 1:
            amt = int(input(f"How many {item}s do you want "+
                            "to remove from my inventory? "))
        if inventory[item][2] <= amt:
            print(f"I only have {inventory[item][2]} of those. I'm returning"+
                  "all of them to you.")
        inventory[item][2] -= amt
        if inventory[item][2] <= 0:
            inventory.pop(item)
            print(f"I have no {item}s left. I removed it from my inventory.")
        else:
            print(f"I have {inventory[item][2]} {item}s left.")
def check(inventory):
    print("This is a list of what I currently have:")
    for item in inventory.items():
        print(f"{item[0]}: {item[1][0]}. ${item[1][1]:.2f},"+
              f"available: {item[1][2]}")

def main():
    shop = {"rusty sword": ["a rusted sword", 100.00, 10],
            "molten sand": ["a bucket of molten sand",51.93, 3],
            "empty can": ["an empty can of soda", 0.75, 20],
            "inflatable rubber duck": ["hope you have strong lungs", 150.00, 5],
            "planetary ring": ["taken from a distant planet", 1000000.00, 1]}

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
