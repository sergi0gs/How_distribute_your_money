# An advanced setup script to create multiple executables and demonstrate a few
# of the features available to setup scripts
#
# hello.py is a very simple 'Hello, world' type script which also displays the
# environment in which the script runs
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the script without Python

import sys
from cx_Freeze import setup, Executable

executables = [Executable("income_expenses.py"), Executable("amounts.py")]

setup(
    name="How distribute your money",
    version="0.1",
    description="How distribute your money",
    executables=executables,
)