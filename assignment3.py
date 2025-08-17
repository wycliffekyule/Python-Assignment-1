def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount if it's 20% or higher.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage to be applied
    
    Returns:
    float: Final price after discount if applicable, otherwise original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
