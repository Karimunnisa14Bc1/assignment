# Burger menu
menu = {
    1: {"name": "Aloo Tikki", "price": 5},
    2: {"name": "Maharaja", "price": 10},
    3: {"name": "Mac Special", "price": 15}
}

def display_menu():
    print("****** BURGER MENU ******")
    for item_id, details in menu.items():
        print(f"{item_id}. {details['name']} - ${details['price']}")
    print("*\n")


def calculate_total():
    display_menu()
    # Changed the prompt to ask directly "What do you want to order?"
    burger_choice = input("What do you want to order? ").strip().lower()

    # Match the user's input with the available menu items (case insensitive)
    burger = None
    for item_id, details in menu.items():
        if burger_choice in details['name'].lower():
            burger = details
            break

    # Check if the burger exists in the menu
    if not burger:
        print("Sorry, we don't have that burger. Exiting.")
        return

    burger_name = burger["name"]
    burger_price = burger["price"]

    # Ask for quantity
    quantity = int(input(f"How many {burger_name}  would you like to order? "))
    total_price = burger_price * quantity

    # Student discount
    is_student = input("Are you a student? (yes/no): ").strip().lower() == "yes"
    discount = 0.2 * total_price if is_student else 0

    # Delivery charge
    delivery = input("Do you want delivery? (yes/no): ").strip().lower() == "yes"
    delivery_charge = 0.05 * total_price if delivery else 0

    # Tip
    tip_choice = input("Do you want to give a tip? Enter amount (2, 5, or 10) or 0 for none: ")
    tip = int(tip_choice) if tip_choice in ["2", "5", "10"] else 0

    # Calculate final amount
    final_total = total_price - discount + delivery_charge + tip

    # Print final bill
    print("\n****************** Final Bill **********************")
    print(f"Sr. Name        Price  Quantity  Total_Price")
    print(f"1   {burger_name}   ${burger_price}        {quantity}        ${total_price}")
    print("--------------------------------------------------")
    print(f"Subtotal                ${total_price:.2f}")
    if is_student:
        print(f"Student Discount 20%     -${discount:.2f}")
    if delivery:
        print(f"Delivery Charge 5%      +${delivery_charge:.2f}")
    if tip:
        print(f"Tip                      +${tip:.2f}")
    print("--------------------------------------------------")
    print(f"Total Bill              ${final_total:.2f}")
    print("<<<<<<<<<<<<<<<<< Thank you and come again! >>>>>>>>>>>>>>>>>>>")


# Run the billing system
calculate_total()
