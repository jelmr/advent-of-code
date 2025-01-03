import argparse
import shutil
import os


# Creates the necessary directory structure for the given day/year, and copies the filled in templates to that directory
def create_day(year: int, day: int):
    dir_name = f'year_{year}/day_{day}/'

    os.makedirs(dir_name, exist_ok=True)

    if not os.path.exists(dir_name + 'part1.py'):
        shutil.copy2('templates/part1.py.template', dir_name + 'part1.py')
    if not os.path.exists(dir_name + 'part2.py'):
        shutil.copy2('templates/part2.py.template', dir_name + 'part2.py')
    if not os.path.exists(dir_name + 'test.py'):
        with open('templates/test.py.template', 'r') as test_template:
            template = test_template.read()
            filled_template = template.replace('{{YEAR}}', str(year)).replace('{{DAY}}', str(day))

            with open(dir_name + 'test.py', 'w') as output:
                output.write(filled_template)


def main():
    parser = argparse.ArgumentParser(description='Generate code from a template.')
    parser.add_argument('year', type=int, help='year number to create solution for')
    parser.add_argument('--day', type=int,
                        help='day number to create solution for. Leave empty to generate for all days')
    parser.set_defaults(day=None)
    args = parser.parse_args()

    if args.day is not None:
        create_day(args.year, args.day)
    else:
        for day in range(1, 26):
            create_day(args.year, day)


if __name__ == '__main__':
    main()
