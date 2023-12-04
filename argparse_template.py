import argparse
import webbrowser

parser = argparse.ArgumentParser()

# Positional argument
parser.add_argument('a')

# Named argument
parser.add_argument('-l', '--link', help='Link for open in webbrowser')

# Flag argument if need some default value
parser.add_argument('-v', '--value', action='store_const', const=10, help='Verbose mode flag')

# Flag argument if need true or false
parser.add_argument('-t', '--true', action='store_true', help='Flag with true')
parser.add_argument('-f', '--false', action='store_false', help='Flag with false')

# Some arguments (2, 3, 4)
parser.add_argument('-s', '--some_args', nargs=2, help='Arg with some args')

# With choices
parser.add_argument('-c', '--choices', choices=[1, 2, 3], help='Arg with choices')

args = parser.parse_args()

print(args)
print(args.some_args[1])