print("*"*40)
print("    Movie Theatre Booking Simulator    ")
print("*"*40)

total_rows=int(input("Enter number of rows in the theatre: "))
total_columns=int(input("Enter number of column in the theatre: "))

theatre_layout=[]
for r in range(total_rows):
    rows=[]
    for c in range(total_columns):
        rows.append("O")
    theatre_layout.append(rows)

print(f"\n Theatre layout created: {total_rows}rows * {total_columns}columns.")
print("All seats are currently Open (O).\n")

while True:
    print("*"*40)
    print("1. Display Theatre Layout.")
    print("2. Reserve a Seat.")
    print("3. Cancel a Reservation.")
    print("4. Count Available / Reserved seats.")
    print("5. Check a specific Seat Status.")
    print("6. Exit.")
    print("*"*40)
    
    choice=(input("Enter your choice(1-6): ")).strip()
    
    if choice=="1":
        print("\n Current Theatre Layout:")
        print("(rows top to buttom = rows 1 to rows ",total_rows,")\n")
        for r in range(len(theatre_layout)):
            print(f"Rows {r+1}: ",end=" ")
            for c in range(len(theatre_layout[r])):
                print(theatre_layout[r][c],end=" ")
            print()
        print()
        
    elif choice=="2":
        row_num=int(input(f"Enter row number (a to {total_rows}): "))-1
        col_num=int(input(f"Enter Seat number (a to {total_columns}): "))-1
        
        if 0<= row_num<total_rows and 0<= col_num<total_columns:
            if theatre_layout[row_num]=="X":
                print("This Seat is Reserved.\n")
            else:
                theatre_layout[row_num][col_num]="X"
                print(f"Seat at Row{row_num+1},Seat{col_num+1} reserved successfully.")
        else:
            print("Invalid row or seat number.\n")
            
    elif choice=="3":
        row_num=int(input(f"Enter row number (a to {total_rows}): "))-1
        col_num=int(input(f"Enter Seat number (a to {total_columns}): "))-1
        
        if 0<= row_num<total_rows and 0<= col_num<total_columns:

            if theatre_layout[row_num]=="O":
              print("This Seat is Open.\n")
            else:
                theatre_layout[row_num][col_num]="O"
                print(f"Reservation cancelled for row{row_num+1},Seat{col_num+1}.")
        else:
            print("Invalid row or seat number.\n")
        
        
    elif choice=="4":
        row_num=int(input(f"Enter row number (a to {total_rows}): "))-1
        col_num=int(input(f"Enter Seat number (a to {total_columns}): "))-1
            
        if 0<= row_num<total_rows and 0<= col_num<total_columns:
            status=theatre_layout[row_num][col_num]
    
            if status=="O":
                print(f"Seat Row {row_num+1},Seat{col_num+1} is Open.\n")
            else:
                print(f"Seat Row {row_num+1},Seat{col_num+1} is Reserved.\n")
        else:
                print("Invalid row or seat number.\n")
                
                
    elif choice=="5":
        open_count=0
        reserved_count=0
        for r in range(len(theatre_layout)):
            for c in range(len(theatre_layout[r])):
                if theatre_layout[r][c]=="O":
                    open_count=open_count+1
                else:
                    reserved_count=reserved_count+1
        
        print(f"Total Seats: {total_rows*total_columns}")
        print(f"Open Seats : {open_count}")
        print(f"Reserved Seats: {reserved_count}\n")
        
        
    elif choice=="6":
        print("Existing program.Thank you.")
        break
    else:
        print("Invalid choice.Please enter a number between 1 to 6.\n")