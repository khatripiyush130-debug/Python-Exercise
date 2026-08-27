print("========== Order-Tracking System ==========")

status=input("Enter order status(shipped,delivered,pending) = ").lower().strip()

if status=="Shipped".lower():
    message=("Your order has been shipped and is on its way to you.")
    
elif  status=="Pending".lower():
    message=("Your order is confirmed and is currently being prepared.")

elif status=="Delivered".lower():
    message=("Your order has been successfully delivered. Thank you for shopping with us!")
    
else:
    message=("Invalid status. Please enter pending, shipped, or delivered")

print("\n========== Tracking Update ==========")
print(message)
