from sys import stderr, exit
import argparse


def read_file(content, newline=False, numbered=False):
    try:
        with open(content, 'r') as f:
            line_number = 0
            for line in f:
                noargs_lines = line.rstrip('\n')
                if newline:
                    noargs_lines += "$"
                if numbered:
                    line_number += 1
                    noargs_lines = f"{line_number} {noargs_lines}"
                
                print(noargs_lines)

    except FileNotFoundError as e:
        print(f"{e} File not found", end='\n', file=stderr)
        exit(1)


def main():
    parser = argparse.ArgumentParser(description='Print the content of a file/s')
    parser.add_argument('files', metavar='filename', type=str, nargs='*', help='Files to show')
    parser.add_argument('-e', action='store_true', help='Add $ at the end of each line')
    parser.add_argument('-n', action='store_true', help='Show line numbers like nl util')
    args = parser.parse_args()
    
    for filename in args.files:
        read_file(filename, args.e, args.n)


if __name__ == '__main__':
    main()