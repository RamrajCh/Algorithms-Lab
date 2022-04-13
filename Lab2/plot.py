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

y_ms = []
for x in x_axis_ms:
    values = list(range(x))
    start_time = time.time()
    merge_sort(values, 0, x-1)
    end_time = time.time()
    y_ms.append((end_time-start_time)*10**6)
    
fig, ax = plt.subplots(nrows=3, figsize=(20,30))

ax[0].plot(x_axis_is, y_is_bc, '.', label='Best Case - Insertion Sort')
ax[1].plot(x_axis_is, y_is_wc, 'x', label='Worst Case - Insertion Sort')

ax[0].set_xlabel("Length of array (n)")
ax[0].set_ylabel("Time (in microseconds)")
ax[0].set_title("Insertion Sort Best Case")
ax[0].legend()

ax[1].set_xlabel("Length of array (n)")
ax[1].set_ylabel("Time (in microseconds)")
ax[1].set_title("Insertion Sort Worst Case")
ax[1].legend()

ax[2].plot(x_axis_ms, y_ms, '.', label='Merge Sort')
# plt4.plot(x_axis_ms, y_ms_wc, 'x', label='Worst Case')

ax[2].set_xlabel("Length of array (n)")
ax[2].set_ylabel("Time (in microseconds)")
ax[2].set_title("Merge Sort")
ax[2].legend()


plt.show()