def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
print("Temperature Conversion")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter your choice: "))
temp = float(input("Enter temperature: "))
if choice == 1:
    print("Fahrenheit:", celsius_to_fahrenheit(temp))
elif choice == 2:
    print("Celsius:", fahrenheit_to_celsius(temp))
else:
    print("Invalid choice")
