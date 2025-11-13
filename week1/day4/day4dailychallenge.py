#DC Day4 Review
#create, read, update, delete and exit (CRUDE)
#

menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):
    # """Print all drinks and prices."""
    for item, price in menu_dict.items():
        print(f"{item}: ${price:.2f}")



def add_item(menu_dict):
    # """Add a new drink to the menu."""
    item = input("Enter the name of the drink to add: ")
    if item in menu_dict:
            print(f"{item} already exists in the menu.")
    else:
        price = float(input("Enter the price with decimal: "))
        menu_dict[item] = price
        print('Item added successfully.')


def update_price(menu_dict):
    # """Change the price of an existing drink."""
    item = input("Enter the name of the drink to update: ")
    if item in menu_dict:
        new_price = float(input("Enter the new price with decimal: "))
        menu_dict[item] = new_price
        print('Price updated successfully.')
    else:
        print(f"{item} not found in the menu.")


def delete_item(menu_dict):
    # """Remove a drink from the menu."""
    item = input("Enter the name of the drink to delete: ")
    if item in menu_dict:
        del menu_dict[item]
        print('Item deleted successfully.')
    else:
        print(f"{item} not found in the menu.")


def show_options():
    # """Print the available actions."""
    options = '''What would you like to do?
    "\nCoffee Shop Menu Manager"
    1. View all items"
    2. Add a new item"
    3. Update an item's price"
    4. Delete an item"
    5. Exit'''
    print(options)    


def run_coffee_shop():
#     # """Main loop of the program."""
    while True:
      show_options()
      choice = input("What would you like to do: ")

      if choice == '1':
            show_menu(menu)
      elif choice == '2':
            add_item(menu)
      elif choice == '3':
            update_price(menu)
      elif choice == '4':
            delete_item(menu)
      elif choice == '5':
            print("Goodbye!")
            break
      else:
            print("Invalid choice, try again.")
  

# Start the program
run_coffee_shop()