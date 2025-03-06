from datetime import datetime
current_date_and_time = datetime.now()
day = current_date_and_time.weekday()
# day = 2
subtotal = float(input("What is your subtotal? $ "))
tax = subtotal * .06

if day == 1 or day == 2 and subtotal >= 50:
    discount = subtotal * .10
    disc_tax = (subtotal - discount) *.06
    disc_total = (subtotal - discount) + disc_tax
    print(f"Discount amount: {discount:.2f}")
    print(f"Sales tax amount: {disc_tax:.2f}")
    print(f"Total: {disc_total:.2f}")
else:
    print(f"Sales tax amount: {tax:.2f}")
    print(f"Total: {subtotal + tax:.2f}")