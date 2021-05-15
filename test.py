from texttable import Texttable

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
