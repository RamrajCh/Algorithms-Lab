import time
from mergeSort import merge_sort
from insertionsort import insertion_sort
import matplotlib.pyplot as plt

x_axis_is = range(10, 1000, 10)

y_is_bc = []
for x in x_axis_is:
    values = list(range(x))
    start_time = time.time()
    insertion_sort(values)
    end_time = time.time()
    y_is_bc.append((end_time-start_time)*10**6)
    
    
y_is_wc = []
for x in x_axis_is:
    values = list(reversed(range(x)))
    start_time = time.time()
    insertion_sort(values)
    end_time = time.time()
    y_is_wc.append((end_time-start_time)*10**6)
    

x_axis_ms = range(100, 10000, 100)
y_ms_bc = []
for x in x_axis_ms:
    values = list(range(x))
    start_time = time.time()
    merge_sort(values, 0, x-1)
    end_time = time.time()
    y_ms_bc.append((end_time-start_time)*10**6)
    

y_ms_wc = []
for x in x_axis_ms:
    values = list(reversed(range(x)))
    start_time = time.time()
    merge_sort(values, 0, x-1)
    end_time = time.time()
    y_ms_wc.append((end_time-start_time)*10**6)
    
fig, (insertion_plt, merge_plt) = plt.subplots(nrows=1, ncols=2)

insertion_plt.plot(x_axis_is, y_is_bc, '.', label='Best Case')
insertion_plt.plot(x_axis_is, y_is_wc, 'x', label='Worst Case')

insertion_plt.set_xlabel("Length of array (n)")
insertion_plt.set_ylabel("Time (in microseconds)")
insertion_plt.set_title("Insertion Sort")
insertion_plt.legend()

merge_plt.plot(x_axis_ms, y_ms_bc, '.', label='Best Case')
merge_plt.plot(x_axis_ms, y_ms_wc, 'x', label='Worst Case')

merge_plt.set_xlabel("Length of array (n)")
merge_plt.set_ylabel("Time (in microseconds)")
merge_plt.set_title("Merge Sort")
merge_plt.legend()


plt.show()