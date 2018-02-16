
'''
The code below was run in a Jupyter notebook on an i7 quad core windows PC 
with 16GB of RAM. 

The input file was 24 Gbytes in size with approx 335 Million records
'''

from itertools import islice
from collections import defaultdict


def get_chunk_of_lines(file, N):
    """
    Retrieves N lines from specified opened file.
    """
    return [x for x in islice(file, N)]


def collect_period_ids(lines):
    """
    Collects and groups period ID's from specified lines.
    """
    collected_period_ids = defaultdict(list)

    for line in lines:
        # current period ID  from second field
        field1_end = line.find('|') +1
        field2_end = line.find('|',field1_end)
        period_id = line[field1_end:field2_end]
        # appending current line to list of collected lines associated with
        # current period_id
        collected_period_ids[period_id].append(line)

    return collected_period_ids


def export_grouped_periods(periods):
    """
    Exports collected and grouped periods.
    """
    for period_id in periods:
# defining output file name according to period ID
        out_name = R"D:\tmp\iholding\period%s.txt" % period_id
        # opening output file and writing collected lines to it
        with open(out_name, 'a+') as f:
            f.write("".join(periods[period_id]))


def main():
    
 with open(R"D:\tmp\iholding\issueholding.txt") as period_src:

    chunk_cnt = 0

    while True:
        # retrieving 1000 input lines at a time
        line_chunk = get_chunk_of_lines(period_src, 1000000)

        # exiting while loop if no more chunk is left
        if not line_chunk:
            break

        chunk_cnt += 1
        print("+ Working on chunk %d" % chunk_cnt)
 
        # collecting, grouping and exporting period ID's
        periods = collect_period_ids(line_chunk)
        export_grouped_periods(periods)
        


%prun main()

```
Here is the output of the profiler


 1010556133 function calls in 1013.358 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      337  303.724    0.901  351.358    1.043 <ipython-input-3-dcdd1d6561df>:10(<listcomp>)
      336  207.544    0.618  338.705    1.008 <ipython-input-3-dcdd1d6561df>:13(collect_period_ids)
    18813  175.283    0.009  175.283    0.009 {built-in method _codecs.charmap_encode}
670042196  110.909    0.000  110.909    0.000 {method 'find' of 'str' objects}
    18813   59.522    0.003  234.902    0.012 {method 'write' of '_io.TextIOWrapper' objects}
  2636923   45.694    0.000   45.694    0.000 {built-in method _codecs.charmap_decode}
    18813   34.200    0.002   34.200    0.002 {method 'join' of 'str' objects}
        1   25.997   25.997 1013.341 1013.341 <ipython-input-3-dcdd1d6561df>:43(main)
335021098   20.251    0.000   20.251    0.000 {method 'append' of 'list' objects}
    18814   18.622    0.001   18.829    0.001 {built-in method io.open}
      336    9.270    0.028  297.200    0.885 <ipython-input-3-dcdd1d6561df>:31(export_grouped_periods)
  2636923    1.940    0.000   47.633    0.000 cp1252.py:22(decode)
    18814    0.130    0.000    0.130    0.000 {built-in method _locale._getdefaultlocale}
    18813    0.086    0.000  175.370    0.009 cp1252.py:18(encode)
     1008    0.052    0.000    0.062    0.000 iostream.py:195(schedule)
    18814    0.035    0.000    0.166    0.000 _bootlocale.py:11(getpreferredencoding)
    18813    0.019    0.000    0.019    0.000 codecs.py:185(__init__)
    18814    0.017    0.000    0.017    0.000 codecs.py:259(__init__)
        1    0.017    0.017 1013.358 1013.358 <string>:1(<module>)
    18813    0.010    0.000    0.010    0.000 codecs.py:275(reset)
      336    0.006    0.000    0.078    0.000 {built-in method builtins.print}
      672    0.006    0.000    0.072    0.000 iostream.py:366(write)
    18757    0.005    0.000    0.005    0.000 codecs.py:213(setstate)
     1008    0.003    0.000    0.007    0.000 threading.py:1104(is_alive)
     1008    0.002    0.000    0.002    0.000 {method 'acquire' of '_thread.lock' objects}
     1008    0.002    0.000    0.002    0.000 iostream.py:93(_event_pipe)
      337    0.002    0.000  351.360    1.043 <ipython-input-3-dcdd1d6561df>:6(get_chunk_of_lines)
     1008    0.002    0.000    0.004    0.000 threading.py:1062(_wait_for_tstate_lock)
      672    0.002    0.000    0.003    0.000 iostream.py:300(_is_master_process)
      672    0.001    0.000    0.008    0.000 iostream.py:313(_schedule_flush)
      672    0.001    0.000    0.001    0.000 {built-in method nt.getpid}
      672    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
     1008    0.000    0.000    0.000    0.000 threading.py:506(is_set)
     1008    0.000    0.000    0.000    0.000 {method 'append' of 'collections.deque' objects}
        1    0.000    0.000 1013.358 1013.358 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


```
