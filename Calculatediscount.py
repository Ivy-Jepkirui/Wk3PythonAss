def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    Only applies the discount if discount_percent is 20% or higher.
    Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied! Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price: {price:.2f}")

if __name__ == "__main__":
    main()
