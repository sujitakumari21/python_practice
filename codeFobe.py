#PRODUCT PRICE CALCULATOR
original_price = float(input("Enter originalprice:"))
discount_percent = float(input("Enter Discount % :"))
discount_amount = discount_percent/100*original_price
final_price = original_price-discount_amount
print(f"Final price after {discount_percent}% discount:{final_price}")
