# Programming Assignment 1: Gale–Shapley Stable Matching

## Students
Natahja Graddy - UFID: XXXX-XXXX
Nathan King - UFID: 7218-0427

## Build/Compilation Instructions
Build/Compilation not required, as this project is in Python.

## Files
ProgrammingAssignment1.py: Runs Gale Shapley Algorithm.
validity_check.py: Contains 2 functions, one for checking validity of output, one for checking stability of matchings.
exampleData.txt: File to be read into GS Algorithm.
output.txt: Matchings produced by GS.


## Running the Matcher
To generate a stable matching, run:

```bash
python ProgrammingAssignment1.py exampleData.txt output.txt
```

## Running the Verifier
The verifier is implemented in `validity_check.py` as helper functions that
check the validity and stability of the produced matching.
These checks are executed automatically when the matcher is run.


## Assumptions
The number of hospitals and students is equal.
Each hospital and student has a complete, ordered preference list of size n where n is the number of hospitals.
Input files follow the format specified in the assignment.
Python 3 is used for execution.

### Example Input

2
1 2
2 1
2 1
1 2

### Example Output
1 1
2 2




