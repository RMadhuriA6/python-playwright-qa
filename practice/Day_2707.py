testRec = {
    'test_id': "1",
    'test_name': "Login",
    'status': "Pass",
    'priority': "High"
}

print(testRec)
print(testRec['status'])
print(testRec.get('status'))
testRec['status'] = 'fail'
print(testRec.get('status'))
testRec.update({'status': 'Progress'})
print(testRec.get('status'))
testRec.update({'Executed_by': 'Madhuri'})
print(testRec)
testRec.get('Time',0)
print(testRec.get('Time'))
# print(testRec['Time'])

myTuple = ("Chrome", "Firefox", "Edge")
print(myTuple)
myTuple[1]="Safari"
print(myTuple)

mySet = {"pass", "fail", "pass", "skip"}
print(mySet)
list2 = [1, 2, 3]
list1 = list2
list1 = list2.copy()
print(list1)
list1.append(4)

print(list2)