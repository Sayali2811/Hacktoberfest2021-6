#top half
rows = int(input("Enter the number of rows:" ))
k = 0
for i in range(1, rows + 1):
  # print spacesfor j in range (1, (rows - i) + 1):
    print(end = " ")

    # let's print starswhile k != (2 * i - 1):
    print("*", end = "")
    k = k + 1
  k = 0# add a line break
  print()

#bottom half
k = 2
m = 1
for i in range(1, rows):
  # print spacesfor j in range (1, k):
    print(end = " ")
  k = k + 1# print starwhile m <= (2 * (rows - i) - 1):
    print("*", end = "")
    m = m + 1
  m = 1#add a line break
  print()