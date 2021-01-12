""" Utility functions """
import numpy as np


def generate_distribution(mean, std, amount):
    """ Generate normally distributed numbers """
    return (np.random.randn(amount) * std) + mean


def generate_data():
    """ Generate some data from two distributions """
    amount_1 = 60
    height_1 = generate_distribution(5, 2, amount_1)
    width_1 = generate_distribution(2, 3, amount_1)
    x_1 = np.column_stack([height_1, width_1])
    y_1 = np.full(amount_1, 1)

    amount_2 = 40
    height_2 = generate_distribution(1, 3, amount_2)
    width_2 = generate_distribution(5, 1, amount_2)
    x_2 = np.column_stack([height_2, width_2])
    y_2 = np.full(amount_2, -1)

    return np.row_stack([x_1, x_2]), np.concatenate([y_1, y_2])
