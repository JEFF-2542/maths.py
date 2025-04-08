# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    # If the discount is 20% or higher, apply the discount
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)  # Calculate discount
        final_price = price - discount_amount  # Apply discount to price
        return final_price
    else:
        return price  # No discount applied

# Prompt the user for the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Print the final price
if final_price != price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The price is: ${price:.2f}")
