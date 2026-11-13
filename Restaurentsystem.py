menu = {
    "Pizza": 150,
    "Momos": 60,
    "Burger": 80,
    "Sandwich": 120,
    "Coffee": 50,
    "Cold Coffee": 80,
}

print("~Welcome to The Rotash Restaurant")
print("~Here is the menu")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

order_items = []
total = 0

while True:
    order = input("\nWhat do you want to order sir/ma'am? ").strip().title()

    if order in menu:
        order_items.append(order)
        total += menu[order]
        print(f"{order} added. Current total: ₹{total}")
    else:
        print("Item isn't available here!!")

    again = input("Do you want to order anything else? (yes/no): ").strip().lower()
    if again not in ["yes", "y"]:
        break

print("\nYour bill:")
for item in order_items:
    print(f"{item}: ₹{menu[item]}")
print(f"Total: ₹{total}")
print("Thanks for visiting our restaurant!")
