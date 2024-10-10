import argparse
import re

def grep(pattern, file, ignore_case, line_number):
    regex_flags = re.IGNORECASE if ignore_case else 0
    compiled_pattern = re.compile(pattern, regex_flags)

    if file:
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Error: File {file} not found.")
            return

    for i, line in enumerate(lines, 1):
        if compiled_pattern.search(line):
            if line_number:
                print(f"{i}:", end=" ")
            print(line.rstrip())

parser = argparse.ArgumentParser(description = "Python grep tool")
parser.add_argument("pattern", help="Search pattern")
parser.add_argument("file", help="File to search")
parser.add_argument("-i", "--ignore-case", action="store_true", help="Ignore case")
parser.add_argument("-n", "--line-number", action="store_true", help="Prefix each line of output with line number")

args = parser.parse_args()

grep(args.pattern, args.file, args.ignore_case, args.line_number)