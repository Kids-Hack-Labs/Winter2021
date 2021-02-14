class Item(): #Extension 2
    def __init__(self, name_, desc, cost):
        self.name = name_
        self.description = desc
        self.price = cost

class Customer(): #Extension 1
    def __init__(self, name_, funds):
        self.name = name_
        self._balance = funds
        self._inventory = {}

    def check_balance(self):
        return self._balance

    def check_inventory(self):
        return self._inventory
    
    def buy(self, item):
        self._balance -= item.price
        if item in self._inventory.keys():
            self._inventory[item] += 1
        else:
            self._inventory[item] = 1
    
class Shop():
    def __init__(self, inv, cust):
        self.inventory = inv
        
        #CHALLENGE SETUP. Notice the function names as values
        self.actions = {"leave":     self.leave,
                        "balance":   self.check_balance,
                        "check":     self.check_shop,
                        "inventory": self.check_inventory,
                        "buy":       self.sell}
        #CHALLENGE SETUP END

        self.customer = cust
        self.in_shop = True

    def check_shop(self):
        print("Here is what I have in stock:")
        for item in self.inventory.items():
            print(f"{item[0].name}. Price: ${item[0].price:.2f}. "+\
                  f"Available: {item[1]}")
            
    def check_balance(self):
        print(f"You have ${self.customer.check_balance():.2f}.")

    def check_inventory(self):
        inv = self.customer.check_inventory()
        if not inv: #Empty dictionaries evaluate to False
            print("You have no items in your inventory yet.")
            return #An alternative implementation can use an else statement
        print("This is what you have with you:")
        for item in inv.items():
            print(f"{item[0].name}: {item[1]}")

    def confirm_answer(self, item):
        answer = input(f"Do you want to add {item} to my shop "+\
                       "Y/y/N/n? ").lower()
        while answer != "y" and answer != "n":
            answer = input(f"Do you want to add {item} to my shop "+\
                           "(Y/y/N/n)? ").lower()
        return answer != "n"

    def add_item(self, item):
        desc = input(f"What's the {item}'s description? ")
        price = float(input(f"What's the {item}'s price? "))
        while price <= 0:
            price = float(input(f"What's the {item}'s price? "))
        amt = int(input(f"How many {item}s "+\
                        "do you want to add to my stock? "))
        while amt <= 0:
            amt = int(input(f"How many {item}s "+\
                            "do you want to add to my stock? "))
        temp = Item(item, desc, price)
        self.inventory[temp] = amt
        print(f"Added {amt} {item}(s) to my inventory.")

    def sell(self):
        answer = input("What do you want to buy? ").lower()
        #When items become classes, the "check for item in inventory"
        #needs to be changed as well
        item = None
        for option in self.inventory.keys():
            if answer == option.name:
                item = option
                break
        if item:
            if self.customer.check_balance() >= item.price:
                self.customer.buy(item)
                self.inventory[item] -= 1
                print(f"You bought the {answer}.")
                if self.inventory[item] < 1:
                    self.inventory.pop(item)
                    print(f"I have no {answer} left, "+\
                          "so this item is not available anymore.")
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
                           "'inventory' to check your inventory, or "+\
                           "'leave' to leave my shop: ").lower()
            #CHALLENGE EXECUTION
            if answer in self.actions.keys():
                self.actions[answer]()
            #CHALLENGE EXECUTION END
        print("bye")

def main():
    #This dictionary is part of Extension 2. It is created separately
    #and passed as the first argument to the Shop's initializer. Notice
    #how the shop now tracks the amount of items it has to sell as well.
    #This is a preparation for Week 06's homework
    shop_inventory = {Item("rusty sword","a rusty sword", 100.00):10,
                      Item("molten sand","a bucket of molten sand", 51.93):3,
                      Item("empty can","an empty can of soda", 0.75) : 30,
                      Item("inflatable rubber duck",
                           "hope you have strong lungs", 150.00):5,
                      Item("planetary ring",
                           "taken from a distant planet", 1000000.00):1}
    cust = Customer("HErC", 250.00)
    s = Shop(shop_inventory, cust)
    s.run()

if __name__ == "__main__":
    main()
