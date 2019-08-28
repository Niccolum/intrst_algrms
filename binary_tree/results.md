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

$ cd ~/binary_tree
```
## run tests
```
$ python tests.py -vv
test_data_SingleNodeClass (__main__.TestNodes) ... ok
test_data_TwoNodeClass (__main__.TestNodes) ... ok

----------------------------------------------------------------------
Ran 2 tests in 34.623s

OK
```
## mem and CPU test
```
# uncomment @profile decorator in funcs.py
```
#### add memory profiling plot
```
$ mprof run funcs.py
```
creates [result](mprofile_20190819154402.dat)
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

Total time: 5.9e-05 s
File: funcs.py
Function: add_node at line 33

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    33                                               @profile
    34                                               def add_node(self, data: Integral) -> None:
    35       100         59.0      0.6    100.0          bisect.insort(self.data, data)

Total time: 1e-06 s
File: funcs.py
Function: tree_data at line 37

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    37                                               @profile
    38                                               def tree_data(self) -> Iterator:
    39         1          1.0      1.0    100.0          yield from self.data

Total time: 0.001165 s
File: funcs.py
Function: add_node at line 49

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    49                                               @profile
    50                                               def add_node(self, data: Integral) -> None:
    51       691        176.0      0.3     15.1          if self.data is not None:
    52       690        180.0      0.3     15.5              if data < self.data:
    53       297         82.0      0.3      7.0                  if self.left is None:
    54        49         43.0      0.9      3.7                      self.left = SingleNodeClass(data)
    55                                                           else:
    56       248        175.0      0.7     15.0                      self.left.add_node(data)
    57       393        108.0      0.3      9.3              elif data > self.data:
    58       393         98.0      0.2      8.4                  if self.right is None:
    59        50         47.0      0.9      4.0                      self.right = SingleNodeClass(data)
    60                                                           else:
    61       343        256.0      0.7     22.0                      self.right.add_node(data)
    62                                                   else:
    63         1          0.0      0.0      0.0              self.data = data

Total time: 0.000187 s
File: funcs.py
Function: tree_data at line 65

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    65                                               @profile
    66                                               def tree_data(self) -> Iterator:
    67       100         27.0      0.3     14.4          if self.left:
    68        49         53.0      1.1     28.3              yield from self.left.tree_data()
    69       100         24.0      0.2     12.8          yield self.data
    70       100         28.0      0.3     15.0          if self.right:
    71        50         55.0      1.1     29.4              yield from self.right.tree_data()

Total time: 0.009317 s
File: funcs.py
Function: add_node at line 88

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    88                                               @profile
    89                                               def add_node(self, key: Integral, node: Node = None) -> None:
    90                                           
    91       691       1162.0      1.7     12.5          if node is None:
    92       100        177.0      1.8      1.9              node = self.root
    93                                           
    94       691       1253.0      1.8     13.4          if self.root is None:
    95         1         14.0     14.0      0.2              self.root = self.Node(key)
    96                                           
    97                                                   else:
    98       690       1283.0      1.9     13.8              if key <= node.key:
    99       297        550.0      1.9      5.9                  if node.left is None:
   100        49        372.0      7.6      4.0                      node.left = self.Node(key)
   101        49        101.0      2.1      1.1                      node.left.parent = node
   102        49         66.0      1.3      0.7                      return
   103                                                           else:
   104       248       1376.0      5.5     14.8                      return self.add_node(key, node=node.left)
   105                                                       else:
   106       393        663.0      1.7      7.1                  if node.right is None:
   107        50        319.0      6.4      3.4                      node.right = self.Node(key)
   108        50         84.0      1.7      0.9                      node.right.parent = node
   109        50         73.0      1.5      0.8                      return
   110                                                           else:
   111       343       1824.0      5.3     19.6                      return self.add_node(key, node=node.right)

Total time: 0.000772 s
File: funcs.py
Function: tree_data at line 113

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   113                                               @profile
   114                                               def tree_data(self, node: Node = None) -> Iterator:
   115         1          1.0      1.0      0.1          if node is None:
   116         1          1.0      1.0      0.1              node = self.root
   117                                           
   118         1          2.0      2.0      0.3          stack = []
   119       201        129.0      0.6     16.7          while stack or node:
   120       200        189.0      0.9     24.5              if node is not None:
   121       100         95.0      0.9     12.3                  stack.append(node)
   122       100         86.0      0.9     11.1                  node = node.left
   123                                                       else:
   124       100        103.0      1.0     13.3                  node = stack.pop()
   125       100         80.0      0.8     10.4                  yield node.key
   126       100         86.0      0.9     11.1                  node = node.right


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
create and show [plot](result.png), based on performance.json

