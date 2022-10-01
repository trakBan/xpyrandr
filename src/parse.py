from src.globalVariables import *

def parser(args: list) -> list:

    # Prints help and then quits
    for x in args:
        if x in ("--help", "-h"):
            print(HELP)
            raise SystemExit()

        # Prints the version and then quits
        if x in ("--version", "-v"):
            print("Version:", VERSION)
            raise SystemExit()