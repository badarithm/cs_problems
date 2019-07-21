from typing import Tuple
from time import time
from functools import reduce

def calculate_pi(n_terms: int) -> float:

    numerator: float = 4.0
    denominator: float = 1.0
    operation:float = 1.0
    pi: float = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi

def  re_calculate_pi(parameters: Tuple[int, int, float, float, float, float]) -> Tuple[float, int, int, float, float, float]:
    n_terms, term, numerator, denominator, operation, pi = parameters
    # print("{}".format(parameters))
    if term < n_terms:
        return re_calculate_pi((
            n_terms,
            term + 1,
            numerator,
            2.0 + denominator,
            operation * -1.0,
            pi + (operation * (numerator / denominator))))
    else:
        return parameters

def calculate(n_terms: int) -> float :
    return re_calculate_pi((n_terms, 0, 4.0, 1.0, 1.0, 0.0))[5]

def pi_from_list(n_terms: int) -> float:
    return sum([(-1)**(x % 2) * (4 / (1 + (x << 1)))for x in range(0, n_terms, 1)])


def calculate_1000_times() -> None:
    first = time()
    for _ in range(1000):
        calculate(990)
    second = time()

    for _ in range(1000):
        calculate_pi(990)
    third = time()

    for _ in range(1000):
        pi_from_list(990)
    fourth = time()

    print(second - first)
    print(third - second)
    print(fourth - third)
