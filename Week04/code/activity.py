class Shop():
    def __init__(self):
        self.inventory = {"rusty sword":100.00,
                          "molten sand":51.93,
                          "empty can":0.75,
                          "inflatable rubber duck":150.00,
                          "planetary ring": 1000000.00}
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

    def leave(self):
        self.in_shop = False
            
    def run(self):
        print("Welcome, customer!")
        while self.in_shop:
            answer = input("Type 'balance' for balance, "+\
                           "'check' to see my items, "+\
                           "'buy' to buy something, or "+\
                           "'leave' to leave my shop: ").lower()
            if answer == "leave":
                self.leave()
            elif answer == "check":
                self.check_shop()
            elif answer == "balance":
                self.check_balance()
            elif answer == "buy":
                self.sell()
        print("bye")

def main():
    s = Shop()
    s.run()

if __name__ == "__main__":
    main()
