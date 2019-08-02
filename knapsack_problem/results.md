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
$ python tests.py 
*************** TestKnapsackProblem1StaticData ***************
##### knapsack_1_solution #####
Knapsack with 5 items was completed in 0.000176 seconds
Knapsack with 5 items was completed in 0.000150 seconds
Knapsack with 22 items was completed in 0.004866 seconds
.##### knapsack_2_solution #####
Knapsack with 5 items was completed in 0.000081 seconds
Knapsack with 5 items was completed in 0.000097 seconds
Knapsack with 22 items was completed in 0.004316 seconds
.##### knapsack_3_solution #####
Knapsack with 5 items was completed in 0.000680 seconds
Knapsack with 5 items was completed in 0.000131 seconds
Knapsack with 22 items was completed in 0.004909 seconds
.##### knapsack_4_solution #####
Knapsack with 5 items was completed in 0.000566 seconds
Knapsack with 5 items was completed in 0.000074 seconds
Knapsack with 22 items was completed in 4.554347 seconds
.##### knapsack_5_solution #####
Knapsack with 5 items was completed in 0.000034 seconds
Knapsack with 5 items was completed in 0.000033 seconds
Knapsack with 22 items was completed in 0.002070 seconds
.##### knapsack_6_solution #####
Knapsack with 5 items was completed in 0.000071 seconds
Knapsack with 5 items was completed in 0.000053 seconds
Knapsack with 22 items was completed in 0.007740 seconds
.##### knapsack_greedy_solution #####
Knapsack with 5 items was completed in 0.000022 seconds
Knapsack with 5 items was completed in 0.000015 seconds
Knapsack with 22 items was completed in 0.000031 seconds
.*************** TestKnapsackProblem2DynamicData ***************
##### knapsack_1_solution #####
Knapsack with 10 items was completed in 0.000173 seconds
Knapsack with 14 items was completed in 0.000162 seconds
Knapsack with 18 items was completed in 0.000216 seconds
Knapsack with 22 items was completed in 0.000366 seconds
Knapsack with 26 items was completed in 0.000789 seconds
Knapsack with 30 items was completed in 0.000618 seconds
Knapsack with 34 items was completed in 0.000692 seconds
Knapsack with 38 items was completed in 0.000846 seconds
Knapsack with 42 items was completed in 0.001006 seconds
Knapsack with 46 items was completed in 0.001309 seconds
.##### knapsack_2_solution #####
Knapsack with 10 items was completed in 0.000037 seconds
Knapsack with 14 items was completed in 0.000051 seconds
Knapsack with 18 items was completed in 0.000080 seconds
Knapsack with 22 items was completed in 0.000110 seconds
Knapsack with 26 items was completed in 0.000153 seconds
Knapsack with 30 items was completed in 0.000202 seconds
Knapsack with 34 items was completed in 0.000254 seconds
Knapsack with 38 items was completed in 0.000327 seconds
Knapsack with 42 items was completed in 0.000389 seconds
Knapsack with 46 items was completed in 0.000453 seconds
.##### knapsack_3_solution #####
Knapsack with 10 items was completed in 0.000055 seconds
Knapsack with 14 items was completed in 0.000070 seconds
Knapsack with 18 items was completed in 0.000111 seconds
Knapsack with 22 items was completed in 0.000147 seconds
Knapsack with 26 items was completed in 0.000194 seconds
Knapsack with 30 items was completed in 0.000264 seconds
Knapsack with 34 items was completed in 0.000332 seconds
Knapsack with 38 items was completed in 0.000589 seconds
Knapsack with 42 items was completed in 0.000958 seconds
Knapsack with 46 items was completed in 0.001012 seconds
.##### knapsack_4_solution #####
Knapsack with 10 items was completed in 0.000674 seconds
Knapsack with 14 items was completed in 0.012272 seconds
Knapsack with 18 items was completed in 0.219250 seconds
Knapsack with 22 items was completed in 4.020011 seconds
Knapsack with 26 items was completed in 72.700317 seconds
Function knapsack_4_solution working too long
.##### knapsack_5_solution #####
Knapsack with 10 items was completed in 0.000041 seconds
Knapsack with 14 items was completed in 0.000059 seconds
Knapsack with 18 items was completed in 0.000091 seconds
Knapsack with 22 items was completed in 0.000123 seconds
Knapsack with 26 items was completed in 0.000171 seconds
Knapsack with 30 items was completed in 0.000225 seconds
Knapsack with 34 items was completed in 0.000279 seconds
Knapsack with 38 items was completed in 0.000346 seconds
Knapsack with 42 items was completed in 0.000430 seconds
Knapsack with 46 items was completed in 0.000535 seconds
.##### knapsack_6_solution #####
Knapsack with 10 items was completed in 0.000274 seconds
Knapsack with 14 items was completed in 0.000620 seconds
Knapsack with 18 items was completed in 0.001316 seconds
Knapsack with 22 items was completed in 0.003064 seconds
Knapsack with 26 items was completed in 0.004732 seconds
Knapsack with 30 items was completed in 0.007246 seconds
Knapsack with 34 items was completed in 0.008738 seconds
Knapsack with 38 items was completed in 0.015569 seconds
Knapsack with 42 items was completed in 0.016186 seconds
Knapsack with 46 items was completed in 0.032483 seconds
.##### knapsack_greedy_solution #####
Knapsack with 10 items was completed in 0.000026 seconds
Knapsack with 14 items was completed in 0.000012 seconds
Knapsack with 18 items was completed in 0.000023 seconds
Knapsack with 22 items was completed in 0.000016 seconds
Knapsack with 26 items was completed in 0.000016 seconds
Knapsack with 30 items was completed in 0.000017 seconds
Knapsack with 34 items was completed in 0.000019 seconds
Knapsack with 38 items was completed in 0.000021 seconds
Knapsack with 42 items was completed in 0.000037 seconds
Knapsack with 46 items was completed in 0.000039 seconds
.
----------------------------------------------------------------------
Ran 14 tests in 81.645s

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
