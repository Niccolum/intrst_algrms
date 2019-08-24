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
test_recursion_flatten (tests.flatten_funcs.TestFlattenFunctions) ... 2.59538s
ok
test_recursive_flatten_like_tishka (tests.flatten_funcs.TestFlattenFunctions) ... 0.54907s
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
creates [result](mprofile_20190819093315.dat)
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

Total time: 0.004034 s
File: funcs.py
Function: niccolum_flatten at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           @profile
     8                                           def niccolum_flatten(array: Iterable) -> List:
     9                                               """
    10                                               Non recursive algorithm
    11                                               Based on pop/insert elements in current list
    12                                               """
    13                                           
    14         2          6.0      3.0      0.1      new_array = array[:]
    15         2          0.0      0.0      0.0      ind = 0
    16         2          1.0      0.5      0.0      while True:
    17      2002        580.0      0.3     14.4          try:
    18      2110        938.0      0.4     23.3              while isinstance(new_array[ind], list):
    19       108         42.0      0.4      1.0                  item = new_array.pop(ind)
    20      2114        682.0      0.3     16.9                  for inner_item in reversed(item):
    21      2006       1150.0      0.6     28.5                      new_array.insert(ind, inner_item)
    22      2000        633.0      0.3     15.7              ind += 1
    23         2          2.0      1.0      0.0          except IndexError:
    24         2          0.0      0.0      0.0              break
    25         2          0.0      0.0      0.0      return new_array

Total time: 0.00983 s
File: funcs.py
Function: tishka_flatten at line 28

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    28                                           @profile
    29                                           def tishka_flatten(data: Iterable) -> List:
    30                                               """
    31                                               Non recursive algorithm
    32                                               Based on append/extend elements to new list
    33                                           
    34                                               """
    35         2          1.0      0.5      0.0      nested = True
    36       112         27.0      0.2      0.3      while nested:
    37       110         22.0      0.2      0.2          new = []
    38       110         25.0      0.2      0.3          nested = False
    39     11218       2726.0      0.2     27.7          for i in data:
    40     11108       3693.0      0.3     37.6              if isinstance(i, list):
    41       108         44.0      0.4      0.4                  new.extend(i)
    42       108         25.0      0.2      0.3                  nested = True
    43                                                       else:
    44     11000       3220.0      0.3     32.8                  new.append(i)
    45       110         46.0      0.4      0.5          data = new
    46         2          1.0      0.5      0.0      return data

Total time: 0.002676 s
File: funcs.py
Function: zart_flatten at line 49

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    49                                           @profile
    50                                           def zart_flatten(a: Iterable) -> List:
    51                                               """
    52                                               Non recursive algorithm
    53                                               Based on pop from old and append elements to new list
    54                                               """
    55         2          1.0      0.5      0.0      queue, out = [a], []
    56      2112        548.0      0.3     20.5      while queue:
    57      2110        729.0      0.3     27.2          elem = queue.pop(-1)
    58      2110        737.0      0.3     27.5          if isinstance(elem, list):
    59       110         46.0      0.4      1.7              queue.extend(elem)
    60                                                   else:
    61      2000        604.0      0.3     22.6              out.append(elem)
    62         2         11.0      5.5      0.4      return out[::-1]

Total time: 0.002074 s
File: funcs.py
Function: recursive_flatten_like_tishka at line 65

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    65                                           @profile
    66                                           def recursive_flatten_like_tishka(array: Iterable) -> List:
    67                                               """
    68                                               Recursive algorithm
    69                                               Based on tishka_flatten algorithm
    70                                           
    71                                               """
    72       110         34.0      0.3      1.6      lst = []
    73      2218        566.0      0.3     27.3      for i in array:
    74      2108        701.0      0.3     33.8          if isinstance(i, list):
    75       108        141.0      1.3      6.8              lst.extend(recursive_flatten_like_tishka(i))
    76                                                   else:
    77      2000        604.0      0.3     29.1              lst.append(i)
    78       110         28.0      0.3      1.4      return lst

Total time: 0.002318 s
File: funcs.py
Function: recursion_flatten at line 81

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    81                                           @profile
    82                                           def recursion_flatten(arr: Iterable) -> Iterator:
    83                                               """
    84                                               Recursive algorithm based on iterator
    85                                               Usual solution to this problem
    86                                           
    87                                               """
    88                                           
    89      2218        817.0      0.4     35.2      for i in arr:
    90      2108        862.0      0.4     37.2          if isinstance(i, list):
    91       108        153.0      1.4      6.6              yield from recursion_flatten(i)
    92                                                   else:
    93      2000        486.0      0.2     21.0              yield i

Total time: 0.003156 s
File: funcs.py
Function: tishka_flatten_with_stack at line 96

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    96                                           @profile
    97                                           def tishka_flatten_with_stack(seq: Iterable) -> List:
    98                                               """
    99                                               Non recursive algorithm
   100                                               Based on zart_flatten, but build on try/except pattern
   101                                               """
   102         2          2.0      1.0      0.1      stack = [iter(seq)]
   103         2          1.0      0.5      0.0      new = []
   104       112         54.0      0.5      1.7      while stack:
   105       110         56.0      0.5      1.8          i = stack.pop()
   106       110         42.0      0.4      1.3          try:
   107       110         43.0      0.4      1.4              while True:
   108      2218        956.0      0.4     30.3                  data = next(i)
   109      2108        976.0      0.5     30.9                  if isinstance(data, list):
   110       108         37.0      0.3      1.2                      stack.append(i)
   111       108         40.0      0.4      1.3                      i = iter(data)
   112                                                           else:
   113      2000        841.0      0.4     26.6                      new.append(data)
   114       110         57.0      0.5      1.8          except StopIteration:
   115       110         50.0      0.5      1.6              pass
   116         2          1.0      0.5      0.0      return new

Total time: 0.000283 s
File: funcs.py
Function: outer_flatten_1_profile at line 121

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   121                                               @profile
   122                                               def outer_flatten_1_profile(arr: Iterable) -> Iterator:
   123         2        283.0    141.5    100.0          return list(outer_flatten_1(arr))

Total time: 0.036295 s
File: funcs.py
Function: outer_flatten_2_profile at line 126

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   126                                               @profile
   127                                               def outer_flatten_2_profile(arr: Iterable) -> Iterator:
   128         2      36295.0  18147.5    100.0          return list(outer_flatten_2(arr))

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
