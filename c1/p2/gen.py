
from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.N = BoundedConstraint(1, 10**3)
    self.X = BoundedConstraint(1, 10**4)
    

def generate_input(self, **kwargs):
    yield self.N.next
    yield self.X.next
    

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(4)]),
    Batch(num=2, cases=[Case(X=BoundedConstraint(10**4, 10**4)) for i in range(1)]),
]

Generator(batches=batches, exe='ans.exe').start()
