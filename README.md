### To setup:
```
python3.13 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### To run a solution for year `year` and day `day`:
```
aoc/bin/python src/solution_runner <year> <day> <part>
```
e.g. to run part 1 from day 4 of 2015:
```
aoc/bin/python src/solution_runner 2015 4 1
```
e.g. to run part 2 from day 1 of 2016:
```
aoc/bin/python src/solution_runner 2016 1 2
```

### Example inputs
You can run the above commands with an additional `--example` flag to run it using the example provided in the instructions.

e.g. to run part 2 from day 1 of 2016 with example input:
```
aoc/bin/python src/solution_runner 2016 1 2 -- example
```

You can delete the `.example` files from the `inputs` directory to reset examples.

### To  submit your solution:
Add the `--submit` flag
```
aoc/bin/python src/solution_runner <year> <day> <part> --submit
```
