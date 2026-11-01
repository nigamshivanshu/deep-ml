import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	mat_a = np.array(a)
	mat_b = np.array(b)
	if np.shape(mat_a)[1] == np.shape(mat_b)[0]:
		return list(np.dot(a, b))
	else:
		return -1