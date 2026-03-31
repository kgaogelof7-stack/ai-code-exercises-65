def format_currency(value: float) -> str:
    """Helper to add '$' and commas to any number."""
    return f"${value:,.2f}"

def calculate_discount(price: float, discount_rate: float) -> float:
    """Helper to calculate any discount amount."""
    return price * discount_rate

def apply_tax(price: float, tax_rate: float = 0.08) -> float:
    """Helper to calculate the tax on a price."""
    return price * tax_rate

def generate_full_report(sales_items: list):
    """Main function that replaces 200+ lines of messy code."""
    grand_total = 0
    total_tax = 0
    total_discounts = 0

    print("========== COMPLETE SALES REPORT ==========")
    
    for item in sales_items:
        price = item.get('price', 0)
        # Apply a 10% discount if the item is over $1000
        discount = calculate_discount(price, 0.10) if price > 1000 else 0
        tax = apply_tax(price - discount)
        
        final_price = price - discount + tax
        grand_total += final_price
        total_tax += tax
        total_discounts += discount

        print(f"Product: {item['name']:<15} | Final: {format_currency(final_price)}")

    print("-" * 43)
    print(f"TOTAL DISCOUNTS: {format_currency(total_discounts)}")
    print(f"TOTAL TAX:       {format_currency(total_tax)}")
    print(f"GRAND TOTAL:     {format_currency(grand_total)}")
    print("===========================================")

if _name_ == "_main_":
    # Test data representing a complex sales list
    data = [
        {"name": "Laptop", "price": 1200.00},
        {"name": "Mouse", "price": 25.50},
        {"name": "Monitor", "price": 450.00},
        {"name": "Keyboard", "price": 85.00}
    ]
    generate_full_report(data)