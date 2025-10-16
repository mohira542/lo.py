# Collect: Item name, price, and quantity for 3 electronics items
# Get customer information: Name, is_member (yes/no), total_previous_purchases (in sum)

item_1_name = 'laptop'
item_1_price = 11000000
item_1_quantity = 3

item_2_name = 'electric kettle'
item_2_price = 250000
item_2_quantity =5

item_3_name= 'television'
item_3_price= 2000000
item_3_quantity=2

customer_name="Mohira"
is_member="yes"
total_previous_purchase = 5000000
print("\n---------CUSTOMER INFORMATION---------- ")
print(f"Customer:{customer_name}")
print(f"membership:{is_member}")
print(f"total pervious purchase: {total_previous_purchase}")
print(f"{" "*50}\n")
print("---------List of all 3 purchase---------")#print(f"Names of all 3 items: {item_1_name} , {item_2_name} , {item_3_name} ")

subtotal = item_1_price * item_1_quantity + item_2_price *item_2_quantity + item_3_price *item_3_quantity
#Discount Rules: Calculate eligiblility and amounts for each  discount type:
#Member discount: 10% off subtotal (eligible if customer is a member)
#Bulk discount: 5% off ( eligible if total items > 5)
 #Loyalty discount: 3% off (eligible if total_previous_purchases>= 420)
#All discounts stack - apply  them sequentially using boolean arithmetic
 
member_discount_eligibiliity = is_member == "yes"
member_discount_amount = member_discount_eligibiliity * subtotal * 0.1

subtotal_after_member_discount = subtotal - member_discount_amount

total_quantity = item_1_quantity + item_2_quantity + item_3_quantity

bluk_discount_eligible = total_quantity > 5
bluk_discount = bluk_discount_eligible * subtotal_after_member_discount * 0.05

subtotal_after_bulk_discount = subtotal_after_member_discount - bluk_discount

loyalty_discount_eligible = total_previous_purchase>= 1000000
loyalty_discount_amount = loyalty_discount_eligible * subtotal_after_bulk_discount * 0.03

subtotal_after_loyalty_discount = subtotal_after_bulk_discount - loyalty_discount_amount


shipping_eligible = subtotal > 5

tax_rate = subtotal * 0.12

# subtract tax rate from subtotal after discounts
shipping = (subtotal <= 500000) * 25000
subtotal_after_discount = subtotal - tax_rate
print(f'item_1_name : {item_1_name}')
print(f'item_1_price: {item_1_price}')
print(f'item_1_quantity: {item_1_quantity}')
print(f'item_2_name: {item_2_name}')
print(f'item_2_price: {item_2_price}')
print(f'item_2_quantity:{item_2_quantity}')
print(f'item_3_name:{item_3_name}')
print(f'item_3_price:{item_2_price}')
print(f'item_3_quantity:{item_3_quantity}') 
print(f'member_discount_eligibility:{member_discount_eligibiliity}')
print(f'member_discount_amount:{member_discount_amount}')
print(f'subtotal_after_member_discount:{subtotal_after_discount}')
print(f'total_quantity:{total_quantity}')
print(f'bluk_discount_eligible:{bluk_discount_eligible}')
print(f'bluk discount:{bluk_discount}')
print(f'subtotal_after_bluk_discount:{subtotal_after_bulk_discount}')
print(f'loyalty_discount_eligible:{loyalty_discount_eligible}')
print(f'loyalty_discount_amount:{loyalty_discount_amount}')

      