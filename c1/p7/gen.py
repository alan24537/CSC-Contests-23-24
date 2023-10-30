
from testcase_generator import BoundedConstraint, Case, Batch, Generator

def dist(x1, y1, x2, y2):
    return int((abs(x1-x2)**2 + abs(y1-y2)**2)**0.5)

def set_constraints(self):
    self.N = BoundedConstraint(1, 10**3)
    self.M = BoundedConstraint(1, 10**3)
    self.P = BoundedConstraint(-10**4, 10**4)

def generate_input(self, **kwargs):
    n, m = self.N.next, self.M.next
    litter, food = [], []
    for i in range(n):
        litter.append((self.P.next, self.P.next))
    for i in range(m):
        food.append((self.P.next, self.P.next))
    
    max_dist = -1
    for i in range(n):
        for j in range(m):
            max_dist = max(max_dist, dist(litter[i][0], litter[i][1], food[j][0], food[j][1]))
    for i in range(n):
        for j in range(m):
            if dist(litter[min(i, n - 1)][0], litter[min(i, n - 1)][1], food[j][0], food[j][1]) == max_dist:
                del litter[i]
                n -= 1
    yield n, m
    for i in range(n):
        yield litter[i][0], litter[i][1]
    for i in range(m):
        yield food[i][0], food[i][1]
    

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(4)]),
    Batch(num=2, cases=[Case(N=BoundedConstraint(10**3, 10**3), M=BoundedConstraint(10**3, 10**3)) for i in range(1)]),
]

Generator(batches=batches, exe='ans.exe').start()
