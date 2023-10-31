from testcase_generator import BoundedConstraint, Case, Batch, Generator
import random

def set_constraints(self):
    self.N = BoundedConstraint(1, 10**6)
    self.K = BoundedConstraint(1, 10**9)
    self.A_i = BoundedConstraint(1, 10**9)
    self.min_ans = BoundedConstraint(1, 10**6)
    
def generate_input(self, **kwargs):
    n = self.N.next
    k = self.K.next
    min_ans = self.min_ans.next
    yield n, k
    arr = [self.A_i.next for i in range(n)]
    for i in range(min_ans):
        idx1 = random.randint(0, n-1)
        idx2 = random.randint(0, n-1)
        arr[idx2] = abs(k - arr[idx1])
    yield arr

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(4)]),
    Batch(num=2, cases=[Case(N=BoundedConstraint(10**6, 10**6), K=BoundedConstraint(1, 1)) for i in range(1)]),
]

Generator(batches=batches, exe='ans.exe').start()
