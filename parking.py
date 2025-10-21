print("===Parking Garage Calculator===")
total=0
while True:
    day_type=input("Enter day type: weekday,weekend, or holiday:")
    if day_type== "done":
        break
    if day_type=="weekday":
        price=8.00
    elif day_type=="weekend":
        price=6.00
    elif day_type== "holiday":
        price=5.00
    else:
        print("Invalid word")
    total+=price
    print(f"Price: ${price:.2f}")
    print(f"Current total: ${total:.2f}")
special_offer=0.0
if total>=50.00:
    special_offer=7.00
final_total=total-special_offer
print(f"===Parking Summary===")
print(f"Subtotal: ${total:.2f}")
print(f"Frequent Parker Discount: -${special_offer}")
print(f"Final Total: ${final_total:.2f}")
print(f"Thank you for parking with us !")