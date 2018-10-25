from functools import reduce
import math
import numpy


def find_transient_arrays(m):
    transient_arrays = []
    for array in m:
        if reduce((lambda x, y: x + y), array) > 0:
            transient_arrays.append(array)
    return transient_arrays

def find_q_and_r(trans_arrays):
    n = len(trans_arrays)
    q_array = []
    r_array = []
    for index, array in enumerate(trans_arrays):
        q_array.extend(array[:n])
        r_array.extend(array[n:])
    return [q_array, r_array]

def turn_values_to_decimals(transient_arrays):
    for array in transient_arrays:
        denominator = reduce((lambda x, y: x + y), array)
        print(denominator)
        for index, value in enumerate(array):
            array[index] = float(value)/float(denominator)
            print(array)
    return transient_arrays

def subtract_q_from_i(n, q_array):
    i_length = 1
    i = []
    while i_length < n*n:
        zero_counter = 0
        i.append(1)
        while zero_counter < n:
            i.append(0)
            zero_counter += 1
        i_length += n+1
    i.append(1)
    # print(i)
    # print(q_array)
    return([i[index] - q_array[index] for index,value in enumerate(i)])

def inverse_a(a, n):
    big_one = []
    counter = 0
    for i in range(0, n):
        big_one.append(a[counter:n+counter])
        counter += n
    return numpy.linalg.inv(big_one)

def multiply_matrices(inverted_a, r):
    multiplied_matrix = []
    counter = 0
    for index, value in enumerate(inverted_a):
        print value
        for i, v in inverted_a[index]:
            print v
            for x in r[i]:
                print v[i] * x
    return "done"



    return "something"

def answer(m):
    trans_arrays = turn_values_to_decimals(find_transient_arrays(m))
    n = len(trans_arrays)
    q_and_r_array = find_q_and_r(trans_arrays)
    q_array = q_and_r_array[0]
    r_array = q_and_r_array[1]
    a = subtract_q_from_i(n, q)
    inverted_a = inverse_a(a, n)


# [1.0, -0.5, -0.4444444444444444, 1.0]

# >>> q_and_r_array
# [[0.0, 0.5, 0.4444444444444444, 0.0], [0.0, 0.0, 0.0, 0.5, 0.0, 0.3333333333333333, 0.2222222222222222, 0.0]]
