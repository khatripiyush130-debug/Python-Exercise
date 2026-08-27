costs = input("Enter asset costs separated by spaces: ").split()

for i in range(len(costs)):
    costs[i] = float(costs[i])

costs.sort(reverse=True)

print("\nTop 3 priciest assets:")

for i in range(min(3, len(costs))):
    print(f"{i + 1}. {costs[i]:.2f}")