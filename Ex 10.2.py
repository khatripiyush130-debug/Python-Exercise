# Inventory Catalog Manager

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]

item = input("Enter the product name to search: ")

for i in range(len(products)):
    if products[i].lower() == item.lower():
        print("Item found!")
        print("Product:", products[i])
        print("Index:", i)
        found = True
        break

if not found:
    print("Item not found in inventory.")