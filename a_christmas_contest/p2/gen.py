
from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.N = BoundedConstraint(1, 100)
    

def generate_input(self, **kwargs):
    yield self.N.next
    

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(8)]),
    Batch(num=2, cases=[Case(N=BoundedConstraint(1, 1)) for i in range(1)]),
    Batch(num=3, cases=[Case(N=BoundedConstraint(100, 100)) for i in range(1)]),
]

Generator(batches=batches, exe='ans.exe').start()
