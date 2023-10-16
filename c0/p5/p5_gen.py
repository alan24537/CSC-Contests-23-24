from testcase_generator import BoundedConstraint, Case, Batch, Generator, CustomGeneratorConstraint, StringGenerator
import random

jp = [
    "a", "i", "u", "e", "o",
    "ka", "ki", "ku", "ke", "ko",
    "sa", "shi", "su", "se", "so",
    "ta", "chi", "tsu", "te", "to",
    "na", "ni", "nu", "ne", "no",
    "ha", "hi", "fu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",
    "ya", "yu", "yo",
    "ra", "ri", "ru", "re", "ro",
    "wa", "wo", "n"
]

def set_constraints(self):
    self.S = CustomGeneratorConstraint(generator=StringGenerator)
    
    self.S.initialize(BoundedConstraint(1, 10000))

def generate_input(self, **kwargs):
    if random.randint(1, 3) == 1:
        yield self.S.next
    else:
        yield "".join([random.choice(jp) for i in range(random.randint(1, 4000))])
        
Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input


# alternatively, you can create the batches manually
batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='p5_ans.exe').start()