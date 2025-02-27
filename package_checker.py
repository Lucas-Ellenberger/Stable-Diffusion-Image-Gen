import importlib.util
import sys

# This file was used as a sanity check to ensure the listed packages were properly installed.

# For illustrative purposes.
names = ['pathlib', 'numpy', 'torch', 'huggingface_hub', 'packaging', 'tqdm', 'diffusers']

for name in names:
    if name in sys.modules:
        print(f"{name!r} already in sys.modules")
    elif (spec := importlib.util.find_spec(name)) is not None:
        # If you choose to perform the actual import ...
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        print(f"{name!r} has been imported")
    else:
        print(f"can't find the {name!r} module")
