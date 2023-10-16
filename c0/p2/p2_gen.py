from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.T1 = BoundedConstraint(1, 10000)
    self.T2 = BoundedConstraint(1, 10000)
    self.T3 = BoundedConstraint(1, 10000)
    self.X = BoundedConstraint(1, 10000)

def generate_input(self, **kwargs):
    yield self.T1.next
    yield self.T2.next
    yield self.T3.next
    yield self.X.next


Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input


# alternatively, you can create the batches manually
batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='p2_ans.exe').start()