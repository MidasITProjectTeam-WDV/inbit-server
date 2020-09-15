import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
_BASE = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(_BASE)
ROOT_DIR = os.path.dirname(BASE_DIR)

print(BASE_DIR)