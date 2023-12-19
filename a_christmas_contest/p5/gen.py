import random
from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.N = BoundedConstraint(1, 2000)
    self.M = BoundedConstraint(1, 2000)
    
def generate_input(self, **kwargs):
    n, m = self.N.next, self.M.next
    yield n, m
    
    grid = [['X' if random.randint(0, 2) == 0 else '.' for j in range(m)] for i in range(n)]
    grid[random.randint(0, n - 1)][random.randint(0, m - 1)] = 'E'
    grid[random.randint(0, n - 1)][random.randint(0, m - 1)] = 'H'
    
    for i in range(n):
        yield ''.join(grid[i])
    

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='ans.exe').start()
