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
$ cd ~/unpacking_flatten_lists

$ source env/bin/activate

$ python -V
Python 3.7.3

$ pip install -r requirements.txt
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
## add CPU profiling plots
```
$ cd ../
# uncomment @profile decorator in funcs.py

$ kernprof -l funcs.py
Wrote profile results to funcs.py.lprof

$ python -m line_profiler funcs.py.lprof
```
# add profiling plots
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

... # * create and show plot, based on performance.json *
```