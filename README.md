[![](https://travis-ci.org/Niccolum/intrst_algrms.svg?branch=master)](https://travis-ci.org/Niccolum/intrst_algrms) <!-- travis-ci build status -->
[![](https://codecov.io/gh/Niccolum/intrst_algrms/branch/master/graph/badge.svg)](https://codecov.io/gh/Niccolum/intrst_algrms) <!-- Code Coverage by Codecov -->
[![](https://img.shields.io/snyk/vulnerabilities/github/Niccolum/intrst_algrms)](https://app.snyk.io/org/niccolum/) <!-- Vulnerabilities by SNYK -->
[![](https://img.shields.io/codacy/grade/6157aa23ef6e4886b146b9b16a7a68c8)](https://app.codacy.com/project/lastsal/intrst_algrms/dashboard) <!-- Codacy Badge -->

[![](https://img.shields.io/pypi/v/Intrst_algrms.svg?colorB=blue)](https://pypi.org/project/Intrst-algrms/) <!-- travis-ci build status -->
[![](https://img.shields.io/pypi/pyversions/Intrst_algrms.svg)](https://github.com/Niccolum/intrst_algrms/blob/master/setup.py#L65) <!-- Package version -->
[![](https://img.shields.io/pypi/l/Intrst_algrms.svg?colorB=blue)](https://github.com/Niccolum/intrst_algrms/blob/master/LICENSE.md) <!-- Licence -->
[![](https://img.shields.io/pypi/status/Intrst_algrms)](https://github.com/Niccolum/intrst_algrms/blob/master/setup.py#L60) <!-- Project status -->
[![](https://img.shields.io/github/last-commit/Niccolum/Intrst_algrms)](https://github.com/Niccolum/intrst_algrms/commits/master) <!-- Last Commit -->

# Instruments and algorithms

Here is examples of realizations several algorithms, they performance, memory used and result plots.

## Getting Started

### Requirements

Python 3.6+

### Installing

```bash
    python3 -m venv env
    source env/bin/activate
```

#### For check and research

```bash
    pip install -e git+https://github.com/Niccolum/intrst_algrms#egg=Intrst_algrms['all']
    cd env/src/intrst_algrms
```

##### Note

*For check memory tests - install line_profiler manually.*
*This package not include to install because of problem with installation. Details [here](https://github.com/rkern/line_profiler#installation)*

After that you can run commands from results.md on each folders.

More detailed description and HOW-TO:

Results of research algorithms here:
*   [Binary Tree (sorting)](https://github.com/Niccolum/intrst_algrms/blob/master/binary_tree/results.md)
*   [Knapsack problem](https://github.com/Niccolum/intrst_algrms/blob/master/knapsack_problem/results.md)
*   [Unpacking nested lists of indefinite depth](https://github.com/Niccolum/intrst_algrms/blob/master/unpacking_flatten_lists/results.md)

#### For use funcs in your own code you can install package from PYPI

```bash
    pip install Intrst_algrms
```

and import it from your code:
```python
    from binary_tree.funcs import ...
    from knapsack_problem.funcs import ...
    from unpacking_flatten_lists.funcs import ...
```

More, about funcs, in [docs](https://intrst-algrms.readthedocs.io/en/latest/)

## Contributing

Please read [CONTRIBUTING.md](https://github.com/Niccolum/intrst_algrms/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Dev

For developers info [here](https://github.com/Niccolum/intrst_algrms/blob/master/README-DEV.md).

## Authors

*   **Nikolai Vidov** - *maintainer* - [Niccolum](https://github.com/Niccolum)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Niccolum/intrst_algrms/blob/master/LICENSE.md) file for details