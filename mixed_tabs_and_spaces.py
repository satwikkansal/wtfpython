def square(x):
    sum_so_far = 0
    for counter in range(x):
        sum_so_far = sum_so_far + x
	return sum_so_far  # noqa Python 3 will raise a TabError here

print(square(10))
