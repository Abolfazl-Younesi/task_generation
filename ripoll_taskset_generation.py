import random

def ripoll_taskset_generation(n_sets: int, max_compute_time: int, max_slack_time: int, max_delay: int, target_utilization: float):
    """
    Args:
        -   n_sets  : Number of tasksets to generate.
        -   max_compute_time  : Maximum computation time of a task.
        -   max_slack_time  : Maximum slack time.
        -   max_delay  : Maximum delay after the deadline.
        -   target_utilization  : Total utilization to reach.
    Returns:
        -   task_sets  : List of tasksets generated.
    """
    task_sets = []
    for i in range(n_sets):
        task_set = []
        total_utilization = 0.0
        while total_utilization < target_utilization:
            compute_time, slack_time, delay = random.randint(1, max_compute_time), random.randint(0, max_slack_time), random.randint(0, max_delay)
            task_set.append((compute_time, compute_time + slack_time, compute_time + slack_time + delay))
            total_utilization += compute_time / (compute_time + slack_time + delay)
        task_sets.append(task_set)
    return task_sets