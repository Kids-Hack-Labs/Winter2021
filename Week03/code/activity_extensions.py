"""
    Article on f-strings: https://zetcode.com/python/fstring/
    Extension 04 shows on functions at the top.
    Not all code could be encapsulated in functions at the moment
"""

def print_shop(data): #Extension 02
    for item in data.items():
        print(f"{item[0]} : {item[1]:10.2f}")

def confirm_answer(item):
    answer = input(f"Do you want to add {item} to my shop "+\
                   "(Y/y/N/n)? ").lower()
    while answer != "y" and answer != "n":
        answer = input(f"Do you want to add {item} to my shop "+\
                       "(Y/y/N/n)? ").lower()
    return answer != "n"

def check_customer(customer): #nested dictionary example
    print("You have:")
    for item in customer["items"].items():
        print(f"{item[1]} {item[0]}(s)") 
    
def main():
    shop = {"rusty sword":100.00,
            "molten sand":51.93,
            "empty can":0.75,
            "inflatable rubber duck":150.00,
            "planetary ring": 1000000.00}
    customer = {"funds": 250.00, "items":{}} #Extension 01
    in_shop = True
    print("Welcome!")
    print_shop(shop)
        
    while in_shop:
        answer = input("Type 'balance' for balance, "+\
                       "'inventory' for your inventory, "+\
                       "'check' to see my items, "+\
                       "'buy' to buy something, or "+\
                       "'leave' to leave my shop: ").lower()
        if answer == "leave":
            in_shop = False
        elif answer == "check":
            print("Sure, here it is:")
            print_shop(shop)
        elif answer == "balance":
            print(f"You have {customer['funds']:.2f}.")
        elif answer == "inventory":
            check_customer(customer)
        elif answer == "buy":
            answer = input("What do you want to buy? ").lower()
            if answer in shop.keys():
                if customer["funds"] >= shop[answer]:
                    print(f"You've bought the {answer}.")
                    customer["funds"] -= shop[answer]
                    if answer in customer["items"]:
                        customer["items"][answer] += 1
                    else:
                        customer["items"][answer] = 1
                else:
                    print(f"You don't have enough money to buy the {answer}.")
            else:
                print(f"I have no {answer} to sell")
                #extension 03
                if confirm_answer(answer):
                    shop[answer] = float(input(f"What is the price of {answer}? "))
                else:
                    print("okay")
    print("bye")

if __name__ == "__main__":
    main()
