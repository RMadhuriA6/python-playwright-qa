Status = ['pass', 'fail', 'progress', 'blocked']
for value in Status:
    if value == 'pass':
        print('case passed')
    elif value == 'fail':
        print('case failed')
    elif value == 'progress':
        print('case in progress')
    else:
        print('unknown status:', value)

# Predicted : I think it goes an error which should be handled with exception

a = "pass"
b = "pas" + "s"
print(a is b)
print(a == b)