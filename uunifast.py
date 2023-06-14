import csv
import random


def generate_uunifastdiscard(nsets: int, u: float, n: int, filename: str):
    """
    The UUniFast algorithm was proposed by Bini for generating task
    utilizations on uniprocessor architectures.
    The UUniFast-Discard algorithm extends it to multiprocessor by
    discarding task sets containing any utilization that exceeds 1.
    This algorithm is easy and widely used. However, it suffers from very
    long computation times when n is close to u. Stafford's algorithm is
    faster.
    Args:
        -   n  : The number of tasks in a task set.
        -   u  : Total utilization of the task set.
        -   nsets  : Number of sets to generate.
        -   filename  : Name of the CSV file to save the results.
    Returns   nsets   of   n   task utilizations.
    """
    sets = []
    while len(sets) < nsets:
        utilizations = []
        sumU = u
        for i in range(1, n):
            nextSumU = sumU * random.random() ** (1.0 / (n - i))
            utilizations.append(sumU - nextSumU)
            sumU = nextSumU
        utilizations.append(sumU)
        
        if all(ut <= 1 for ut in utilizations):
            sets.append(utilizations)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Task ' + str(i) for i in range(1, n+1)])
        for utilizations in sets:
            writer.writerow(utilizations)

    return sets


utilizations = generate_uunifastdiscard(nsets=5, u=0.1, n=10, filename='task_utilizations.csv')