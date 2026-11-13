import sys
import tkinter as tk

MENU = {
    "Pizza": 150,
    "Momos": 60,
    "Burger": 80,
    "Sandwich": 120,
    "Coffee": 50,
    "Cold Coffee": 80,
}


def print_menu():
    print("~Welcome to The Rotash Restaurant")
    print("~Here is the menu")
    for item, price in MENU.items():
        print(f"{item}: ₹{price}")
    print()


def collect_order():
    items = []
    total = 0

    while True:
        try:
            order = input("~What would you like to order sir/ma'am? (type 'done' to finish): ").strip().title()
        except EOFError:
            print("\nNo input detected. Using a sample order.")
            return ["Pizza", "Coffee"], 200

        if not order:
            continue

        if order.lower() == "done":
            break

        if order in MENU:
            items.append(order)
            total += MENU[order]
            print(f"{order} added. Current total: ₹{total}")
        else:
            print("Item isn't available here!!")

        try:
            again = input("Do you want to order anything else sir/ma'am? (yes/no): ").strip().lower()
        except EOFError:
            break

        if again not in {"yes", "y"}:
            break

    return items, total


def build_bill(items, total):
    lines = ["~Welcome to The Rotash Restaurant", "Your bill:"]
    if not items:
        lines.append("No items ordered.")
    else:
        for item in items:
            lines.append(f"{item}: ₹{MENU[item]}")
    lines.append(f"Total: ₹{total}")
    return "\n".join(lines)


def show_bill_window(bill_text):
    root = tk.Tk()
    root.geometry("420x420")
    root.title("Harsh Tiwari")
    root.config(background="skyblue", border=2)

    label = tk.Label(
        root,
        text="Your bill",
        bg="skyblue",
        fg="white",
        font=("Arial", 30, "bold"),
        relief="groove",
        border=10,
    )
    label.pack(padx=10, pady=10)

    bill = tk.StringVar(value=bill_text)
    bill_label = tk.Label(
        root,
        textvariable=bill,
        bg="white",
        fg="black",
        font=("Arial", 18, "bold"),
        border=10,
        justify="left",
    )
    bill_label.pack(padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    print_menu()

    if sys.stdin is not None and not sys.stdin.isatty():
        ordered_items = ["Pizza", "Coffee"]
        total = sum(MENU[item] for item in ordered_items)
        bill_text = build_bill(ordered_items, total)
        print(bill_text)
    else:
        ordered_items, total = collect_order()
        bill_text = build_bill(ordered_items, total)
        print("\n" + bill_text)
        try:
            show_bill_window(bill_text)
        except tk.TclError:
            pass

