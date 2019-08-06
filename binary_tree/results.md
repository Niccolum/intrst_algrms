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
$ cd ~/binary_tree

$ source env/bin/activate

$ python -V
Python 3.7.3

$ pip install -r requirements.txt
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
## add memory profiling plots
```
$ cd logs && python ../profiling.py

... # create plots and logs for profiling in logs dir
```
## add CPU profiling plots
```
$ cd ../
# uncomment @profile decorator in funcs.py

$ kernprof -l funcs.py
Wrote profile results to funcs.py.lprof

$ python -m line_profiler funcs.py.lprof 
Timer unit: 1e-06 s

Total time: 1.74942 s
File: funcs.py
Function: add_node at line 33

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    33                                               @profile
    34                                               def add_node(self, data: Integral) -> None:
    35    100000    1749417.0     17.5    100.0          bisect.insort(self.data, data)

Total time: 1e-06 s
File: funcs.py
Function: tree_data at line 37

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    37                                               @profile
    38                                               def tree_data(self) -> Iterator:
    39         1          1.0      1.0    100.0          yield from self.data

Total time: 3.64878 s
File: funcs.py
Function: add_node at line 49

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    49                                               @profile
    50                                               def add_node(self, data: Integral) -> None:
    51   1926140     607824.0      0.3     16.7          if self.data is not None:
    52   1926139     523653.0      0.3     14.4              if data < self.data:
    53   1001036     284169.0      0.3      7.8                  if self.left is None:
    54     49865      84578.0      1.7      2.3                      self.left = SingleNodeClass(data)
    55                                                           else:
    56    951171     791230.0      0.8     21.7                      self.left.add_node(data)
    57    925103     252249.0      0.3      6.9              elif data > self.data:
    58    925103     267906.0      0.3      7.3                  if self.right is None:
    59     50134     120011.0      2.4      3.3                      self.right = SingleNodeClass(data)
    60                                                           else:
    61    874969     717162.0      0.8     19.7                      self.right.add_node(data)
    62                                                   else:
    63         1          1.0      1.0      0.0              self.data = data

Total time: 0.223213 s
File: funcs.py
Function: tree_data at line 65

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    65                                               @profile
    66                                               def tree_data(self) -> Iterator:
    67    100000      37258.0      0.4     16.7          if self.left:
    68     49865      54765.0      1.1     24.5              yield from self.left.tree_data()
    69    100000      30394.0      0.3     13.6          yield self.data
    70    100000      39131.0      0.4     17.5          if self.right:
    71     50134      61665.0      1.2     27.6              yield from self.right.tree_data()

Total time: 4.7792 s
File: funcs.py
Function: add_node at line 88

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    88                                               @profile
    89                                               def add_node(self, key: Integral, node: Node = None) -> None:
    90                                           
    91   1926140     573057.0      0.3     12.0          if node is None:
    92    100000      31931.0      0.3      0.7              node = self.root
    93                                           
    94   1926140     584570.0      0.3     12.2          if self.root is None:
    95         1          8.0      8.0      0.0              self.root = self.Node(key)
    96                                           
    97                                                   else:
    98   1926139     866050.0      0.4     18.1              if key <= node.key:
    99   1001036     354463.0      0.4      7.4                  if node.left is None:
   100     49865     124374.0      2.5      2.6                      node.left = self.Node(key)
   101     49865      18192.0      0.4      0.4                      node.left.parent = node
   102     49865      13259.0      0.3      0.3                      return
   103                                                           else:
   104    951171     944841.0      1.0     19.8                      return self.add_node(key, node=node.left)
   105                                                       else:
   106    925103     338364.0      0.4      7.1                  if node.right is None:
   107     50134      81167.0      1.6      1.7                      node.right = self.Node(key)
   108     50134      18637.0      0.4      0.4                      node.right.parent = node
   109     50134      13564.0      0.3      0.3                      return
   110                                                           else:
   111    874969     816724.0      0.9     17.1                      return self.add_node(key, node=node.right)

Total time: 0.375843 s
File: funcs.py
Function: tree_data at line 113

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   113                                               @profile
   114                                               def tree_data(self, node: Node = None) -> Iterator:
   115         1          1.0      1.0      0.0          if node is None:
   116         1          0.0      0.0      0.0              node = self.root
   117                                           
   118         1          1.0      1.0      0.0          stack = []
   119    200001      67582.0      0.3     18.0          while stack or node:
   120    200000      68945.0      0.3     18.3              if node is not None:
   121    100000      43771.0      0.4     11.6                  stack.append(node)
   122    100000      61825.0      0.6     16.4                  node = node.left
   123                                                       else:
   124    100000      46715.0      0.5     12.4                  node = stack.pop()
   125    100000      40069.0      0.4     10.7                  yield node.key
   126    100000      46934.0      0.5     12.5                  node = node.right



```
## create json file of performance result
```
$ python performance.py

... # creates performance.json for plot
```
## obviously - make performance plot
```
$ python make_performance_plot.py

... # create and show plot, based on performance.json
```
