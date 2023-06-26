import random
import timeit

import Merge_sort
import Quick_sort
import Heap_sort
import Counting_sort
import Bubble_sort


def generate_random_sequence(n):
    return random.sample(range(1, n + 1), n)


def generate_growing_sequence(n):
    return list(range(1, n + 1))


def generate_decreasing_sequence(n):
    return list(range(n, 0, -1))


numbers_n = random.sample(range(10, 51), 5)

# def measure_time(sort_func: object, sequence: object) -> object:
#     start_time = timeit.timeit()
#     sort_func(sequence)
#     end_time = timeit.timeit()
#     return end_time - start_time


def test_sorting_algorithms():
    sequence_types = [
        ("Random", generate_random_sequence),
        ("Growing", generate_growing_sequence),
        ("Decreasing", generate_decreasing_sequence)
    ]
    sequence_lengths = random.sample(range(10, 51), 5)
    num_tests = 5

    for sequence_type, generate_sequence in sequence_types:
        print("--- execution of sequence", sequence_type, "---")

        for length in sequence_lengths:
            print(f"\nLength of sequence {length}:")
            total_merge_sort_time = 0
            total_heap_sort_time = 0
            total_bubble_sort_time = 0
            total_counting_sort_time = 0
            total_quick_sort_time = 0

            for _ in range(num_tests):
                sequence = generate_sequence(length)

                bubble_sort_time = timeit.timeit(lambda: Bubble_sort.Bubble_sort(generate_sequence(length)), number=10000)
                counting_sort_time = timeit.timeit(lambda: Counting_sort.countingsort(generate_sequence(length)), number=10000)
                heap_sort_time = timeit.timeit(lambda: Heap_sort.heapsort(generate_sequence(length)), number=10000)
                merge_sort_time = timeit.timeit(lambda: Merge_sort.mergesort(generate_sequence(length)), number=10000)
                quick_sort_time = timeit.timeit(lambda: Quick_sort.quicksort(generate_sequence(length)), number=10000)
                print(str.format(": {} : {} : {} : {} :", round(bubble_sort_time, 3), round(counting_sort_time, 3),
                                 round(heap_sort_time, 3), round(merge_sort_time, 3), round(quick_sort_time, 3)))

                total_bubble_sort_time += bubble_sort_time
                total_counting_sort_time += counting_sort_time
                total_heap_sort_time += heap_sort_time
                total_merge_sort_time += merge_sort_time
                total_quick_sort_time += quick_sort_time

            avg_merge_sort_time = total_merge_sort_time / num_tests
            avg_heap_sort_time = total_heap_sort_time / num_tests
            avg_bubble_sort_time = total_bubble_sort_time / num_tests
            avg_counting_sort_time = total_counting_sort_time / num_tests
            avg_quick_sort_time = total_quick_sort_time / num_tests

            print("Average time:", sequence_lengths)
            print("Bubble Sort:", round(avg_bubble_sort_time, 5))
            print("Counting Sort:", round(avg_counting_sort_time, 5))
            print("Heap Sort:", round(avg_heap_sort_time,5 ))
            print("Merge Sort:", round(avg_merge_sort_time, 5))
            print("Quick Sort:", round(avg_quick_sort_time, 5))


test_sorting_algorithms()
