import os

CONTEST = 'a_christmas_contest'
NUM_PROBLEMS = 5

gen_template = '''
from testcase_generator import BoundedConstraint, Case, Batch, Generator

def set_constraints(self):
    self.N = BoundedConstraint(1, 1000)
    

def generate_input(self, **kwargs):
    yield self.N.next
    

Case.SET_CONSTRAINTS = set_constraints
Case.SET_INPUT = generate_input

batches = [
    Batch(num=1, cases=[Case() for i in range(10)])
]

Generator(batches=batches, exe='ans.exe').start()
'''

def problem_template(num):
    return f'''# Problem {num}:

**Time Limit:** 1s
**Memory Limit:** 128MB

## Constraints

## Input Specification

## Output Specification

## Sample Input

```txt

```

## Sample Output

```txt

```
'''

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the contest directory relative to the script's location
contest_dir = os.path.join(script_dir, CONTEST)
os.mkdir(contest_dir)

# Create the 'zips' directory relative to the contest directory
zips_dir = os.path.join(contest_dir, 'zips')
os.mkdir(zips_dir)

# Create problem directories and associated files
for i in range(NUM_PROBLEMS):
    problem_dir = os.path.join(contest_dir, f'p{i + 1}')
    os.makedirs(problem_dir)

    with open(os.path.join(problem_dir, 'problem.md'), 'w') as f:
        f.write(problem_template(i + 1))

    with open(os.path.join(problem_dir, 'problem.yaml'), 'w') as f:
        f.write(f'name: {CONTEST.upper()}P{i + 1}')

    with open(os.path.join(problem_dir, 'domjudge-problem.ini'), 'w') as f:
        f.write('timelimit=\'1\'')

    # Create empty files
    with open(os.path.join(problem_dir, 'ans.cpp'), 'w'):
        pass
    with open(os.path.join(problem_dir, 'ans.py'), 'w'):
        pass
    with open(os.path.join(problem_dir, 'gen.py'), 'w') as f:
        f.write(gen_template)