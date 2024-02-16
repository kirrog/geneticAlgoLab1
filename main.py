import time
import tracemalloc
from random import randint
from typing import Tuple, Union, Any
from numba.typed import List

from numba import njit


def check_sort(input_data, algo_func, njit_) -> Tuple[Union[bool, Any], float, int]:
    sorted_data_reference = input_data.copy()
    sorted_data_reference.sort()
    if njit_:
        input_data_new = List()
        [input_data_new.append(x) for x in input_data]
        input_data = input_data_new
    tracemalloc.start()
    start = time.time()
    sorted_data_func = algo_func(input_data)
    stop = time.time()
    current, maximum = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    if njit_:
        sorted_data_func = list(sorted_data_func)
    return sorted_data_func == sorted_data_reference, stop - start, maximum


def sort_default(list2sort):
    max_num = max(list2sort)
    min_num = min(list2sort)
    cnt = [0] * (max_num + 1 - min_num)
    for item in list2sort:
        cnt[item - min_num] += 1
    result = [0] * len(list2sort)
    counter = 0
    for num, count in enumerate(cnt):
        for i in range(count):
            result[counter] = num + min_num
            counter += 1
    return result


@njit
def sort_optimised(list2sort):
    max_num = max(list2sort)
    min_num = min(list2sort)
    cnt = [0] * (max_num + 1 - min_num)
    for item in list2sort:
        cnt[item - min_num] += 1
    result = [0] * len(list2sort)
    counter = 0
    for num, count in enumerate(cnt):
        for i in range(count):
            result[counter] = num + min_num
            counter += 1
    return result


def generate_random_data(bias=0, up_level=1000, count=1000):
    return [randint(bias, bias + up_level) for r in range(count)]


iteration_num = 100

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("results.tsv", "w") as f:
        f.write(f"up_level_iter\tcount_iter\tdefault_accum\toptimised_accum\n")
        for up_level_iter in [x * 1000 for x in range(1, 11)]:
            for count_iter in [x * 1000 for x in range(1, 11)]:
                default_time_accum = 0.0
                default_mem_accum = 0.0
                optimised_time_accum = 0.0
                optimised_mem_accum = 0.0
                for i in range(iteration_num):
                    data = generate_random_data(0, up_level_iter, count_iter)
                    check, time_, maximum_mem = check_sort(data, sort_default, False)
                    assert check
                    default_time_accum += time_ / iteration_num
                    default_mem_accum += maximum_mem / iteration_num

                    data = generate_random_data(0, up_level_iter, count_iter)
                    check, time_, maximum_mem = check_sort(data, sort_optimised, True)
                    assert check
                    optimised_time_accum += time_ / iteration_num
                    optimised_mem_accum += maximum_mem / iteration_num
                f.write(f"{up_level_iter:05d}\t{count_iter:05d}\t"
                        f"{default_time_accum:.09f}\t{optimised_time_accum:.09f}\t"
                        f"{default_mem_accum:.01f}\t{optimised_mem_accum:.01f}\n")
                print(f"{up_level_iter:05d}\t{count_iter:05d}\t{default_time_accum:.09f}\t"
                      f"{optimised_time_accum:.09f}\t"
                      f"{default_mem_accum:.01f}\t{optimised_mem_accum:.01f}")
