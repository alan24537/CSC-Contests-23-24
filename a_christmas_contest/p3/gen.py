
from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.Y = BoundedConstraint(1, 5000)
    self.M = BoundedConstraint(1, 12)
    self.D = BoundedConstraint(1, 31)

def generate_input(self, **kwargs):
    year, month, day = str(self.Y.next), str(self.M.next), str(self.D.next)
    yield f"{"0" * (4 - len(year))}{year}/{"0" * (2 - len(month))}{month}/{"0" * (2 - len(day))}{day}"

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(3)]),
    Batch(num=2, cases=[Case(Y=BoundedConstraint(2023, 2023)) for i in range(3)]),
    Batch(num=3, cases=[Case(Y=BoundedConstraint(2023, 2023), M=BoundedConstraint(12, 12)) for i in range(3)]),
    Batch(num=4, cases=[Case(Y=BoundedConstraint(2023, 2023), M=BoundedConstraint(12, 12), D=BoundedConstraint(25, 25)) for i in range(1)]),
]

Generator(batches=batches, exe='ans.exe').start()