import numpy as np

def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    mat_a = np.array(a)
    reshaped_matrix = []

    if mat_a.size == new_shape[0] * new_shape[1]:
        reshaped_matrix = np.reshape(mat_a, new_shape)
        reshaped_matrix = reshaped_matrix.tolist()

    return reshaped_matrix