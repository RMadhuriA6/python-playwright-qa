Status = ['pass', 'fail', 'progress', 'blocked']
Priority = ['high', 'medium', 'low']

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


def check_priority(value='high'):
    if value == 'high':
        return 'fix immediately'
    elif value == 'medium':
        return 'fix next week'
    elif value == 'low':
        return 'fix next cycle'
    else:
        return f'unknown priority: {value}'


def check_status(value):
    if value == 'pass':
        return 'case passed'
    elif value == 'fail':
        return 'case failed'
    elif value == 'progress':
        return 'case in progress'
    else:
        return f'unknown status: {value}'


def check_severity():
    severity = 'more'


def full_test_report(name, status, priority):
    status_msg = check_status(status)
    priority_msg = check_priority(priority)

    return f'{name}: {status_msg}, priority: {priority_msg}'


for test in tests:
    print(full_test_report(test['test_name'], test['status'], test['priority']))

print(full_test_report(name='Logout', status='progress', priority='low'))

try:
    print(full_test_report(('test7', 'medium', 'fail')))
except TypeError:
    print('Checkout the count of arguments passed')


    def outer():
        x = 5

        def inner():
            print(x)

        inner()


    outer()
