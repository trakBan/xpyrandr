from globalVariables import *

def parser(args: list) -> list:

    for x in args:
        if x in ("--help", "-h"):
            print(HELP)
            raise SystemExit()

        if x in ("--version", "-v"):
            print("Version:", VERSION)
            raise SystemExit()