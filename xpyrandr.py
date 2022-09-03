from sys import argv
from subprocess import PIPE, run
from parse import parser

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
            monitors[z] = [splitted_line[0]]

            # Adds highest refresh rate
            for w in splitted_line[1:]:
                w = w.strip().translate({ord(letter): None for letter in "-+*"})
                if w != "":
                    splitted_line_hz.append(float(w))

            monitors[z].append(max(splitted_line_hz))

print(monitors)