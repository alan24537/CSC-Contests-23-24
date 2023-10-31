import random
from testcase_generator import BoundedConstraint, Case, Batch, Generator

def tri_area(a, b, c):
    return abs((a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0]))/2.0
def is_inside(a, b, c, p):
    return tri_area(a, b, c) == tri_area(a, b, p) + tri_area(a, c, p) + tri_area(b, c, p)

def set_constraints(self):
    self.COORD = BoundedConstraint(-10**3, 10**3)

def generate_input(self, **kwargs):
    if random.randint(0, 1) == 0:
        yield self.COORD.next, self.COORD.next, self.COORD.next, self.COORD.next, self.COORD.next, self.COORD.next
        yield self.COORD.next, self.COORD.next 
    else:
        ax, ay, bx, by, cx, cy = self.COORD.next, self.COORD.next, self.COORD.next, self.COORD.next, self.COORD.next, self.COORD.next
        yield ax, ay, bx, by, cx, cy
        while True:
            px, py = self.COORD.next, self.COORD.next
            if is_inside((ax, ay), (bx, by), (cx, cy), (px, py)):
                yield px, py
                break
    

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(5)])
]

Generator(batches=batches, exe='ans.exe').start()
