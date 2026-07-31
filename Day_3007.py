Status = ['pass', 'fail', 'progress', 'blocked']
Priority = ['high', 'medium', 'low']


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


for status in Status:
    print(check_status(status))

print(check_priority('medium'))
print(check_priority())
check_severity()
print(check_severity())



def full_test_report(name,status,priority):
    status_msg = check_status(status)
    priority_msg = check_priority(priority)

    return f'{name}: {status_msg}, priority: {priority_msg}'