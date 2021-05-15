# Tut-Ses #

Just to teach some basic python code techniques taught at IIT.

## Overview of [test.py](https://github.com/Pathum312/Tut-Ses/blob/master/test.py) ##

### \# Tut 1 ### 

Teaches how to take values from a list them display them in a table using the `TextTable` libarary.

```
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
```

#### Output of Tut 1 ####

```
+----+---------+
| id | Name    |
+----+---------+
| 0  | Pathum  |
+----+---------+
| 1  | Johan   |
+----+---------+
| 2  | Tharaka |
+----+---------+
| 3  | Rehan   |
+----+---------+
```

### \# Tut 2 ### 

Teaches how to acces values from multiple lists and display them in an datafram fashion using the `Pandas` library.

```
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
```

#### Output of Tut 2 ####

```
   1   2   3   4   5
1  1   2   3   4   5
2  2   4   6   8  10
3  3   6   9  12  15
4  4   8  12  16  20
5  5  10  15  20  25
```

### \# Tut 3 ###

Same thing as the first tut but teaches how to use the `pow()` function.

```
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
```

#### Output of Tut 3 ####

```
+--------+--------+------+
| Number | Square | Cube |
+--------+--------+------+
| 2      | 4      | 8    |
+--------+--------+------+
| 3      | 9      | 27   |
+--------+--------+------+
| 4      | 16     | 64   |
+--------+--------+------+
```

### \# Imports Used ###

```
from texttable import Texttable
import pandas as pd
import numpy as np
```
