import sys
from cx_Freeze import setup, Executable

options = {
    "build_exe": {
        "includes": ["amounts"],
        "path": sys.path + ["modules"],
    }
}

executables = [Executable("income_expenses.pyw")]

setup(
    name="How distribute your money",
    version="0.1",
    description="How distribute your money",
    options=options,
    executables=executables,
)