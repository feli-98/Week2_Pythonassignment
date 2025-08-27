def calculate_discount(price, discount_percent):
    price = float(price)
    discount_percent = float(discount_percent)

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")

    if discount_percent >= 20:
        return round(price * (1 - discount_percent / 100), 2)
    return round(price, 2)
def main():
    price = 800
    discount = 25

    if discount < 0 or discount > 100:
        print("Error: discount must be between 0 and 100")
        return
    final_price = calculate_discount(price, discount)

    if discount >= 20:
        print(f"Discounted price: ${final_price}")
    else:
        print(f"Price: ${final_price}")
if __name__ == "__main__":
    main()


