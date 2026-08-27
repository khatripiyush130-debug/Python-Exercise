feedback = input("Enter your feedback: ")

blocked_words = ["badword", "abuse", "spam"]

for word in blocked_words:
    feedback = feedback.replace(word, "****")

print("Moderated Feedback:")
print(feedback)