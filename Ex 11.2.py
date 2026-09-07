print("*"*60)
print("              CLASS SCHEDULE LAYOUT SYSTEM                ")
print("*"*60)

total_rows = int(input("Enter number of time slots: "))
total_columns = 6

days = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday"]

time_slots = []

for r in range(total_rows):
    time = input(f"Enter time slot {r+1}: ")
    time_slots.append(time)

schedule = []

for r in range(total_rows):
    rows = []
    for c in range(total_columns):
        rows.append("---")
    schedule.append(rows)

print(f"\nClass schedule created: {total_rows} time slots * 6 days.")
print("All subjects are currently empty (---).\n")


while True:
    print("*"*60)
    print("1. Display Class Schedule.")
    print("2. Add / Overwrite Subject Topic.")
    print("3. Clear a Subject Topic.")
    print("4. Count Empty / Filled Slots.")
    print("5. Check a Specific Class Status.")
    print("6. Exit.")
    print("*"*60)
    
    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        print("\nCurrent Class Schedule:")
        print("-"*100)
        print(f"{'Time':<15}", end="")
        for day in days:
            print(f"{day:<14}", end="")
        print()
        print("-"*100)
        for r in range(len(schedule)):
            print(f"{time_slots[r]:<15}", end="")
            for c in range(len(schedule[r])):
                print(f"{schedule[r][c]:<14}", end="")
            print()
        print()

    elif choice == "2":
        print("\nAvailable Days:")
        for i in range(len(days)):
            print(f"{i+1}. {days[i]}")
        day_num = int(input("Enter day number (1-6): ")) - 1
        time_num = int(input(
            f"Enter time slot number (1-{total_rows}): "
        )) - 1
        if (0 <= day_num < total_columns and 0 <= time_num < total_rows):
            print(f"Current subject:{schedule[time_num][day_num]}")
            subject = input("Enter new subject/topic: ").strip()
            schedule[time_num][day_num] = subject
            print("Subject added/overwritten successfully.\n")
        else:
            print("Invalid day or time slot number.\n")

    elif choice == "3":
        print("\nAvailable Days:")
        for i in range(len(days)):
            print(f"{i+1}. {days[i]}")
        day_num = int(input("Enter day number (1-6): ")) - 1
        time_num = int(input(f"Enter time slot number (1-{total_rows}): ")) - 1
        if (0 <= day_num < total_columns and 0 <= time_num < total_rows):
            if schedule[time_num][day_num] == "---":
                print("This class slot is already empty.\n")
            else:
                schedule[time_num][day_num] = "---"
                print("Subject cleared successfully.\n")
        else:
            print("Invalid day or time slot number.\n")

    elif choice == "4":
        empty_count = 0
        filled_count = 0
        for r in range(len(schedule)):
            for c in range(len(schedule[r])):
                if schedule[r][c] == "---":
                    empty_count = empty_count + 1
                else:
                    filled_count = filled_count + 1

        print(f"\nTotal Class Slots: {total_rows * total_columns}")
        print(f"Empty Slots       : {empty_count}")
        print(f"Filled Slots      : {filled_count}\n")

    elif choice == "5":
        print("\nAvailable Days:")
        for i in range(len(days)):
            print(f"{i+1}. {days[i]}")
        day_num = int(input("Enter day number (1-6): ")) - 1
        time_num = int(input(f"Enter time slot number (1-{total_rows}): ")) - 1

        if (0 <= day_num < total_columns and 0 <= time_num < total_rows):
            status = schedule[time_num][day_num]
            if status == "---":
                print(f"Class on {days[day_num]},{time_slots[time_num]} is EMPTY.\n")
            else:
                print(f"Class on {days[day_num]},{time_slots[time_num]}: {status}\n")
        else:
            print("Invalid day or time slot number.\n")

    elif choice == "6":
        print("Exiting program. Thank you.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 to 6.\n")