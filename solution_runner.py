import argparse
import time
from pydoc import locate
from aoc_client import AocClient


class SolutionRunner:

    def __init__(self, year: int, day: int, part: int, example: bool):
        self.year = year
        self.day = day
        self.part = part
        self.example = example
        self.aocClient = AocClient()
        self.solution = self.get_solution(year, day, part)

    @staticmethod
    def get_solution(year: int, day: int, part: int):
        day_str = str(day).zfill(2)
        solution_class_name = f'year_{year}.day_{day_str}.part{part}.Part{part}'
        solution_class = locate(solution_class_name)
        if not solution_class:
            raise Exception(f'No solution for day {day}, expected \'{solution_class_name}\' to exist.')
        return solution_class()

    def run(self, show_input, submit):
        if self.example:
            input_data = self.aocClient.get_example(self.year, self.day)
        else:
            input_data = self.aocClient.get_input(self.year, self.day)

        if show_input:
            print(f'INPUT:')
            print('>>>', input_data)

        start = time.time()
        result = self.solution.solve(input_data)
        duration = time.time() - start
        print(f'OUTPUT:')
        print('>>>', result)
        print(f'Time elapsed: {duration:.2f}')

        if submit:
            print('Submitting to Advent of Code!')
            response = self.aocClient.submit(self.year, self.day, self.part, result)
            print('Result: ')
            print(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download input files for Advent of Code')
    parser.add_argument('year', type=int, help='year number to download input for')
    parser.add_argument('day', type=int, help='day number to download input for')
    parser.add_argument('part', type=int, help='part number to download input for')
    parser.add_argument('-e', '--example', dest='example', action='store_true', help='whether to run the example input')
    parser.add_argument('-i', '--show-input', dest='show_input', action='store_true', help='whether to print the used input to the console')
    parser.add_argument('-s', '--submit', dest='submit', action='store_true', help='whether to submit the answer to AoC')
    parser.set_defaults(example=False, submit=False, show_input=False)
    args = parser.parse_args()

    if args.example and args.submit:
        exit(1)

    runner = SolutionRunner(args.year, args.day, args.part, args.example)
    runner.run(args.show_input, args.submit)