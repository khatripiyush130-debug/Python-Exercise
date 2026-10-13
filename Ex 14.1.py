products = ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile",
            "Laptop", "Tablet", "Mobile", "Laptop"]
votes = {
    "Laptop": 0,
    "Mobile": 0,
    "Tablet": 0
}
for product in products:
    if product in votes:
        votes[product] += 1
    else:
        votes[product] = 1
print("----- SURVEY RESULTS -----")
for product in votes:
    print(product, ":", votes[product], "votes")
winner = max(votes, key=votes.get)
print("\nWinner:", winner)
print("Votes:", votes[winner])
