def print_inventory_report(items):
    print("----- INVENTORY REPORT -----")
    # Loop through the items. We use len(items) to stay within the list.
    for i in range(len(items)):
        print(f"Item {i + 1}: {items[i]['name']} - Quantity: {items[i]['quantity']}")

def main():
    # These 5 lines must be pushed to the right (Indented)
    items = [
        {"name": "Laptop", "quantity": 15},
        {"name": "Mouse", "quantity": 30},
        {"name": "Keyboard", "quantity": 25}
    ]
    # Indented to be inside main
    print_inventory_report(items)

if _name_ == "_main_":
    # Indented to be inside the if statement
    main()