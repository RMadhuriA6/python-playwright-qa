test1 = {
    'test_name': 'Login',
    'status': 'pass',
    'priority': 'high'
}
test2 = {
    'test_name': 'Home page',
    'status': 'fail',
    'priority': 'medium'
}
test3 = {
    'test_name': 'Purchase',
    'status': 'blocked',
    'priority': 'low'
}
test4 = {
    'test_name': 'Logout',
    'status': 'progress',
    'priority': 'not specified'
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




def full_test_report(name, status, priority):
    if priority == 'high':
        return 'fix immediately'
    elif priority == 'medium':
        return 'fix next week'
    elif priority == 'low':
        return 'fix next cycle'
    else:
        return f'unknown priority: {priority}'
    return f'{name}: {status_msg}, priority: {priority_msg}'

