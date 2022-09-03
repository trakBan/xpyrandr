from sys import argv
from subprocess import PIPE, run
from parse import parser

# Wrapper for testing
def wrapper(monitors: dict) -> dict:
    for x in monitors:
        print(f"{x} - {monitors[x]}")

def finalXrandr(cmd: str) -> str:
    print(cmd)
    raise SystemExit()

parser(argv[1:])

raw_monitors: str = run(("xrandr --listmonitors").split(" "),
    stdout=PIPE, stderr=PIPE, universal_newlines=True).stdout

raw_xrandr: str = run(("xrandr").split(" "),
    stdout=PIPE, stderr=PIPE, universal_newlines=True).stdout

# Adds monitors to a dict
monitors : dict = {}
for x in raw_monitors.splitlines()[1:]:
    monitors[(x.split()[-1])] = []

splitted_line: list = []
splitted_line_hz: list = []

# Adds highest resolution and highest refresh rate
for y, x in enumerate(raw_xrandr.splitlines()):
    for z in monitors:
        if x.split()[0] in z:
            splitted_line = (raw_xrandr.splitlines()[y + 1].strip().split())

            # Adds highest resolution
            monitors[z].append(splitted_line[0])
 
            # Adds highest refresh rate
            for w in splitted_line[1:]:
                w = w.strip().translate({ord(letter): None for letter in "-+*"})
                if w != "":
                    splitted_line_hz.append(float(w))

            monitors[z].append(max(splitted_line_hz))

for y, x in enumerate(monitors):
    if y == 0:
        monitors[x] = (f"xrandr --output {x} --primary --size {monitors[x][0]} --rate {monitors[x][1]}")
    else:
        monitors[x] = (f"--output {x} --size {monitors[x][0]} --rate {monitors[x][1]}")

if len(monitors) == 1:
    finalXrandr(monitors[list(monitors)[0]])

if len(monitors) > 2:
    print("Currently this programm only supports up to 2 monitors!")
    raise SystemExit()

side: str = input("(left) or (right) based on the primary monitor: ").lower()
monitors[list(monitors)[1]] += f" --{side}-of {list(monitors)[0]}"

cmd: str = ""
for x in monitors:
    cmd += monitors[x] + " "

finalXrandr(cmd)