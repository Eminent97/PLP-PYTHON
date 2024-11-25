def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent/100)
        return final_price
    else:
        return price

price = int(input("Enter a price: "))
discount_percentage = int(input("Enter your discount percentage"))

final_price = calculate_discount(price, discount_percentage)

if discount_percentage >= 20:
    print(f"The final price after applying discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${price:.2f}")



