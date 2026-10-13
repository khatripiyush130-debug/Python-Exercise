inventory = {
    "Pen": 50,
    "Notebook": 30,
    "Pencil": 20
}
item = input("Enter item sold: ")
if item in inventory:
    qty = int(input("Enter quantity sold: "))
    inventory[item] -= qty
    print("Remaining stock:", inventory[item])
    if inventory[item] == 0:
        print("Warning: Stock is zero!")
else:
    print("Item not found.")
