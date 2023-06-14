import csv
import numpy as np

def generate_random_periods_uniform(num_periods: int, num_sets: int, min_period: float, max_period: float, round_to_int: bool = False):
    """
    Generate a list of num_sets sets containing each num_periods random periods using a uniform distribution.
    Args:
        - num_periods: The number of periods in a period set.
        - num_sets: Number of sets to generate.
        - min_period: Minimum period value.
        - max_period: Maximum period value.
        - round_to_int: Whether to round the generated periods to integers.
    """
    periods = np.random.uniform(low=min_period, high=max_period, size=(num_sets, num_periods))

    if round_to_int:
        periods = np.rint(periods).tolist()
    else:
        periods = periods.tolist()

    with open('uniform_periods.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i, period_set in enumerate(periods):
            writer.writerow([f'Period Set {i+1}'] + period_set)

    return periods