import os
import sys

from setuptools import setup

if sys.version_info < (3, 6):
    raise RuntimeError("Intrst_algrms 3.x requires Python 3.6+")


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Intrst_algrms",
    version=read('VERSION.md'),
    author="Nikolai Vidov",
    author_email="lastsal@mail.ru",
    description="https://intrst-algrms.readthedocs.io/en/latest/",
    license="MIT",
    keywords="example documentation algorithms",
    url="https://pypi.org/project/Intrst-algrms/",
    packages=['.', 'binary_tree', 'knapsack_problem', 'unpacking_flatten_lists'],
    package_data={
        # If any package contains files, include them:
        '': ['*.txt', '*.rst', '*.md', '*.png', '*.lprof', '*.json', '*.dat'],
    },
    python_requires='>=3.6',
    install_requires=[
        'Cython',
        'iteration-utilities',
        'more-itertools',
        'memory-profiler',
        # 'line-profiler', # install line-profiler manually
        'matplotlib',
    ],
    long_description=read('README.md'),
)