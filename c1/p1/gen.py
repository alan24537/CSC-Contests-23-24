
from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.C = BoundedConstraint(1, 10**3)
    self.D = BoundedConstraint(1, 10**3)

def generate_input(self, **kwargs):
    yield self.C.next
    yield self.D.next

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(4)]),
    Batch(num=2, cases=[Case(C=BoundedConstraint(10**3, 10**3), D=BoundedConstraint(10**3, 10**3)) for i in range(1)])
]

Generator(batches=batches, exe='ans.exe').start()
