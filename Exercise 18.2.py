FILENAME = "Student.txt"
print("=" * 40)
print("         LOG VIEWER")
print("=" * 40)
try:
    file = open(FILENAME, "r")
    count = 0
    print("\nLog File Contents:")
    print("-" * 40)
    line = file.readline()
    while line:
        print(line, end="")
        count += 1
        line = file.readline()
    file.close()
    print("\n" + "-" * 40)
    print("Total number of lines:", count)
except FileNotFoundError:
    print("Log file does not exist.")
except OSError:
    print("Error reading the log file.")