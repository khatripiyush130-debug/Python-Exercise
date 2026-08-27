print("===============================")
print("       Pattern Generator       ")
print("===============================")

frame_rows=int(input("Enter the Hight(rows)="))
frame_col=int(input("Enter the width(column)="))

for i in range(frame_rows):

    for j in range(frame_col):

        if i==0 or i==frame_rows-1 or j==0 or j==frame_col-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()