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

$ cd ~/knapsack_problem
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

## mem and CPU test
```
# uncomment @profile decorator in funcs.py
```
#### add memory profiling plot
```
$ mprof run funcs.py
```
creates [result](mprofile_20190819094003.dat)
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

Total time: 3e-06 s
File: funcs.py
Function: knapsack_1_standard_solution at line 18

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    18                                           @profile
    19                                           def knapsack_1_standard_solution(items: Tuple[Item], weight_limit: int) -> Item:
    20                                               """
    21                                               https://codereview.stackexchange.com/a/20581
    22                                           
    23                                               Solve the knapsack problem by finding the most valuable subsequence
    24                                               of items that weighs no more than weight_limit.
    25                                           
    26                                               items must be a sequence of pairs (value, weight), where value is a
    27                                               number and weight is a non-negative integer.
    28                                           
    29                                               weight_limit is a non-negative integer.
    30                                           
    31                                               Return a pair whose first element is the sum of values in the most
    32                                               valuable subsequence, and whose second element is the subsequence.
    33                                               """
    34         3          3.0      1.0    100.0      return knapsack_standard_solution(items, weight_limit)

Total time: 0.01259 s
File: funcs.py
Function: knapsack_2_solution at line 37

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    37                                           @profile
    38                                           def knapsack_2_solution(items: Tuple[Item], weight_limit: int) -> Item:
    39                                               """
    40                                               my own function, written thanks to the site:
    41                                               https://foxford.ru/wiki/informatika/algoritm-ukladki-ryukzaka
    42                                               """
    43         3          2.0      0.7      0.0      w = weight_limit
    44         3         26.0      8.7      0.2      f = [[0] * (w + 1) for i in range(len(items) + 1)]
    45        35         12.0      0.3      0.1      for i in range(len(items)):
    46        32         19.0      0.6      0.2          weight = items[i].weight
    47        32         19.0      0.6      0.2          value = items[i].value
    48      8937       3430.0      0.4     27.2          for j in range(1, w + 1):
    49      8905       3394.0      0.4     27.0              if j >= weight:
    50      7636       5050.0      0.7     40.1                  f[i][j] = max(f[i - 1][j], f[i - 1][j - weight] + value)
    51                                                       else:
    52      1269        590.0      0.5      4.7                  f[i][j] = f[i - 1][j]
    53                                           
    54        35         20.0      0.6      0.2      for k in reversed(range(len(items))):
    55        32         15.0      0.5      0.1          if f[k][w] != f[k - 1][w]:
    56        16          4.0      0.2      0.0              yield items[k]
    57        16          9.0      0.6      0.1              w -= items[k].weight

Total time: 0.028563 s
File: funcs.py
Function: knapsack_3_solution at line 60

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    60                                           @profile
    61                                           def knapsack_3_solution(items: Tuple[Item], weight_limit: int) -> Item:
    62                                               """
    63                                               Given a list of items with name, value and weight.
    64                                               Return the optimal value with total weight <= allowed weight and
    65                                               list of picked items.
    66                                               https://codereview.stackexchange.com/a/125386
    67                                               """
    68                                           
    69                                               # find which item are picked
    70         3        412.0    137.3      1.4      def fetch_items(k: List[List[int]], weight_limit: int, items: Tuple[Item]):
    71                                                   for item, weights_p, weights_n in zip(items[::-1], k[-2::-1], k[::-1]):
    72                                                       if weights_n[weight_limit] != weights_p[weight_limit]:
    73                                                           yield item
    74                                                           weight_limit -= item.weight
    75                                           
    76                                               k = [
    77         3          3.0      1.0      0.0          [0] * (weight_limit + 1)
    78         3         23.0      7.7      0.1          for x in range(len(items) + 1)
    79                                               ]
    80        35         40.0      1.1      0.1      for next_idx, (item, weights) in enumerate(zip(items, k), 1):
    81      8937       5646.0      0.6     19.8          for w, current_weight in enumerate(weights[1:], 1):
    82      8905       5607.0      0.6     19.6              if item.weight <= w:
    83      7636       4636.0      0.6     16.2                  k[next_idx][w] = max(
    84      7636       5392.0      0.7     18.9                      item.value + weights[w - item.weight],
    85      7636       6040.0      0.8     21.1                      current_weight
    86                                                           )
    87                                                       else:
    88      1269        760.0      0.6      2.7                  k[next_idx][w] = current_weight
    89                                           
    90         3          4.0      1.3      0.0      return fetch_items(k, weight_limit, items)

Total time: 19.0995 s
File: funcs.py
Function: knapsack_4_bruteforce_solution at line 93

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    93                                           @profile
    94                                           def knapsack_4_bruteforce_solution(items: Tuple[Item], weight_limit: int) -> Union[Item, List[None]]:
    95                                               """
    96                                               Brute force algorithm
    97                                               http://rosettacode.org/mw/index.php?title=Knapsack_problem/0-1&action=edit&section=62
    98                                               """
    99                                           
   100         3         15.0      5.0      0.0      def any_comb(items: Tuple[Item]) -> Generator:
   101                                                   """return combinations of any length from the items"""
   102                                                   return (comb
   103                                                           for r in range(1, len(items) + 1)
   104                                                           for comb in combinations(items, r)
   105                                                           )
   106                                           
   107         3        204.0     68.0      0.0      def total_value(comb: Tuple[Any]) -> Tuple[int, int]:
   108                                                   """Totalise a particular combination of items"""
   109                                                   totwt = totval = 0
   110                                                   for item, val, wt in comb:
   111                                                       totwt += wt
   112                                                       totval += val
   113                                                   return (totval, -totwt) if totwt <= weight_limit else (0, 0)
   114                                           
   115         3   19099285.0 6366428.3    100.0      bagged = max(any_comb(items), key=total_value)  # max val or min wt if values equal
   116         3          6.0      2.0      0.0      if bagged[0].weight <= weight_limit:
   117         3          3.0      1.0      0.0          return bagged
   118                                               return []

Total time: 0.015072 s
File: funcs.py
Function: knapsack_5_dynamic_solution at line 121

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   121                                           @profile
   122                                           def knapsack_5_dynamic_solution(items: Tuple[Item], weight_limit: int) -> Item:
   123                                               """
   124                                               Dynamic programming solution
   125                                               http://rosettacode.org/mw/index.php?title=Knapsack_problem/0-1&action=edit&section=63
   126                                               """
   127                                           
   128         3         27.0      9.0      0.2      table = [[0] * (weight_limit + 1) for j in range(len(items) + 1)]
   129                                           
   130        35         15.0      0.4      0.1      for j in range(1, len(items) + 1):
   131        32         16.0      0.5      0.1          item, val, wt = items[j - 1]
   132      8937       3302.0      0.4     21.9          for w in range(1, weight_limit + 1):
   133      8905       3354.0      0.4     22.3              if wt > w:
   134      1269        555.0      0.4      3.7                  table[j][w] = table[j - 1][w]
   135                                                       else:
   136      7636       3242.0      0.4     21.5                  table[j][w] = max(table[j - 1][w],
   137      7636       4493.0      0.6     29.8                                    table[j - 1][w - wt] + val)
   138                                           
   139         3          3.0      1.0      0.0      w = weight_limit
   140        35         15.0      0.4      0.1      for j in range(len(items), 0, -1):
   141        32         15.0      0.5      0.1          was_added = table[j][w] != table[j - 1][w]
   142        32         12.0      0.4      0.1          if was_added:
   143        16         10.0      0.6      0.1              item, val, wt = items[j - 1]
   144        16          8.0      0.5      0.1              yield items[j - 1]
   145        16          5.0      0.3      0.0              w -= wt

Total time: 0.018763 s
File: funcs.py
Function: knapsack_6_recursive_dynamic_solution at line 148

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   148                                           @profile
   149                                           def knapsack_6_recursive_dynamic_solution(items: Tuple[Item], weight_limit: int) -> Tuple[Item]:
   150                                               """
   151                                               Recursive dynamic programming algorithm
   152                                               http://rosettacode.org/mw/index.php?title=Knapsack_problem/0-1&action=edit&section=64
   153                                               """
   154                                           
   155         3         15.0      5.0      0.1      def total_value(items: Tuple[Item], weight_limit: int) -> int:
   156                                                   return sum([x.value for x in items]) if sum([x.weight for x in items]) <= weight_limit else 0
   157                                           
   158         3          3.0      1.0      0.0      cache = {}
   159                                           
   160         3          5.0      1.7      0.0      def solve(items: Tuple[Item], weight_limit: int) -> Tuple:
   161                                                   if not items:
   162                                                       return ()
   163                                                   if (items, weight_limit) not in cache:
   164                                                       head = items[0]
   165                                                       tail = items[1:]
   166                                                       include = (head,) + solve(tail, weight_limit - head[2])
   167                                                       dont_include = solve(tail, weight_limit)
   168                                                       if total_value(include, weight_limit) > total_value(dont_include, weight_limit):
   169                                                           answer = include
   170                                                       else:
   171                                                           answer = dont_include
   172                                                       cache[(items, weight_limit)] = answer
   173                                                   return cache[(items, weight_limit)]
   174                                           
   175         3      18740.0   6246.7     99.9      return solve(items, weight_limit)

Total time: 4.1e-05 s
File: funcs.py
Function: knapsack_greedy_solution at line 178

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   178                                           @profile
   179                                           def knapsack_greedy_solution(items: Tuple[Item], weight_limit: int) -> Iterator:
   180                                               """
   181                                               Return a list of items with the maximum value, subject to the
   182                                               constraint that their combined weight must not exceed max_weight.
   183                                               Implements the well-known "greedy approximation algorithm" for the knapsack problem
   184                                               (first described by George Dantzig in 1957).
   185                                               https://codereview.stackexchange.com/a/62871
   186                                               """
   187                                           
   188         3          3.0      1.0      7.3      def efficiency(item: Item) -> float:
   189                                                   """Return efficiency of item (its value per unit weight)."""
   190                                                   return float(item.value) / float(item.weight)
   191                                           
   192         3          4.0      1.3      9.8      def pack(item: Item) -> bool:
   193                                                   # Attempt to pack item; return True if successful.
   194                                                   if item.weight <= pack.max_weight:
   195                                                       pack.max_weight -= item.weight
   196                                                       return True
   197                                                   else:
   198                                                       return False
   199                                           
   200         3          4.0      1.3      9.8      pack.max_weight = weight_limit
   201         3         30.0     10.0     73.2      return filter(pack, sorted(items, key=efficiency, reverse=True))

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