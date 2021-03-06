from texttable import Texttable
import pandas as pd
import numpy as np

# Tut 1

print("")
print("Tut 1")
print("")

id = [0, 1, 2, 3]
name = ["Pathum", "Johan", "Tharaka", "Rehan"]

count = 0

t = Texttable()
t.add_row(["id", "Name"])
# print("id name")
while count < len(name):
    t.add_row([id[count], name[count]])
    # print("{}".format(id[count]) + "  " + name[count])
    count = count + 1

print(t.draw())

print("")

# Tut 2

print("Tut 2")
print("")

x = [1, 2, 3, 4, 5]
data = np.array(
    [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [3, 6, 9, 12, 15],
        [4, 8, 12, 16, 20],
        [5, 10, 15, 20, 25],
    ]
)

print(pd.DataFrame(data, x, x))

print("")

# Tut 3

print("Tut 3")
print("")

x = 2
y = 3
z = 4

num = [x, y, z]
square = [pow(x, 2), pow(y, 2), pow(z, 2)]
cube = [pow(x, 3), pow(y, 3), pow(z, 3)]

count1 = 0

r = Texttable()
r.add_row(["Number", "Square", "Cube"])
while count1 < len(num):
    r.add_row([num[count1], square[count1], cube[count1]])
    count1 = count1 + 1

print(r.draw())
