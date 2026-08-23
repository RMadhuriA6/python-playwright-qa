qaList = ["Login", "SignUp", "Add To Cart", "Purchase", "Log out"]

print(qaList)
print(qaList[0], qaList[-1])
qaList.append("Close")
print(qaList)
qaList.remove("Purchase")
for x in qaList:
    print(str(qaList.index(x)) + ":" + x)
print(qaList)
qaList.append("Log out")
for x in qaList:
    print(str(qaList.index(x)) + ":" + x)
print(qaList)
for index, value in enumerate(qaList):
    print(index, ':', value)

s = "Automation Testing"
s.replace("Testing", "Framework")
print(s)