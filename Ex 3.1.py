age=int(input("Enter Student Age = "))
income=int(input("Enter Family Income = "))

if age>=18 and age<=25:  
    if income<=300000:
        print("It is elible for Scholarship.")
    else:
        print("It is not eligible for Scholarship.")
else:
    print("It is not eligible for Scholarship.")