import glob
import os

# Collect all .py files inside the current folder (modules)
mod_files = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))

ALL_MODULES = [
    os.path.basename(f)[:-3]
    for f in mod_files
    if os.path.isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
]
