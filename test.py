from texttable import Texttable
import pandas as pd
import numpy as np

# Tut 1

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

x = [1, 2, 3, 4, 5]
data = np.array(
    [
        [1, 2, 1, 1, 3],
        [2, 3, 1, 2, 2],
        [3, 4, 5, 6, 7],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
    ]
)

print(pd.DataFrame(data, x, x))
