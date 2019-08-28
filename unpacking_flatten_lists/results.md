## OS info
```
$ lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 10 (buster)
Release:    10
Codename:   buster
```
## CPU info
```
$ lscpu
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
Address sizes:       36 bits physical, 48 bits virtual
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  2
Core(s) per socket:  2
Socket(s):           1
NUMA node(s):        1
Vendor ID:           GenuineIntel
CPU family:          6
Model:               42
Model name:          Intel(R) Core(TM) i5-2410M CPU @ 2.30GHz
Stepping:            7
CPU MHz:             1067.519
CPU max MHz:         2900.0000
CPU min MHz:         800.0000
BogoMIPS:            4589.31
Virtualization:      VT-x
L1d cache:           32K
L1i cache:           32K
L2 cache:            256K
L3 cache:            3072K
NUMA node0 CPU(s):   0-3
```
## Memory info
```
$ free -m
              total        used        free      shared  buff/cache   available
Mem:           5872        1067        3429         157        1375        4381
Swap:          6053           0        6053
```

## start to work
```
$ python -V
Python 3.7.3

$ cd ~/unpacking_flatten_lists
```
## run tests
```
$ python -m unittest tests.main -v
test_niccolum_flatten (tests.flatten_funcs.TestFlattenFunctions) ... 0.59161s
ok
test_outer_flatten_1 (tests.flatten_funcs.TestFlattenFunctions) ... 0.43485s
ok
test_outer_flatten_2 (tests.flatten_funcs.TestFlattenFunctions) ... 3.10676s
ok
test_recursive_flatten_iterator (tests.flatten_funcs.TestFlattenFunctions) ... 2.59538s
ok
test_recursive_flatten_generator (tests.flatten_funcs.TestFlattenFunctions) ... 0.54907s
ok
test_tishka_flatten (tests.flatten_funcs.TestFlattenFunctions) ... 2.19138s
ok
test_tishka_flatten_with_stack (tests.flatten_funcs.TestFlattenFunctions) ... 0.48661s
ok
test_zart_flatten (tests.flatten_funcs.TestFlattenFunctions) ... 0.46095s
ok
test_create_data_decreasing_depth (tests.data_generation.TestGenerationData) ... ok
test_create_data_increasing_depth (tests.data_generation.TestGenerationData) ... ok

----------------------------------------------------------------------
Ran 10 tests in 10.419s
```
## mem and CPU test
```
# uncomment @profile decorator in funcs.py
```
#### add memory profiling plot
```
$ mprof run funcs.py
```
creates [result](mprofile_20190827164514.dat)
```
$ mprof plot
```
see and save [memory_test.png](memory_test.png)

#### add CPU profiling data
```
$ kernprof -l funcs.py
```
Wrote profile results to [funcs.py.lprof](funcs.py.lprof)
```
$ python -m line_profiler funcs.py.lprof
Timer unit: 1e-06 s

Total time: 1.7e-05 s
File: funcs.py
Function: outer_flatten_1 at line 11

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    11                                           @profile
    12                                           def outer_flatten_1(array: Iterable) -> List:
    13                                               """
    14                                               Based on C realization of this solution
    15                                               More on:
    16
    17                                               https://iteration-utilities.readthedocs.io/en/latest/generated/deepflatten.html
    18
    19                                               https://github.com/MSeifert04/iteration_utilities/blob/384948b4e82e41de47fa79fb73efc56c08549b01/src/deepflatten.c
    20                                               """
    21         2         17.0      8.5    100.0      return deepflatten(array)

Total time: 3.3e-05 s
File: funcs.py
Function: outer_flatten_2 at line 24

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    24                                           @profile
    25                                           def outer_flatten_2(array: Iterable) -> List:
    26                                               """
    27                                               recursive algorithm, vaguely reminiscent of recursion_flatten. Based on next pattern:
    28
    29                                               .. code:: python
    30
    31                                                   try:
    32                                                       tree = iter(node)
    33                                                   except TypeError:
    34                                                       yield node
    35
    36                                               more on:
    37                                               https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.collapse
    38                                               """
    39         2         33.0     16.5    100.0      return collapse(array)

Total time: 0.105099 s
File: funcs.py
Function: niccolum_flatten at line 42

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    42                                           @profile
    43                                           def niccolum_flatten(array: Iterable) -> List:
    44                                               """
    45                                               Non recursive algorithm
    46                                               Based on pop/insert elements in current list
    47                                               """
    48
    49         2         39.0     19.5      0.0      new_array = array[:]
    50         2          6.0      3.0      0.0      ind = 0
    51         2          2.0      1.0      0.0      while True:
    52     20002       7778.0      0.4      7.4          try:
    53     21010      13528.0      0.6     12.9              while isinstance(new_array[ind], list):
    54      1008       1520.0      1.5      1.4                  item = new_array.pop(ind)
    55     21014      13423.0      0.6     12.8                  for inner_item in reversed(item):
    56     20006      59375.0      3.0     56.5                      new_array.insert(ind, inner_item)
    57     20000       9423.0      0.5      9.0              ind += 1
    58         2          2.0      1.0      0.0          except IndexError:
    59         2          2.0      1.0      0.0              break
    60         2          1.0      0.5      0.0      return new_array

Total time: 0.137481 s
File: funcs.py
Function: tishka_flatten at line 63

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    63                                           @profile
    64                                           def tishka_flatten(data: Iterable) -> List:
    65                                               """
    66                                               Non recursive algorithm
    67                                               Based on append/extend elements to new list
    68
    69                                               """
    70         2         17.0      8.5      0.0      nested = True
    71      1012       1044.0      1.0      0.8      while nested:
    72      1010       1063.0      1.1      0.8          new = []
    73      1010        992.0      1.0      0.7          nested = False
    74    112018      38090.0      0.3     27.7          for i in data:
    75    111008      50247.0      0.5     36.5              if isinstance(i, list):
    76      1008       1431.0      1.4      1.0                  new.extend(i)
    77      1008       1138.0      1.1      0.8                  nested = True
    78                                                       else:
    79    110000      42052.0      0.4     30.6                  new.append(i)
    80      1010       1406.0      1.4      1.0          data = new
    81         2          1.0      0.5      0.0      return data

Total time: 0.062931 s
File: funcs.py
Function: zart_flatten at line 84

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    84                                           @profile
    85                                           def zart_flatten(a: Iterable) -> List:
    86                                               """
    87                                               Non recursive algorithm
    88                                               Based on pop from old and append elements to new list
    89                                               """
    90         2         20.0     10.0      0.0      queue, out = [a], []
    91     21012      12866.0      0.6     20.4      while queue:
    92     21010      16849.0      0.8     26.8          elem = queue.pop(-1)
    93     21010      17768.0      0.8     28.2          if isinstance(elem, list):
    94      1010       1562.0      1.5      2.5              queue.extend(elem)
    95                                                   else:
    96     20000      13813.0      0.7     21.9              out.append(elem)
    97         2         53.0     26.5      0.1      return out[::-1]

Total time: 0.052754 s
File: funcs.py
Function: recursive_flatten_generator at line 100

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   100                                           @profile
   101                                           def recursive_flatten_generator(array: Iterable) -> List:
   102                                               """
   103                                               Recursive algorithm
   104                                               Looks like recursive_flatten_iterator, but with extend/append
   105
   106                                               """
   107      1010       1569.0      1.6      3.0      lst = []
   108     22018      13565.0      0.6     25.7      for i in array:
   109     21008      17060.0      0.8     32.3          if isinstance(i, list):
   110      1008       6624.0      6.6     12.6              lst.extend(recursive_flatten_generator(i))
   111                                                   else:
   112     20000      13622.0      0.7     25.8              lst.append(i)
   113      1010        314.0      0.3      0.6      return lst

Total time: 0.054103 s
File: funcs.py
Function: recursive_flatten_iterator at line 116

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   116                                           @profile
   117                                           def recursive_flatten_iterator(arr: Iterable) -> Iterator:
   118                                               """
   119                                               Recursive algorithm based on iterator
   120                                               Usual solution to this problem
   121
   122                                               """
   123
   124     22018      20200.0      0.9     37.3      for i in arr:
   125     21008      19363.0      0.9     35.8          if isinstance(i, list):
   126      1008       6856.0      6.8     12.7              yield from recursive_flatten_iterator(i)
   127                                                   else:
   128     20000       7684.0      0.4     14.2              yield i

Total time: 0.056111 s
File: funcs.py
Function: tishka_flatten_with_stack at line 131

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   131                                           @profile
   132                                           def tishka_flatten_with_stack(seq: Iterable) -> List:
   133                                               """
   134                                               Non recursive algorithm
   135                                               Based on zart_flatten, but build on try/except pattern
   136                                               """
   137         2         24.0     12.0      0.0      stack = [iter(seq)]
   138         2          5.0      2.5      0.0      new = []
   139      1012        357.0      0.4      0.6      while stack:
   140      1010        435.0      0.4      0.8          i = stack.pop()
   141      1010        328.0      0.3      0.6          try:
   142      1010        330.0      0.3      0.6              while True:
   143     22018      17272.0      0.8     30.8                  data = next(i)
   144     21008      18951.0      0.9     33.8                  if isinstance(data, list):
   145      1008        997.0      1.0      1.8                      stack.append(i)
   146      1008       1205.0      1.2      2.1                      i = iter(data)
   147                                                           else:
   148     20000      15413.0      0.8     27.5                      new.append(data)
   149      1010        425.0      0.4      0.8          except StopIteration:
   150      1010        368.0      0.4      0.7              pass
   151         2          1.0      0.5      0.0      return new
```

```
# comment @profile decorator in funcs.py
```

## create json file of performance result

```
$ python performance.py
```
creates [performance.json](performance.json) for plot

## obviously - make performance plot

```
$ python make_performance_plot.py
```

create and show [common plot](result.png) and [more accurate plot](result2.png), based on performance.json
