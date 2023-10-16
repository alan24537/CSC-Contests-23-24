from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.N = BoundedConstraint(1, 1000)
    self.C = BoundedConstraint(1, 10000)
    self.D = BoundedConstraint(1, 100000)

def generate_input(self, **kwargs):
    n =  self.N.next
    yield n
    yield self.D.next
    for i in range(n):
        yield self.C.next


Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input


# alternatively, you can create the batches manually
batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='p3_ans.exe').start()