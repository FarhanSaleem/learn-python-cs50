import sys

# sys.argv is the list of arguments that user
# typed in before the pressed enter
# used with command line programs

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# slice in a list to get subset of list with starting index and : number of items
for arg in sys.argv[1:]:
    print("hello, my name is", arg)

