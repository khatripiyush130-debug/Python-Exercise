print("===============================")
print("       Pattern Generator       ")
print("===============================")

rows_pattern=int(input("Ente row of Pattern="))

for i in range(1,rows_pattern+1):

    for j in range(1,i+1):
        print(i, end=" ")

    print()