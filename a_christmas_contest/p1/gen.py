
from testcase_generator import BoundedConstraint, Case, Batch, Generator
import random

def set_constraints(self):
    self.N = BoundedConstraint(1, 2000)
    self.P = BoundedConstraint(1, 100)
    

def generate_input(self, **kwargs):
    n, p = self.N.next, self.P.next
    yield n, p
    path = "H" if random.randint(0, 1) == 0 else "W"
    for i in range(n - 1):
        if random.randint(0, p // 2) == 0:
            path += 'W'
        else:
            path += 'H'
    yield path
    

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='ans.exe').start()
