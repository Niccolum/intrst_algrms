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

Total time: 53.9418 s
File: funcs.py
Function: add_node at line 35

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    35                                               @profile
    36                                               def add_node(self, data: Integral) -> None:
    37  25544561    9622062.0      0.4     17.8          if self.data is not None:
    38  25544560    7273561.0      0.3     13.5              if data < self.data:
    39  12422749    4050492.0      0.3      7.5                  if self.left is None:
    40    500178    2012613.0      4.0      3.7                      self.left = SingleNodeClass(data)
    41                                                           else:
    42  11922571   10527388.0      0.9     19.5                      self.left.add_node(data)
    43  13121811    3750113.0      0.3      7.0              elif data > self.data:
    44  13121811    4252520.0      0.3      7.9                  if self.right is None:
    45    499821    1293489.0      2.6      2.4                      self.right = SingleNodeClass(data)
    46                                                           else:
    47  12621990   11159518.0      0.9     20.7                      self.right.add_node(data)
    48                                                   else:
    49         1          1.0      1.0      0.0              self.data = data

Total time: 2.32393 s
File: funcs.py
Function: tree_data at line 51

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    51                                               @profile
    52                                               def tree_data(self) -> Iterator:
    53   1000000     405404.0      0.4     17.4          if self.left:
    54    500178     565194.0      1.1     24.3              yield from self.left.tree_data()
    55   1000000     303625.0      0.3     13.1          yield self.data
    56   1000000     420314.0      0.4     18.1          if self.right:
    57    499821     629394.0      1.3     27.1              yield from self.right.tree_data()

Total time: 60.3506 s
File: funcs.py
Function: add_node at line 74

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    74                                               @profile
    75                                               def add_node(self, key: Integral, node: Node = None) -> None:
    76                                           
    77  25544561    7238977.0      0.3     12.0          if node is None:
    78   1000000     298427.0      0.3      0.5              node = self.root
    79                                           
    80  25544561    7145711.0      0.3     11.8          if self.root is None:
    81         1          9.0      9.0      0.0              self.root = self.Node(key)
    82                                           
    83                                                   else:
    84  25544560   11484225.0      0.4     19.0              if key <= node.key:
    85  12422749    4489340.0      0.4      7.4                  if node.left is None:
    86    500178     956148.0      1.9      1.6                      node.left = self.Node(key)
    87    500178     174555.0      0.3      0.3                      node.left.parent = node
    88    500178     126197.0      0.3      0.2                      return
    89                                                           else:
    90  11922571   11239458.0      0.9     18.6                      return self.add_node(key, node=node.left)
    91                                                       else:
    92  13121811    4698574.0      0.4      7.8                  if node.right is None:
    93    499821     898488.0      1.8      1.5                      node.right = self.Node(key)
    94    499821     170032.0      0.3      0.3                      node.right.parent = node
    95    499821     125574.0      0.3      0.2                      return
    96                                                           else:
    97  12621990   11304894.0      0.9     18.7                      return self.add_node(key, node=node.right)

Total time: 2.74602 s
File: funcs.py
Function: tree_data at line 99

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    99                                               @profile
   100                                               def tree_data(self, node: Node = None) -> Iterator:
   101         1          0.0      0.0      0.0          if node is None:
   102         1          1.0      1.0      0.0              node = self.root
   103                                           
   104         1          0.0      0.0      0.0          stack = []
   105   2000001     485865.0      0.2     17.7          while stack or node:
   106   2000000     510503.0      0.3     18.6              if node is not None:
   107   1000000     313939.0      0.3     11.4                  stack.append(node)
   108   1000000     496807.0      0.5     18.1                  node = node.left
   109                                                       else:
   110   1000000     319196.0      0.3     11.6                  node = stack.pop()
   111   1000000     282000.0      0.3     10.3                  yield node.key
   112   1000000     337708.0      0.3     12.3                  node = node.right



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
