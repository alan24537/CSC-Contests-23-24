
from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.N = BoundedConstraint(1, 10**5)
    self.A_i = BoundedConstraint(1, 10**9)
    

def generate_input(self, **kwargs):
    n = self.N.next
    yield n
    for i in range(n):
        yield self.A_i.next
    

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(5)]),
    Batch(num=2, cases=[Case(N=BoundedConstraint(10**5, 10**5)) for i in range(1)])
]

Generator(batches=batches, exe='ans.exe').start()
