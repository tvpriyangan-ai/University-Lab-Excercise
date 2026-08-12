

import time
import random

                
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break
        



# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    return quick_sort(left) + middle + quick_sort(right)


# Quick Sort - Version_1
def quick_sort_ver_1(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    return quick_sort_ver_1(left) + middle + quick_sort_ver_1(right)


# Quick Sort - Version_2 [ Uses partition function provided below]
def quick_sort_ver_2(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pi = partition(arr, low, high)

            # Push subarrays onto stack
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Merge sort
def merge_sort(lst):
    # if the list is this short, no sorting is necessary
    if len(lst) <= 1:
        # return a copy, out-of-place
        return list(lst)

    # half the length, rounded down
    m = len(lst) // 2

    # list slicing
    A = lst[:m]
    B = lst[m:]

    # sort both halves recursively
    A = merge_sort(A)
    B = merge_sort(B)

    return linear_merge(A, B)

def linear_merge(A, B):
    # merge two sorted lists
    output = []
    i, j = 0, 0

    while i + j < len(A) + len(B):
        if i < len(A) and (j == len(B) or A[i] <= B[j]):
            output.append(A[i])
            i += 1
        else:
            output.append(B[j])
            j += 1

    return output




# --------- Your sorting functions should already be defined ----------
# def bubble_sort(arr): ...
# def quick_sort(arr): ...
# --------------------------------------------------------------------

# Generate lists
def generate_lists(size):
    random_list = [random.randint(1, 10000) for _ in range(size)]
    sorted_list = sorted(random_list)
    return random_list, sorted_list

# Measure time in milliseconds
def measure_time(sort_function, arr):
    start = time.perf_counter()
    sort_function(arr)
    end = time.perf_counter()
    return (end - start) * 1000  # ms

def average_time(sort_function, data, runs=5):
    total_time = 0

    for i in range(runs):
        total_time += measure_time(sort_function, data)

    return total_time / runs

# Benchmark comparison
def compare_algorithms(runs=10):
    sizes = [1,2,3,4, 5,6,10,100,1000,3000,5000,10000]

    print("Size\t ******Bubble Sort*****")
    print("\tList-1 \t\t List-2")

    for size in sizes:
        b_rand, b_sorted = [], []
        m_rand, m_sorted = [], []
        q_rand, q_sorted = [], []
        q1_rand, q1_sorted = [], []
        q2_rand, q2_sorted = [], []
        
        for _ in range(runs):
            rand_list, sorted_list = generate_lists(size)

            # Bubble Sort
            b_rand.append(measure_time(bubble_sort, rand_list.copy()))
            b_sorted.append(measure_time(bubble_sort, sorted_list.copy()))

            # Merge Sort
            m_rand.append(measure_time(merge_sort, rand_list.copy()))
            m_sorted.append(measure_time(merge_sort, sorted_list.copy()))

            # Quick Sort
            q_rand.append(measure_time(quick_sort, rand_list.copy()))   
            q_sorted.append(measure_time(quick_sort, sorted_list.copy()))

            # Quick Sort - Version 1
            q1_rand.append(measure_time(quick_sort_ver_1, rand_list.copy()))
            q1_sorted.append(measure_time(quick_sort_ver_1, sorted_list.copy()))

            # Quick Sort - Version 2
            q2_rand.append(measure_time(quick_sort_ver_2, rand_list.copy()))
            q2_sorted.append(measure_time(quick_sort_ver_2, sorted_list.copy()))

            
                  
        # Compute averages
        avg_br = sum(b_rand) / runs
        avg_bs = sum(b_sorted) / runs
        avg_mr = sum(m_rand) / runs
        avg_ms = sum(m_sorted) / runs
        avg_qr = sum(q_rand) / runs
        avg_qs = sum(q_sorted) / runs
        avg_q1r = sum(q1_rand) / runs
        avg_q1s = sum(q1_sorted) / runs
        avg_q2r = sum(q2_rand) / runs
        avg_q2s = sum(q2_sorted) / runs

        print("size:",size,"avg_br:", avg_br,"avg_bs:", avg_bs,"avg_mr:", avg_mr,"avg_ms:", avg_ms,"avg_qr:", avg_qr,"avg_qs:", avg_qs,"avg_q1r:", avg_q1r,"avg_q1s:", avg_q1s,"avg_q2r:", avg_q2r,"avg_q2s:", avg_q2s)


# Run comparison
compare_algorithms()