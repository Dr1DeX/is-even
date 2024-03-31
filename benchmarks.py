import timeit
from main import is_even, is_even_mod


def time_is_even():
    print("Func is_even start the execution:")
    for i in range(1, 1000000):
        is_even(i)
    print("Func is_even completes execution:")


def time_is_even_mod():
    print("Func is_even_mod start the execution: ")
    for i in range(1, 1000000):
        is_even_mod(i)
    print('Func is_even_mod completes execution: ')


start_time = timeit.default_timer()
time_is_even()
print(timeit.default_timer() - start_time)
start_time = timeit.default_timer()
time_is_even_mod()
print(timeit.default_timer() - start_time)
