# Currently this doesn't work

from setuptools import setup
from src.globalVariables import *

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="xpyrandr",
    license="GPLv3",
    version=VERSION,
    description="Yet another xrandr auto setter tool",
    long_description=long_description,

    packages=[
        "src/colors.py",
        "src/globalVariables.py",
        "src/parse.py"
    ],
    
    scripts=["xpyrandr"]
)