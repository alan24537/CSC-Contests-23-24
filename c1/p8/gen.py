
from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.N = BoundedConstraint(1, 1000)
    

def generate_input(self, **kwargs):
    yield self.N.next
    

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='ans.exe').start()
