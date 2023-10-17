from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.N = BoundedConstraint(1, 100000)
    self.Q = BoundedConstraint(1, 100000)
    self.L = BoundedConstraint(1, 1000000)
    self.S = BoundedConstraint(1, 1000000)
    self.D = BoundedConstraint(1, 1000000)

def generate_input(self, **kwargs):
    n, q = self.N.next, self.Q.next
    yield n, q
    min_l = 1e9
    for i in range(n):
        l, s = self.L.next, self.S.next
        min_l = min(min_l, l)
        yield l, s
    for i in range(q):
        d = self.D.next
        if d < min_l:
            yield min_l
        else:
            yield d


Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input


# alternatively, you can create the batches manually
batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='p8_ans.exe').start()