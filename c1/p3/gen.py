import random
from testcase_generator import BoundedConstraint, Case, Batch, Generator, CustomGeneratorConstraint, StringGenerator

names = ["miso", "hakuto", "ringo", "paula", "sprite"]

def set_constraints(self):
    self.S = CustomGeneratorConstraint(generator=StringGenerator)
    
    self.S.initialize(BoundedConstraint(1, 10000))
    

def generate_input(self, **kwargs):
    if random.randint(1, 3) == 1:
        yield random.choice(names)
    else:
        yield self.S.next
    

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(5)])
]

Generator(batches=batches, exe='ans.exe').start()
