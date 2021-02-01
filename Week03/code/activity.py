"""
    Article on f-strings: https://zetcode.com/python/fstring/
"""

def print_shop(data):
    for item in data.items():
        print(f"{item[0]} : {item[1]:.2f}")
    
def main():
    shop = {"rusty sword":100.00,
            "molten sand":51.93,
            "empty can":0.75,
            "inflatable rubber duck":150.00,
            "planetary ring": 1000000.00}
    customer = 250.00
    in_shop = True
    print("Welcome!")
    print_shop(shop)
        
    while in_shop:
        answer = input("Type 'balance' for balance, "+\
                       "'check' to see my items, "+\
                       "'buy' to buy something, or "+\
                       "'leave' to leave my shop: ").lower()
        if answer == "leave":
            in_shop = False
        elif answer == "check":
            print("Sure, here it is:")
            print_shop(shop)
        elif answer == "balance":
            #in an f-string, the expression name can be
            #followed by :.nf, where n is the number of
            #decimal digits to be displayed
            print(f"You have {customer:.2f}.")
        elif answer == "buy":
            answer = input("What do you want to buy? ").lower()
            if answer in shop.keys():
                if customer >= shop[answer]:
                    print(f"You've bought the {answer}.")
                    customer -= shop[answer]
                else:
                    print(f"You don't have enough money to buy the {answer}.")
            else:
                print(f"I have no {answer} to sell...")
    print("bye")

if __name__ == "__main__":
    main()
