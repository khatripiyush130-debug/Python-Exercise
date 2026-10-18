FILENAME = "diary.txt"
print("=" * 40)
print("       PERSONAL DIARY")
print("=" * 40)
while True:
    thought = input("Enter your thoughts (or type 'exit' to stop): ")
    if thought.lower() == "exit":
        print("Your diary entries have been saved.")
        break
    if thought.strip():
        try:
            file = open(FILENAME, "a")
            file.write(thought + "\n\n")
            file.close()
            print("Diary entry saved successfully!")
        except OSError:
            print("Error saving diary entry.")
    else:
        print("Thought cannot be empty.")