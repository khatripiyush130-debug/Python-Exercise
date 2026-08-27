student_name=input("Enter Student Name=")

subject_name1=input("Enter First subject name=")  
subject_name2=input("Enter Second subject name=")  
subject_name3=input("Enter Third subject name=")  

subject_mark1=float(input("Enter marks for First Subject= "))
subject_mark2=float(input("Enter marks for Second Subject= "))
subject_mark3=float(input("Enter marks for Third Subject= "))

total_marks=(subject_mark1+subject_mark2+subject_mark3)
print("Total marks = ",total_marks)

average_marks=total_marks/3
print("average marks = ",average_marks)