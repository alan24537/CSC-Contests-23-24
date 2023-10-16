from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.N = BoundedConstraint(1, 10000)
    self.R = BoundedConstraint(1, 10000)

def generate_input(self, **kwargs):
    n = self.N.next
    yield n
    self.K = BoundedConstraint(1, n)
    yield self.K.next
    for i in range(n):
        yield self.R.next


Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input


# alternatively, you can create the batches manually
batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='p4_ans.exe').start()