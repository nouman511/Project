# Create a dictionary-based mini project in Python to manage an inventory in stock. The user should have options
# to add new items, buy items, change the price of items, and update the inventory of current items.
# There should also be a total sales variable that is initially set to 0. The project should handle inventory,
# price, and count. The project should be broken down into steps with clear instructions for each step.
# Each step should be pushed to GitHub.
# 1. Create a new GitHub repository and set up a new Python project.
# 2. Define the inventory dictionary to hold item data and a variable for total sales.
# 3. Create a `main` function to run the program and print a welcome message.
# 4. Create a function `add_item` to add new items to the inventory with a specified name, price, and count.
# 5. Update the `main` function to include a menu option for adding new items.
# 6. Commit the changes to GitHub.
# 7. Create a function `buy_item` to handle buying items from the inventory, updating the item count and total sales.
# 8. Update the `main` function to include a menu option for buying items.
# 9. Commit the changes to GitHub.
# 10. Create a function `change_price` to update the price of an existing item in the inventory.
# 11. Update the `main` function to include a menu option for changing item prices.
# 12. Commit the changes to GitHub.
# 13. Create a function `display_inventory` to print the current state of the inventory and total sales.
# 14. Update the `main` function to include a menu option for displaying the inventory.
# 15. Commit the changes to GitHub.
# 16. Create a function `update_inventory` to update the count of an existing item in the inventory.
# 17. Update the `main` function to include a menu option for updating the inventory count of existing items.
# 18. Commit the changes to GitHub.
# 19. Review and refactor the code if necessary. Add comments and documentation to explain the functionality.
# 20. Add a final commit to GitHub with any refinements and the completed project

total_sales=0
inventory={'Lcd':{'price':10000,'count':30},
           'SSD 250 GB':{'price':5000,'count':50},
           'Key board':{'price':2000,'count':20},
           'Battery':{'price':3500,'count':25},
           'RAM 16 GB':{'price':8000,'count':100},
           'FAN':{'price':2500,'count':10}}


def welcome_message():
    print('Welcome')

def add_item(name,price,count):
    if name in inventory:
        print("Item already exists. Use update_inventory to change count or change_price to change the price.")
    else:
        inventory[name] = {'price': price, 'count': count}
        print(f"Added {name} to inventory.")
    
def buy_item(name,count):
    global total_sales
    if name not in inventory:
        print("Item not found.")
    elif inventory[name]['count'] < count:
        print("Not enough items in stock.")
    else:
        inventory[name]['count'] -= count
        total_sales += inventory[name]['price'] * count
        print(f"Purchased {count} of {name}. Total cost: {inventory[name]['price'] * count}")

def change_price(name, new_price):
    if name not in inventory:
        print("Item not found.")
    else:
        inventory[name]['price'] = new_price
        print(f"Price of {name} updated to {new_price}.")

def update_inventory(name, new_count):
    if name not in inventory:
        print("Item not found.")
    else:
        inventory[name]['count'] = new_count
        print(f"Inventory of {name} updated to {new_count}.")

