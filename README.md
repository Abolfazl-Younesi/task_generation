# Project Name

A collection of files for generating random periods and task sets.

## Table of Contents

- [Description](#description)
- [Files](#files)
- [Contributing](#contributing)
- [License](#license)

## Description

This project provides several Python scripts for generating random periods and task sets for various purposes. The files included are:

- `generate_random_periods_discrete.py`: Generates a matrix of random periods chosen randomly from a list of available periods using a discrete distribution.
- `generate_random_periods_loguniform.py`: Generates a list of sets containing random periods using a loguniform distribution.
- `generate_random_periods_uniform.py`: Generates a list of sets containing random periods using a uniform distribution.
- `ripoll_taskset_generation.py`: Generates task sets with specific properties such as computation time, slack time, delay, and target utilization.
- `taskset_generation.py`: Generates task sets based on provided task utilization and period sets.
- `uunifast.py`: Implements the UUniFast and UUniFast-Discard algorithms for generating task utilizations on uniprocessor and multiprocessor architectures.

## Files

1. `generate_random_periods_discrete.py`: 
    - Description: Generates a matrix of (num_sets x num_periods) random periods chosen randomly from the list of available periods.
    - Args:
        - `num_periods`: The number of periods in a period set.
        - `num_sets`: Number of sets to generate.
        - `available_periods`: A list of available periods.
    - Tags: random periods, discrete distribution

2. `generate_random_periods_loguniform.py`:
    - Description: Generates a list of num_sets sets containing num_periods random periods using a loguniform distribution.
    - Args:
        - `num_periods`: The number of periods in a period set.
        - `num_sets`: Number of sets to generate.
        - `min_period`: Minimum period value.
        - `max_period`: Maximum period value.
        - `round_to_int`: Whether to round the generated periods to integers.
    - Tags: random periods, loguniform distribution

3. `generate_random_periods_uniform.py`:
    - Description: Generates a list of num_sets sets containing num_periods random periods using a uniform distribution.
    - Args:
        - `num_periods`: The number of periods in a period set.
        - `num_sets`: Number of sets to generate.
        - `min_period`: Minimum period value.
        - `max_period`: Maximum period value.
        - `round_to_int`: Whether to round the generated periods to integers.
    - Tags: random periods, uniform distribution

4. `ripoll_taskset_generation.py`:
    - Description: Generates task sets with specific properties such as computation time, slack time, delay, and target utilization.
    - Args:
        - `n_sets`: Number of task sets to generate.
        - `max_compute_time`: Maximum computation time of a task.
        - `max_slack_time`: Maximum slack time.
        - `max_delay`: Maximum delay after the deadline.
        - `target_utilization`: Total utilization to reach.
    - Returns:
        - `task_sets`: List of task sets generated.
    - Tags: task sets, computation time, slack time, delay, target utilization

5. `taskset_generation.py`:
    - Description: Generates task sets based on provided task utilization and period sets.
    - Args:
        - `utilizations`: The list of task utilization sets.
        - `periods`: The list of task period sets.
        - `filename`: The name of the CSV file to save the results in.
    - Returns:
        - For the provided example, it returns:
           

            ```
            [[(3.0, 20), (20.0, 50), (8.0, 13), (10.0, 80), (8.0, 23)],
             [(10.0, 110), (123.0,320), (14.0, 80), (50.0,150), (5.0, 10)]]
            ```
    - Tags: task sets, task utilization, period sets

6. `uunifast.py`:
    - Description: Implements the UUniFast and UUniFast-Discard algorithms for generating task utilizations on uniprocessor and multiprocessor architectures.
    - Args:
        - `n`: The number of tasks in a task set.
        - `u`: Total utilization of the task set.
        - `nsets`: Number of sets to generate.
        - `filename`: Name of the CSV file to save the results.
    - Returns `nsets` of `n` task utilizations.
    - Tags: task utilizations, UUniFast, UUniFast-Discard

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
        - `filename`: The name of the CSV file to save the results in.
    - Returns:
        - For the provided example, it returns:
            ```
            [[(3.0, 20), (20.0, 50), (8.0, 13), (10.0, 80), (8.0, 23)],
             [(10.0, 110), (123.0,320), (14.0, 80), (50.0,150), (5.0, 10)]]
            ```

6. `uunifast.py`:
    - Description: Implements the UUniFast and UUniFast-Discard algorithms for generating task utilizations on uniprocessor and multiprocessor architectures.
    - Args:
        - `n`: The number of tasks in a task set.
        - `u`: Total utilization of the task set.
        - `nsets`: Number of sets to generate.
        - `filename`: Name of the CSV file to save the results.
    - Returns `nsets` of `n` task utilizations.


## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

