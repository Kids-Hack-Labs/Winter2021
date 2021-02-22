"""
    NOTE: Extension added using a simple add() method and a
    matching option for the customer. The user cannot set
    negative prices

    NOTE 2: Extension also included a remove() method so that
    the user can further customize their shop.

    NOTE 3: The student should come up with their own JSON
    containing the shop's inventory
"""
import json

class Shop():
    def __init__(self, inv):
        self.inventory = inv
        self.customer = 250.00
        self.in_shop = True

    def check_shop(self):
        print("Here is what I have in stock:")
        for item in self.inventory.items():
            print(f"{item[0]}: ${item[1]:.2f}")
            
    def check_balance(self):
        print(f"You have ${self.customer:.2f}.")

    def sell(self):
        answer = input("What do you want to buy? ").lower()
        if answer in self.inventory.keys():
            if self.customer >= self.inventory[answer]:
                print(f"You bought the {answer}.")
                self.customer -= self.inventory[answer]
            else:
                print(f"You don't have enough money to buy the {answer}.")
        else:
            print(f"I have no {answer} to sell...")

    def add(self):
        answer = input("What do you want to add to my stock? ").lower()
        while answer in self.inventory.keys():
            print(f"I already sell {answer}. You should add new stuff.")
            answer = input("What do you want to add to my stock? ").lower()
        price = float(input(f"And what is {answer}'s price? "))
        while price <= 0:
            print("I don't think I can put that price up...")
            price = float(input(f"And what is {answer}'s price? "))
        self.inventory[answer] = round(price, 2)

    def remove(self):
        answer = input("What item do you want to remove from my inventory? ").lower()
        if answer not in self.inventory.keys():
            print(f"I have no {answer} to sell...")
            return
        self.inventory.pop(answer)
        print(f"Done. I don't sell {answer} anymore.")
        
    def leave(self):
        self.in_shop = False
            
    def run(self):
        print("Welcome, customer!")
        while self.in_shop:
            answer = input("Type 'balance' for balance, "+\
                           "'check' to see my items, "+\
                           "'buy' to buy something, "+\
                           "'add' to add items to my stock,"+\
                           "'remove' to remove an item from my stock, or "+\
                           "'leave' to leave my shop: ").lower()
            if answer == "leave":
                self.leave()
            elif answer == "check":
                self.check_shop()
            elif answer == "balance":
                self.check_balance()
            elif answer == "buy":
                self.sell()
            elif answer == "add":
                self.add()
            elif answer == "remove":
                self.remove()
                
        with open("inventory.json", "w") as inv_file:
            #indent and separators write a "pretty-printed" json file
            json.dump(self.inventory, inv_file,
                      indent=4, separators=(", ",": "))
        print("bye")

def main():
    with open("inventory.json", "r") as inventory:
        inv_dict = json.load(inventory)
        s = Shop(inv_dict)
    s.run()

if __name__ == "__main__":
    main()
