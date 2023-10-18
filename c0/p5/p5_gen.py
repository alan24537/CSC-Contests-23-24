from testcase_generator import BoundedConstraint, Case, Batch, Generator, CustomGeneratorConstraint, StringGenerator

def set_constraints(self):
    self.N = BoundedConstraint(1, 1000)
    self.Q = BoundedConstraint(1, 1000)
    self.A = CustomGeneratorConstraint(generator=StringGenerator)
    self.S = BoundedConstraint(1, 1000000)
    self.X = BoundedConstraint(1, 1000000)
    
    self.A.initialize(BoundedConstraint(1, 30))

def generate_input(self, **kwargs):
    n = self.N.next
    q = self.Q.next
    names = set([self.A.next for i in range(n)])
    sweets = set([self.S.next for i in range(n)])
    yield len(names), q
    for name in names:
        yield name, self.S.next
    for i in range(q):
        yield self.X.next


Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input


# alternatively, you can create the batches manually
batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='p5_ans.exe').start()