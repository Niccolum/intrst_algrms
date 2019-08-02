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
*************** TestKnapsackProblem1StaticData ***************
test_knapsack_1_solution (__main__.TestKnapsackProblem1StaticData) ... ok
test_knapsack_2_solution (__main__.TestKnapsackProblem1StaticData) ... ok
test_knapsack_3_solution (__main__.TestKnapsackProblem1StaticData) ... ok
test_knapsack_4_solution (__main__.TestKnapsackProblem1StaticData) ... ok
test_knapsack_5_solution (__main__.TestKnapsackProblem1StaticData) ... ok
test_knapsack_6_solution (__main__.TestKnapsackProblem1StaticData) ... ok
*************** TestKnapsackProblem2DynamicData ***************
test_knapsack_1_solution (__main__.TestKnapsackProblem2DynamicData) ... 
Knapsack with 10 items was completed in 0.000135 seconds
Knapsack with 14 items was completed in 0.000116 seconds
Knapsack with 18 items was completed in 0.000167 seconds
Knapsack with 22 items was completed in 0.000280 seconds
Knapsack with 26 items was completed in 0.000357 seconds
Knapsack with 30 items was completed in 0.000552 seconds
Knapsack with 34 items was completed in 0.000652 seconds
Knapsack with 38 items was completed in 0.000832 seconds
Knapsack with 42 items was completed in 0.001336 seconds
Knapsack with 46 items was completed in 0.001124 seconds
ok
test_knapsack_2_solution (__main__.TestKnapsackProblem2DynamicData) ... 
Knapsack with 10 items was completed in 0.000036 seconds
Knapsack with 14 items was completed in 0.000055 seconds
Knapsack with 18 items was completed in 0.000083 seconds
Knapsack with 22 items was completed in 0.000120 seconds
Knapsack with 26 items was completed in 0.000160 seconds
Knapsack with 30 items was completed in 0.000218 seconds
Knapsack with 34 items was completed in 0.000276 seconds
Knapsack with 38 items was completed in 0.000356 seconds
Knapsack with 42 items was completed in 0.000388 seconds
Knapsack with 46 items was completed in 0.000490 seconds
ok
test_knapsack_3_solution (__main__.TestKnapsackProblem2DynamicData) ... 
Knapsack with 10 items was completed in 0.000054 seconds
Knapsack with 14 items was completed in 0.000071 seconds
Knapsack with 18 items was completed in 0.000115 seconds
Knapsack with 22 items was completed in 0.000151 seconds
Knapsack with 26 items was completed in 0.000197 seconds
Knapsack with 30 items was completed in 0.000264 seconds
Knapsack with 34 items was completed in 0.000383 seconds
Knapsack with 38 items was completed in 0.000425 seconds
Knapsack with 42 items was completed in 0.000518 seconds
Knapsack with 46 items was completed in 0.000950 seconds
ok
test_knapsack_4_solution (__main__.TestKnapsackProblem2DynamicData) ... 
Knapsack with 10 items was completed in 0.001076 seconds
Knapsack with 14 items was completed in 0.011666 seconds
Knapsack with 18 items was completed in 0.209452 seconds
Knapsack with 22 items was completed in 4.249598 seconds
Knapsack with 26 items was completed in 73.873633 seconds
Function knapsack_4_solution working too long
ok
test_knapsack_5_solution (__main__.TestKnapsackProblem2DynamicData) ... 
Knapsack with 10 items was completed in 0.000041 seconds
Knapsack with 14 items was completed in 0.000061 seconds
Knapsack with 18 items was completed in 0.000089 seconds
Knapsack with 22 items was completed in 0.000131 seconds
Knapsack with 26 items was completed in 0.000168 seconds
Knapsack with 30 items was completed in 0.000235 seconds
Knapsack with 34 items was completed in 0.000285 seconds
Knapsack with 38 items was completed in 0.000357 seconds
Knapsack with 42 items was completed in 0.000431 seconds
Knapsack with 46 items was completed in 0.000506 seconds
ok
test_knapsack_6_solution (__main__.TestKnapsackProblem2DynamicData) ... 
Knapsack with 10 items was completed in 0.000288 seconds
Knapsack with 14 items was completed in 0.000676 seconds
Knapsack with 18 items was completed in 0.001300 seconds
Knapsack with 22 items was completed in 0.002478 seconds
Knapsack with 26 items was completed in 0.004910 seconds
Knapsack with 30 items was completed in 0.006547 seconds
Knapsack with 34 items was completed in 0.009097 seconds
Knapsack with 38 items was completed in 0.012221 seconds
Knapsack with 42 items was completed in 0.016448 seconds
Knapsack with 46 items was completed in 0.032734 seconds
ok

----------------------------------------------------------------------
Ran 12 tests in 83.078s

OK

```
## add profiling plots
```
$ cd logs && python ../profiling.py

... # create plots and logs for profiling in logs dir
```
## create json file of performance result
```
$ cd ../ && python performance.py

... # creates performance.json for plot
```
## obviously - make performance plot
```
$ python make_performance_plot.py

... # create and show plot, based on performance.json
```
