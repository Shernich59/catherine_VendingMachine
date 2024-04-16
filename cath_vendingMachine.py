class VendingMachine:
    def __init__(self):
        self.vending_items = { 
            501:{"drink": "Tea", "price": 3, "quantity": 8},
            502:{"drink": "100plus", "price": 3, "quantity": 12},
            503:{"drink": "FruitJuice", "price": 5, "quantity": 10},
            504:{"drink": "Coffee", "price": 3, "quantity": 5},
            505:{"drink": "Milk", "price": 2, "quantity": 3},
            506:{"drink": "Milo", "price": 4, "quantity": 7},
        }

    def show_menu(self):
        print("Welcome to Catherine's Vending Machine")
        print("Here are some available drinks:")
        for drink_id, drink_details in self.vending_items.items():
            drink = drink_details['drink']
            price = drink_details['price']
            quantity = drink_details['quantity']
            print(f"ID: {drink_id: <5} | Drink: {drink:<12} | Price($): {price:<5} | Quantity: {quantity:<7}")

    def give_change(self, amount):
        notes = [100, 50, 20, 10, 5, 1]
        for n in notes:
            count = amount // n
            if count:
                print(f"Return {count} ${n} note(s)")
                amount -= count * n

    def purchase_drink(self, drink_id, request_quantity, amount_inserted):
        if drink_id not in self.vending_items:
            print("Sorry, this drink is not available. Please enter a valid ID!")
            return

        drink_info = self.vending_items[drink_id]
        drink_name = drink_info['drink']
        drink_price = drink_info['price']
        total_price = drink_price * request_quantity

        while amount_inserted < total_price:
            print("Insufficient funds.")
            print(f"Current amount inserted is {amount_inserted}")
            top_up = input("Would you like to top up? (y/n): ")
            if top_up.lower() == 'y':
                additional_amount = int(input("Enter additional amount ($): "))
                amount_inserted += additional_amount
            elif top_up.lower() == 'n':
                print("Transaction canceled.")
                return
            else:
                print("Invalid input! Only (y/n)! Please enter again:")

        change = amount_inserted - total_price
        self.give_change(change)
        self.vending_items[drink_id]["quantity"] -= request_quantity
        print(f"Enjoy your {request_quantity} {drink_name}!")

    def check_drink(self, drink_id, request_quantity):
        if drink_id not in self.vending_items:
            print("Sorry, this drink is not available. Please enter a valid ID!")
            return False

        item_info = self.vending_items[drink_id]
        if item_info['quantity'] >= request_quantity:
            print("This drink is available.")
            return True
        elif item_info['quantity'] == 0:
            print("This drink is currently out of stock. Please select another one.")
            return False
        else:
            print("The requested quantity exceed current stock. Please select again.")
            return False


def main():
    vending_machine = VendingMachine()

    while True:
        vending_machine.show_menu()
        user_input = input("Enter drink ID that you want to buy (or 'bye' to quit): ")
        if user_input.lower() == 'bye':
            break

        try:
            drink_id = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid drink ID.")
            continue

        user_quantity = input("Enter the quantity you want (or 'bye' to quit): ")
        if user_quantity.lower() == 'bye':
            break

        try:
            quantity = int(user_quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid positive quantity.")
            continue

        valid_drink = vending_machine.check_drink(drink_id, quantity)
        if not valid_drink:
            continue  # Prompt user to enter again

        cash = int(input("Insert your cash ($): "))
        vending_machine.purchase_drink(drink_id, quantity, cash)

if __name__ == "__main__":
    main()