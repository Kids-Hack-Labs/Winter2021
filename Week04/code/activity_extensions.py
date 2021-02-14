class Shop():
    def __init__(self):
        self.inventory = {"rusty sword":100.00,
                          "molten sand":51.93,
                          "empty can":0.75,
                          "inflatable rubber duck":150.00,
                          "planetary ring": 1000000.00}
        self.customer = {"funds": 250.00,
                         "inventory":{}}
        self.in_shop = True

    def check_shop(self):
        print("Here is what I have in stock:")
        for item in self.inventory.items():
            print(f"{item[0]}: ${item[1]:.2f}")
            
    def check_balance(self):
        print(f"You have ${self.customer['funds']:.2f}.")

    def check_inventory(self):
        if not self.customer["inventory"]:
            print("You have no items in your inventory yet.")
            return
        print("This is what you have with you:")
        for item in self.customer["inventory"].items():
            print(f"{item[0]}: {item[1]}.")

    def confirm_answer(self, item):
        answer = input(f"Do you want to add {item} to my shop "+\
                       "Y/y/N/n? ").lower()
        while answer != "y" and answer != "n":
            answer = input(f"Do you want to add {item} to my shop "+\
                           "(Y/y/N/n)? ").lower()
        return answer != "n"

    def add_item(self, item):
        price = float(input(f"What's the {item}'s price? "))
        while price <= 0:
            price = float(input(f"What's the {item}'s price? "))
        self.inventory[item] = price
        print(f"The {item} was added to my inventory with a price of {price}.")

    def update_customer(self, item, price):
        self.customer["funds"] -= price
        if item in self.customer["inventory"].keys():
            self.customer["inventory"][item] += 1
        else:
            self.customer["inventory"][item] = 1

    def sell(self):
        answer = input("What do you want to buy? ").lower()
        if answer in self.inventory.keys():
            if self.customer["funds"] >= self.inventory[answer]:
                self.update_customer(answer, self.inventory[answer])
                print(f"You bought the {answer}.")
            else:
                print(f"You don't have enough money to buy the {answer}.")
        else:
            print(f"I have no {answer} to sell...")
            if self.confirm_answer(answer):
                self.add_item(answer)
            else:
                print("okay")

    def leave(self):
        self.in_shop = False
            
    def run(self):
        print("Welcome, customer!")
        while self.in_shop:
            answer = input("Type 'balance' for balance, "+\
                           "'check' to see my items, "+\
                           "'buy' to buy something, "+\
                           "'inventory' to check your inventory, or"+\
                           "'leave' to leave my shop: ").lower()
            if answer == "leave":
                self.leave()
            elif answer == "check":
                self.check_shop()
            elif answer == "balance":
                self.check_balance()
            elif answer == "inventory":
                self.check_inventory()
            elif answer == "buy":
                self.sell()
        print("bye")

def main():
    s = Shop()
    s.run()

if __name__ == "__main__":
    main()
