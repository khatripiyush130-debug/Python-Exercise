students = {
    101: "shreyajadh17@gmail.com",
    102: "sanikakoda@gmail.com",
    103: "1387surajjadhav@gmail.com"
}
roll = int(input("Enter student roll number: "))
if roll in students:
    print("Email:", students[roll])
else:
    print("Student not found.")
