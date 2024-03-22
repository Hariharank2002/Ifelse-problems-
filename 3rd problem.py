price = int(input("Enter the price:"))

if price > 1000:
    remining_price = price - 1000
    remining_discount = remining_price * (0.05)
    print("discount price is: ", remining_discount + 100)
elif price == 1000:
    print("discount price is: ", price * (0.10))


