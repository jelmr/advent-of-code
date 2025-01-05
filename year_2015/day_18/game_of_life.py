import numpy as np
from scipy.signal import convolve2d


class GameOfLife:


    def iterate(self, matrix: np.array) -> np.array:
        kernel = np.array([
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ])

        num_neighbours_on = convolve2d(matrix, kernel, mode='same', boundary='fill', fillvalue=0)
        should_be_on = ((matrix == 1) & (num_neighbours_on == 2)) | (num_neighbours_on == 3)
        return np.where(should_be_on, 1, 0)
