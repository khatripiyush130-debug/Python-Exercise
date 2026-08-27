print("-------student details-------")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 17 and age <= 25:
    print("It is eligible")
else:
    print("It is not eligible")

mark = int(input("Enter your mark: "))

if mark >= 90:
    print("Allow seat in AIML", mark)
elif mark >= 80:
    print("Allow seat in CSE", mark)
elif mark >= 60:
    print("Allow seat in General", mark)
else:
    print("Not eligible for a seat", mark)
    