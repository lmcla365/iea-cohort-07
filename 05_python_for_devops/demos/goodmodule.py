"""
goodmodule - Collection of really good stuff!
"""
import sys

def do_good(args):
    """This function does really good things!"""
    print("This is definitely good.")
    print("Here are my args:", args)




if __name__ == "__main__":
    print("Running as a script!")
    print(f"My name is {__name__}")
    args = sys.argv[1:]
    do_good(args)
