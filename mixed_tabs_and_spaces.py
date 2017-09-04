def square(x):
    sum_so_far = 0
    for _ in range(x):
        sum_so_far += x
	return sum_so_far  # noqa: E999 # pylint: disable=mixed-indentation Python 3 will raise a TabError here

print(square(10))
