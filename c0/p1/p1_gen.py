from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.N = BoundedConstraint(0, 1000)
    self.M = BoundedConstraint(1, 1000)
    self.O = BoundedConstraint(1, 1000)
    self.C = BoundedConstraint(1, 1000)

def generate_input(self, **kwargs):
    yield self.N.next
    yield self.M.next
    yield self.O.next
    yield self.C.next


Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input


# alternatively, you can create the batches manually
batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='p1_ans.exe').start()