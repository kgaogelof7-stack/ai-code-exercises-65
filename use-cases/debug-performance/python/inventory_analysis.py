def find_product_combinations(products, target_price, price_margin=10):
    """
    Finds all pairs of products where the combined price is within
    the target_price ± price_margin range.
    """
    results = []
    
    # OPTIMIZATION: 
    # 1. Start 'j' from 'i + 1' to avoid comparing a product with itself 
    # 2. This prevents duplicate pairs like (A, B) and (B, A)
    # 3. We removed the slow 'any()' check to make it run faster
    
    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            product1 = products[i]
            product2 = products[j]
            
            combined_price = product1['price'] + product2['price']
            
            # Check if the combined price is within the target range
            if (target_price - price_margin) <= combined_price <= (target_price + price_margin):
                results.append({
                    "products": (product1, product2),
                    "combined_price": combined_price
                })
                
    return results

if _name_ == "_main_":
    # Test data to verify the fix
    sample_products = [
        {"id": 1, "name": "Laptop", "price": 1000},
        {"id": 2, "name": "Mouse", "price": 50},
        {"id": 3, "name": "Monitor", "price": 300},
        {"id": 4, "name": "Keyboard", "price": 100}
    ]
    print(find_product_combinations(sample_products, 1100, 50))