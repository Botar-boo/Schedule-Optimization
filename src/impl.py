from itertools import product
from heapq import heapify, heappop, heappush


def calc_greedy_schedule(tasks, num_of_processors):
    tasks.sort(reverse=True)
    processors = [0] * num_of_processors
    heapify(processors)
    for i, length in enumerate(tasks):
        cur_processor = heappop(processors)
        cur_processor += length
        heappush(processors, cur_processor)

    return max(processors)


def calc_bruteforce_schedule(tasks, num_of_processors):
    num_of_tasks = len(tasks)
    possible_processors = [i for i in range(num_of_processors)]
    possible_processors_for_all_tasks = [possible_processors] * num_of_tasks
    all_permutations = list(product(*possible_processors_for_all_tasks))

    best_ans = float("inf")
    for permutation in all_permutations:
        cur_processors_work_time = [0] * num_of_processors
        for i, processor in enumerate(permutation):
            cur_processors_work_time[processor] += tasks[i]
        best_ans = min(best_ans, max(cur_processors_work_time))

    return best_ans
