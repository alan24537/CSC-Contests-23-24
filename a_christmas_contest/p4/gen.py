import random
from testcase_generator import BoundedConstraint, Case, Batch, Generator, CustomGeneratorConstraint, StringGenerator

def set_constraints(self):
    self.N = BoundedConstraint(2, 10000)
    self.S = CustomGeneratorConstraint(generator=StringGenerator)
    self.S.initialize(BoundedConstraint(1, 30))

def generate_input(self, **kwargs):
    n = self.N.next
    yield n
    names = set()
    while len(names) != n:
        names.add(self.S.next)
    valid = False
    names = list(names)
    copy_names = names[:]
    while not valid:
        valid = True
        random.shuffle(copy_names)
        for i in range(n):
            if names[i] == copy_names[i]:
                valid = False
                break
    for i in range(n):
        yield names[i], copy_names[i]

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='ans.exe').start()
