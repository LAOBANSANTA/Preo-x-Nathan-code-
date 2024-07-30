from tkinter import *

window = Tk()
window.geometry("1000x1000")
window.title("Preo's Shopping Cart")

# final one

# Initialize the main data
category = {
    "Drinks": {
        # item ID: ItemDetails--------------------------------------------------
        "N32": {'name': "Neo's Green Tea", 'price': 3.00, 'quantity': 0},
        "M13": {'name': "Melo Chocolate Malt Drink", 'price': 2.85, 'quantity': 0},
        "V76": {'name': "Very-Fair Full Cream Milk", 'price': 3.50, 'quantity': 0},
        "N14": {'name': "Nirigold UHT Milk", 'price': 4.15, 'quantity': 0},
    },
    "Beers": {
        "L11": {"name": "Lion (24x320ml)", "price": 52.00, "quantity": 0},
        "P21": {"name": "Panda(24x230ml)", "price": 78.00, "quantity": 0},
        "A54": {"name": "Axe(24x320ml)", "price": 58.00, "quantity": 0},
        "H91": {"name": "Henekan(24x320ml)", "price": 68.00, "quantity": 0},
    },
    "Frozen": {
        "E11": {"name": "Edker Ristorante Pizza 355g", "price": 6.95, "quantity": 0},
        "F43": {"name": "Fazzler Frozen Soup 500g", "price": 5.15, "quantity": 0},
        "CP31": {"name": "CP Frozen Ready Meal 250g", "price": 4.12, "quantity": 0},
        "D72": {"name": "Duitoni Cheese 270g", "price": 5.60, "quantity": 0},
    },
    "Household": {
        "FP76": {"name": "FP Facial Tissues", "price": 9.50, "quantity": 0},
        "FP32": {"name": "FP Premium Kitchen Towel", "price": 5.85, "quantity": 0},
        "K22": {"name": "Klinex Toilet Tissue Rolls", "price": 7.50, "quantity": 0},
        "D14": {"name": "Danny Softener", "price": 9.85, "quantity": 0},
    },
    "Snacks": {
        "SS93": {"name": "Singshort Seaweed", "price": 3.10, "quantity": 0},
        "MC14": {"name": "Mei Crab Cracker", "price": 2.05, "quantity": 0},
        "R35": {"name": "Reo Pokemon Cookie", "price": 4.80, "quantity": 0},
        "HS11": {"name": "Huat Seng Crackers", "price": 3.55, "quantity": 0}
    }
}

# Dictionary to hold quantity for each item
quantityHolder = {}



# The total price calculator
def total_price_calculator(categoryDic, categoryName):
    # Initialise total price equal 0
    totalPrice = 0
    for itemID, itemDetails in categoryDic[categoryName].items():
        # Calculating total price by using the item Price x Quantity
        totalPrice += itemDetails['price'] * itemDetails['quantity']
    return totalPrice

# updating the total price label
def update_total_price_label(categoryDic, categoryName, total_price_label):
    # passing the argument of category dic and categoryName into the calculator
    total_price = total_price_calculator(categoryDic, categoryName)
    # initialising the total price label
    total_price_label.config(text=f"Total Price for {categoryName}: ${total_price:.2f}")

# Decrement item quantity
def decrement_item_quantity(categoryDic, categoryName, itemID, total_price_labels_dic):
    itemDetails = categoryDic[categoryName][itemID]
    # if the quantity is less than 0 than run the code
    if itemDetails['quantity'] > 0:
        # decrease by one
        itemDetails['quantity'] -= 1
        # Update the label displaying the item's quantity
        update_quantity_label(itemID, itemDetails['quantity'])
        # Update the total price label for the specified category
        update_total_price_label(categoryDic, categoryName, total_price_labels_dic[categoryName])

# increment item quantity
def increment_item_quantity(categoryDic, categoryName, itemID, total_price_labels_dic):
    itemDetails = categoryDic[categoryName][itemID]
    # Increase by one
    itemDetails['quantity'] += 1
    # Update the label displaying the item's quantity
    update_quantity_label(itemID, itemDetails['quantity'])

    # Update the total price label for the specified category
    update_total_price_label(categoryDic, categoryName, total_price_labels_dic[categoryName])

# update quantity label
def update_quantity_label(itemID, quantity):
    # if the itemID is in the quantity holder than run the code below
    if itemID in quantityHolder:
        # configure text onto the screen
        quantityHolder[itemID].config(text=f"Quantity: {quantity}")


# clearing window function
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# Displaying items in the different categories
def display_category_items(categoryName):
    clear_window()
    # Declare that we are using the global variable 'row'
    global row
    # local variable row
    row = 0
    # Dic for the total price labels
    total_price_labels_dic = {}

    # creating the category label
    category_label = Label(window, text=categoryName, font=("Arial", 14, "bold"))
    # sticky "ew" fills the space of the grid cell from the left(w) to the right (e): It occupies the full width of the cell
    category_label.grid(row=row, column=0, columnspan=4, pady=10, sticky='ew')
    row += 1

    # Iterating through each item in the specified category
    for itemID, itemDetails in category[categoryName].items():
        # Getting the name
        itemName = itemDetails['name']
        # Getting the price
        itemPrice = itemDetails['price']
        # Getting the quantity
        itemQuantity = itemDetails['quantity']

        # Create an item label for the item displaying its name and price
        item_label = Label(window, text=f"{itemName} - Price: ${itemPrice:.2f}", font=("Arial", 12))
        # Placing the item in the grid at current row and column 0
        item_label.grid(row=row, column=0, padx=5)

        # Create a quantity label
        quantity_label = Label(window, text=f"Quantity: {itemQuantity}", font=("Arial", 12))
        # This quantity label will be right beside the item label
        quantity_label.grid(row=row, column=1, padx=5)
        # updating the quantityholder dic with the quantity label, using the item ID as the key
        quantityHolder[itemID] = quantity_label

        button_minus = Button(
            window,
            text="-",
            # Use a lambda function to capture the current values of categoryName and itemID
            # c=categoryName i=itemID allows you to current values of category name and itemID to the decrement item quantity function
            # If you dont do this the items will update incorrectly
            command=lambda c=categoryName, i=itemID: decrement_item_quantity(category, c, i, total_price_labels_dic),
            font=("Arial", 12),
            fg="yellow",
            bg="black",
            activeforeground="#00FF00",
            activebackground="black",
        )
        button_minus.grid(row=row, column=2, padx=5)

        plus_button = Button(
            window,
            text="+",
            command=lambda c=categoryName, i=itemID: increment_item_quantity(category, c, i, total_price_labels_dic),
            font=("Arial", 12),
            fg="yellow",
            bg="black",
            activeforeground="#00FF00",
            activebackground="black",
        )
        plus_button.grid(row=row, column=3, padx=5)

        row += 1

    # Creating the total price label GUI
    total_price_label = Label(window, text=f"Total Price for {categoryName}: $0.00", font=("Arial", 12, "italic"), fg="blue")
    total_price_label.grid(row=row, column=0, columnspan=4, pady=5)
    total_price_labels_dic[categoryName] = total_price_label

    # Update the total price label for the specified category
    # total_price_labels_dic[categoryName]: The label widget that displays the total price for the specified category
    update_total_price_label(category, categoryName, total_price_labels_dic[categoryName])

    row += 1
    # Making the back button GUI
    back_button = Button(window, text="Back to Menu", command=main_menu, font=("Arial", 12))
    back_button.grid(row=row, column=0, columnspan=4, pady=10)

    # Check out button to check out in their respective category
    checkout_button = Button(window, text="Shopping Cart", command=lambda: display_shoppingcart(categoryName), font=("Arial", 12))
    checkout_button.place(x=900, y=100)


# Declare global variables
total_price = 0
GST_price = 0
# initialising the total price to have the value of none
total_price_label = None
# setting it such that there is no discount at the start
discount_applied = False
# No discount percentage
discount_percentage = 0


def display_shoppingcart(categoryName):
    # Clear the window of any previous widgets
    clear_window()

    # Declare global variables so they can be modified within this function
    global row, total_price_label
    row = 0

    # Create and display a label for the checkout section
    category_label = Label(window, text="Checkout", font=("Arial", 14, "bold"))
    category_label.grid(row=row, column=0, columnspan=4, pady=10, sticky='ew')
    row += 1

    # Initialize total price for all items in the cart
    total_price = 0
    # Local dictionary to manage quantity labels for items on this page
    quantity_labels = {}

    # Loop through each category and its items in the shopping cart
    for cat, items in category.items():
        for itemID, itemDetails in items.items():
            # Only display items with a quantity greater than 0
            if itemDetails['quantity'] > 0:
                # Retrieve item details
                itemName = itemDetails['name']
                itemPrice = itemDetails['price']
                itemQuantity = itemDetails['quantity']
                # Calculate total price for this item
                item_total = itemPrice * itemQuantity
                # Add to the overall total price
                total_price += item_total

                # Create and display a label for the item
                item_label = Label(window, text=f"{itemName} - Quantity: {itemQuantity} - Total: ${item_total:.2f}",
                                   font=("Arial", 12))
                item_label.grid(row=row, column=0, padx=5, sticky='w')

                # Create and display a label for the item quantity
                quantity_label = Label(window, text=f"Quantity: {itemQuantity}", font=("Arial", 12))
                quantity_label.grid(row=row, column=1, padx=5)

                # Store the quantity label in the dictionary for later updates
                quantity_labels[itemID] = quantity_label

                # Create and display a button to decrease the item quantity
                button_minus = Button(
                    window,
                    text="-",
                    command=lambda i=itemID: update_item_quantity(i, -1, quantity_labels),
                    font=("Arial", 12),
                    fg="yellow",
                    bg="black",
                    activeforeground="#00FF00",
                    activebackground="black",
                )
                button_minus.grid(row=row, column=2, padx=5)

                # Create and display a button to increase the item quantity
                plus_button = Button(
                    window,
                    text="+",
                    command=lambda i=itemID: update_item_quantity(i, 1, quantity_labels),
                    font=("Arial", 12),
                    fg="yellow",
                    bg="black",
                    activeforeground="#00FF00",
                    activebackground="black",
                )
                plus_button.grid(row=row, column=3, padx=5)

                # Move to the next row for the next item
                row += 1

    # total price label gui
    total_price_label = Label(window, text=f"Total Price: ${total_price:.2f}\n", font=("Arial", 12, "italic"), fg="blue")
    total_price_label.grid(row=row, column=0, columnspan=4, pady=10)
    row += 1

    # back button gui
    back_button = Button(window, text="Back to Menu", command=main_menu, font=("Arial", 12))
    back_button.grid(row=row, column=0, columnspan=4, pady=10)

    checkout_button = Button(window, text="Proceed to Checkout", command=lambda: display_checkout(categoryName), font=("Arial", 12))
    checkout_button.place(x=900, y=10)

    # Add the discount button and make them GLOBAL
    global ten_percent_discount_button,eight_percent_discount_button,five_percent_discount_button

    # Olk folks
    ten_percent_discount_button = Button(window, text="Old Folks 10% Discount", command=lambda: apply_discount(10), font=("Arial", 12))
    ten_percent_discount_button.place(x=900, y=90)
    # members
    eight_percent_discount_button = Button(window, text="Members 8% Discount", command=lambda: apply_discount(8), font=("Arial", 12))
    eight_percent_discount_button.place(x=900, y=150)
    # Ns men
    five_percent_discount_button = Button(window, text="NS Men 5% Discount", command=lambda: apply_discount(5), font=("Arial", 12))
    five_percent_discount_button.place(x=900, y=210)

    # Reapply the discount state if a discount has already been applied
    if discount_applied:
        discount_label = Label(window, text=f"{discount_percentage}% Discount Applied!", font=("Arial", 12, "bold"),fg="green")
        discount_label.place(x=900, y=50)
        # Disable the buttons
        ten_percent_discount_button.config(state=DISABLED)
        eight_percent_discount_button.config(state=DISABLED)
        five_percent_discount_button.config(state=DISABLED)


# making the apply discount function
def apply_discount(discount):
    global discount_applied, discount_percentage

    # Making it such that the if block will only run if no discount has been applied
    if not discount_applied:
        # Change the status of discount applied to TRUE
        discount_applied = True
        discount_percentage = discount

        # Indicate that the discount has been applied by displaying a label
        discount_label = Label(window, text=f"{discount_percentage}% Discount Applied!", font=("Arial", 12, "bold"),fg="green")
        discount_label.place(x=900, y=50)

        # Disable all discount buttons
        ten_percent_discount_button.config(state=DISABLED)
        eight_percent_discount_button.config(state=DISABLED)
        five_percent_discount_button.config(state=DISABLED)

# Updating item quantity
def update_item_quantity(itemID, change, quantity_labels):
    # Ensure we're using the global variable
    global total_price, total_price_label
    # Iterate through each category and its items
    for cat, items in category.items():
        # Check if the itemID exists in the current category's items
        if itemID in items:
            # Getting the item details
            itemDetails = items[itemID]
            # Changing the quantity
            new_quantity = itemDetails['quantity'] + change
            # Ensure quantity doesn't go below 0
            if new_quantity >= 0:
                # updating the item Quantity
                itemDetails['quantity'] = new_quantity
                # Update the quantity label in the GUI
                quantity_labels[itemID].config(text=f"Quantity: {new_quantity}")

                # Recalculate total price
                total_price = 0
                for items in category.values():
                    for item in items.values():
                        if item['quantity'] > 0:
                            total_price += item['price'] * item['quantity']

                # Update the total price label
                total_price_label.config(text=f"Total Price: ${total_price:.2f}")

def display_checkout(categoryName):
    # Declare global variables to ensure the function can modify them
    global row, total_price, GST_price, discount_applied, discount_percentage
    clear_window()
    row = 0

    # Configure the columns for the grid layout
    window.grid_columnconfigure(0, weight=1)

    # Making the category label GUI and centering it
    category_label = Label(window, text="Checkout", font=("Arial", 20, "bold"))
    category_label.grid(row=row, column=0, columnspan=4, pady=10, sticky='ew')
    row += 1

    # Initialize the total price
    total_price = 0
    # Iterate over all categories and their items to calculate the total price
    for cat, items in category.items():
        for itemID, itemDetails in items.items():
            # Only consider items with a quantity greater than 0
            if itemDetails['quantity'] > 0:
                itemName = itemDetails['name']
                itemPrice = itemDetails['price']
                itemQuantity = itemDetails['quantity']
                item_total = itemPrice * itemQuantity
                total_price += item_total

                # Create a label for each item
                item_label = Label(window, text=f"{itemName} : Quantity: {itemQuantity} : Total: ${item_total:.2f}",
                                   font=("Arial", 12))
                item_label.grid(row=row, column=0, columnspan=4, padx=5, sticky='ew')

                row += 1

    GST_price = (9 / 100) * total_price

    # Apply discount if applicable
    if discount_applied:
        discount_amount = (discount_percentage / 100) * total_price
        discounted_price = total_price - discount_amount + GST_price

        total_price_label = Label(window, text=f"Total Price of the items: ${total_price:.2f}\n"
                                                f"GST amount (9%): ${GST_price:.2f}\n"
                                                f"Discount ({discount_percentage}%): ${discount_amount:.2f}\n"
                                                f"Final payable amount: ${discounted_price:.2f}",
                                  font=("Arial", 12, "italic"), fg="blue")
    else:
        total_price_label = Label(window, text=f"GST amount (9%): ${GST_price:.2f}\n"
                                               f"Total Price of the items: ${total_price:.2f}\n"
                                               f"Total Price including GST: ${GST_price + total_price:.2f}",
                                  font=("Arial", 12, "italic"), fg="blue")

    # Center the total price label in the window
    total_price_label.grid(row=row, column=0, columnspan=4, pady=10, sticky='ew')
    row += 1

    # Goodbye message
    Goodbye_label = Label(window, text="Thank you so much for using Preo's Shopping Cart! \n"
                                       "We hope to see you again as you will get to see PREO being A freaaakyyyy time traveller!",
                          font=("Arial", 12))
    Goodbye_label.grid(row=row, column=0, columnspan=4, pady=10, sticky='ew')

def main_menu():
    clear_window()
    # This is to help me ensure that the label is always pushed to the top and fill the window.
    top_frame = Frame(window, bg="Tan")
    top_frame.pack(side=TOP, fill=X)

    menu_label = Label(top_frame, text="Main Menu", font=("Arial", 16, "bold"), fg="white", bg="black")
    menu_label.pack()

    # All the buttons to bring it to the specific category.
    drinks_button = Button(window, text="Drinks", command=lambda: display_category_items("Drinks"), font=("Arial", 14))
    drinks_button.place(x=200, y=100)

    beers_button = Button(window, text="Beers", command=lambda: display_category_items("Beers"), font=("Arial", 14))
    beers_button.place(x=200, y=450)

    frozen_button = Button(window, text="Frozen", command=lambda: display_category_items("Frozen"), font=("Arial", 14))
    frozen_button.place(x=700, y=350)

    household_button = Button(window, text="Household", command=lambda: display_category_items("Household"), font=("Arial", 14))
    household_button.place(x=1200, y=100)

    snacks_button = Button(window, text="Snacks", command=lambda: display_category_items("Snacks"), font=("Arial", 14))
    snacks_button.place(x=1200, y=450)

    # Check_out button directly from the main menu for them to check what items they currently have.
    # Could even be to directly checkout for if they want to from the main menu for whatever reason.
    checkout_button = Button(window, text="Shopping Cart", command=lambda: display_shoppingcart(None), font=("Arial", 14))
    checkout_button.place(x=1380, y=50)

    # Labels of items right under the category.
    drinks_label = Label(window,
                         text="N32: [Neo's Green Tea - $3] \n"
                              "M13: [Melo Chocolate Malt Drink - $2.85] \n"
                              "V76: [Very-Fair Full Cream Milk - $3.50]\n"
                              "N14: [Nirigold UHT Milk - $4.15]]\n",
                         font=("Arial", 10, "bold"), fg="Black", bg="lavender", bd=5, padx=10, pady=10)
    drinks_label.place(x=100, y=150)

    beer_label = Label(window,
                       text="L11: [Lion (24x320ml) - $52] \n"
                            "P21: [Panda(24x230ml) - $78] \n"
                            "A54: [Axe(24x320ml) - $58]  \n"
                            "H91: [Henekan(24x320ml) - $68]\n",
                       font=("Arial", 10, "bold"), fg="Black", bg="lavender", bd=5, padx=10, pady=10)
    beer_label.place(x=125, y=500)

    frozen_label = Label(window,
                         text="E11: [Edker Ristorante Pizza 355g - $6.95] \n"
                              "F43: [Fazzler Frozen Soup 500g - $5.15] \n"
                              "CP31: [CP Frozen Ready Meal 250g - $4.12]\n"
                              "D72: [Duitoni Cheese 270g - $5.60]\n",
                         font=("Arial", 10, "bold"), fg="Black", bg="lavender", bd=5, padx=10, pady=10)
    frozen_label.place(x=590, y=400)

    household_label = Label(window,
                            text="FP76: [FP Facial Tissues  - $9.50] \n"
                                 "FP32: [FP Premium Kitchen Towel - $5.85] \n"
                                 "K22: [Klinex Toilet Tissue Rolls - $7.50]\n"
                                 "D14: [Danny Softener  - $9.85]\n",
                            font=("Arial", 10, "bold"), fg="Black", bg="lavender", bd=5, padx=10, pady=10)
    household_label.place(x=1100, y=150)

    snacks_label = Label(window,
                         text="SS93: [Singshort Seaweed  - $3.10] \n"
                              "MC14: [Mei Crab Cracker - $2.05 ] \n"
                              "R35: [Reo Pokemon Cookie - $4.80]\n"
                              "HS11: [Huat Seng Crackers  - $3.55 ]\n",
                         font=("Arial", 10, "bold"), fg="Black", bg="lavender", bd=5, padx=10, pady=10)
    snacks_label.place(x=1115, y=500)

def start_menu():
    start_button = Button(window,
                          text="Welcome to Preo's shopping cart!\n"
                               "Click to proceed",
                          font=("Arial", 12),
                          command=main_menu)
    start_button.pack(expand=True)

# Initialize the main menu
start_menu()

# Run the Tkinter event loop
window.mainloop()
