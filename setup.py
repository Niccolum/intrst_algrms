import os
import sys

from setuptools import setup

if sys.version_info < (3, 6):
    # python must be greater than 3.5 because of https://www.python.org/dev/peps/pep-0484/
    # python must be greater than 3.6 because of https://www.python.org/dev/peps/pep-0515/
    raise RuntimeError("Intrst_algrms 3.x requires Python 3.6+")


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

install_requires = [
    'iteration-utilities',
    'more-itertools'
]

tests_require = [
    'memory-profiler',
    # 'line-profiler', # install line-profiler manually
    'matplotlib'
]

extras_require = {
    'docs': [
        'Sphinx',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup(
    name="Intrst_algrms",
    author="Nikolai Vidov",
    author_email="lastsal@mail.ru",
    version=read('VERSION'),
    description="https://intrst-algrms.readthedocs.io/en/latest/",
    license="MIT",
    keywords="example documentation algorithms",
    url="https://pypi.org/project/Intrst-algrms/",
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    platforms='any',
    packages=['.', 'tree_sort', 'knapsack_problem', 'unpacking_flatten_lists'],
    package_data={
        # If any package contains files, include them:
        '': ['*.txt', '*.rst', '*.md', '*.png', '*.lprof', '*.json', '*.dat'],
    },
    python_requires='>=3.6',
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
