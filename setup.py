import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Intrst_algrms",
    version="0.0.1",
    author="Nikolai Vidov",
    author_email="lastsal@mail.ru",
    description="https://intrst-algrms.readthedocs.io/en/latest/",
    license="MIT",
    keywords="example documentation algorithms",
    url="https://intrst-algrms.readthedocs.io/en/latest/",
    packages=['binary_tree', 'knapsack_problem', 'unpacking_flatten_lists'],
    package_data={
        # If any package contains files, include them:
        '': ['*.txt', '*.rst', '*.md', '*.png', '*.lprof', '*.json', '*.dat'],
    },
    python_requires='>=3.6',
    install_requires=[
        'iteration-utilities',
        'more-itertools',
        'memory-profiler',
        'line-profiler',
        'matplotlib',
    ],
    long_description=read('README.md'),
)