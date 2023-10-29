import random
from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.N = BoundedConstraint(1, 10**5)
    self.A_i = BoundedConstraint(1, 10**9)
    

def generate_input(self, **kwargs):
    n = self.N.next
    if random.randint(0, 1) == 0:
        yield n
        for i in range(n):
            yield self.A_i.next
    else:
        n -= n % 2
        arr = []
        yield n
        for i in range(n // 2):
            odd, even = self.A_i.next, self.A_i.next
            arr.append(odd - ((odd + 1) % 2))
            arr.append(even - (even % 2))
        random.shuffle(arr)
        for num in arr:
            yield num
        

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(4)]),
    Batch(num=2, cases=[Case(N=BoundedConstraint(10**5, 10**5)) for i in range(1)]),
]

Generator(batches=batches, exe='ans.exe').start()
