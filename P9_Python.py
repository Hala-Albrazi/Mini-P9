print("Welcome to place the rabbit!")
plants = [['🌿', '🌿', '🌿'], ['🌿', '🌿', '🌿'], ['🌿', '🌿', '🌿']]
print(f"{plants[0]}\n{plants[1]}\n{plants[2]}\n")
print("Where should the rabbit go? 🐇")
place = input("Please choose a row and a column! \n")
row = int(place[0])
column = int(place[1])
plants[row-1][column-1] = "🐇"
print("success!!!!! \n")
print(f"{plants[0]}\n{plants[1]}\n{plants[2]}\n")


# 🐇
# 🌿

