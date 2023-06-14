import csv
import numpy as np

def generate_random_periods_discrete(num_periods: int, num_sets: int, available_periods: list):
    """
    Generate a matrix of (num_sets x num_periods) random periods chosen randomly in the list of available periods.
    Args:
        - num_periods: The number of periods in a period set.
        - num_sets: Number of sets to generate.
        - available_periods: A list of available periods.
    """
    try:
        periods = np.random.choice(available_periods, size=(num_sets, num_periods)).tolist()
    except AttributeError:
        p = np.array(available_periods)
        periods = p[np.random.randint(len(p), size=(num_sets, num_periods))].tolist()

    with open('discrete_periods.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i, period_set in enumerate(periods):
            writer.writerow([f'Period Set {i+1}'] + period_set)

    return periods