class TestCase:
    def __init__(self, name, status, priority):
        self.TestName = name
        self.TestStatus = status
        self.TestPriority = priority

    def report(self):
        name = self.TestName
        status_msg = self.TestStatus
        if self.TestPriority == 'high':
            priority_msg = 'fix immediately'
        elif self.TestPriority == 'medium':
            priority_msg = 'fix next week'
        elif self.TestPriority == 'low':
            priority_msg = 'fix next cycle'
        else:
            priority_msg = f'unknown priority- {self.TestPriority}'
        return f'{name}: {status_msg}, priority: {priority_msg}'


Test1 = TestCase("Login", "pass", "high")
Test2 = TestCase("Logout", "fail", "boomerang")
print(Test2.report())
print(Test1.report())

