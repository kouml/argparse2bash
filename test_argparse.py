import argparse
from transpiler import transpile


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='this is the simplest tool with argparse')
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                     help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')
    args = parser.parse_args()

    transpile(parser, 'sum.sh', 'bash')
