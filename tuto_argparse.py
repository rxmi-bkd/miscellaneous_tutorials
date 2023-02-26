import argparse

parser = argparse.ArgumentParser(description="some description")

parser.add_argument("-arg1", "--arg1",
                    required=True,
                    help="some help about arg1")

parser.add_argument("-arg2", "--arg2",
                    required=False,
                    help="some help about arg2")

args = vars(parser.parse_args())

print(f"arg1: {args['arg1']}, arg2: {args['arg2']}")
