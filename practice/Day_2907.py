test1 = {
    'test_name': 'Login',
    'status': 'pass'
}
test2 = {
    'test_name': 'Home page',
    'status': 'fail'
}
test3 = {
    'test_name': 'Purchase',
    'status': 'blocked'
}
test4 = {
    'test_name': 'Logout',
    'status': 'progress'
}
tests = [test1, test2, test3, test4]

for test in tests:
    if test['status'] == 'pass':
        print(test['test_name'] + ' passed')
    elif test['status'] == 'fail':
        print(test['test_name'] + ' failed')
    elif test['status'] == 'progress':
        print(test['test_name'] + ' still running')
    elif test['status'] == 'blocked':
        print(test['test_name'] + ' blocked')
    else:
        print(test['test_name'] + ' unknown status')

count = 0
while count < len(tests):
    print('valid test')
    count = count+1
