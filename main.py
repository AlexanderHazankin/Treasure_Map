row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# position = [int(a) for a in str(position)]
column = int(position[1])
row = int(position[0])
map[column-1][row-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
