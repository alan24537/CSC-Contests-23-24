from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.N = BoundedConstraint(2, 100000)
    self.Q = BoundedConstraint(1, 100000)
    self.C = BoundedConstraint(1, 1000)
    self.P = BoundedConstraint(1, 1000)

def generate_input(self, **kwargs):
    n = self.N.next
    q = self.Q.next
    c = self.C.next
    yield n, q, c
    yield [self.P.next for i in range(n)]
    for i in range(q):
        self.A = BoundedConstraint(1, n)
        a = self.A.next
        self.B = BoundedConstraint(a, n)
        b = self.B.next
        yield a, b

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input


# alternatively, you can create the batches manually
batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='p6_ans.exe').start()