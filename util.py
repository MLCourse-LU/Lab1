import numpy as np


def generate_distribution(mean, std, amount):
    return (np.random.randn(amount) * std) + mean


def generate_data():
    amount_1 = 60
    height_1 = generate_distribution(5, 2, amount_1)
    width_1 = generate_distribution(2, 3, amount_1)
    X1 = np.column_stack([height_1, width_1])
    y1 = np.full(amount_1, 1)

    amount_2 = 40
    height_2 = generate_distribution(1, 3, amount_2)
    width_2 = generate_distribution(5, 1, amount_2)
    X2 = np.column_stack([height_2, width_2])
    y2 = np.full(amount_2, -1)

    return np.row_stack([X1, X2]), np.concatenate([y1, y2])
