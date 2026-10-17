"""Tiny built-in dataset and descriptive-statistics exercises."""

ROWS = [
    {"group": "A", "minutes": 10, "score": 62},
    {"group": "A", "minutes": 15, "score": 69},
    {"group": "A", "minutes": 20, "score": 73},
    {"group": "A", "minutes": 25, "score": 81},
    {"group": "B", "minutes": 8, "score": 58},
    {"group": "B", "minutes": 14, "score": 66},
    {"group": "B", "minutes": 19, "score": 72},
    {"group": "B", "minutes": 23, "score": 76},
]


def mean(values):
    values = list(values)
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)


def group_mean(rows, group_field, value_field):
    groups = {}
    for row in rows:
        groups.setdefault(row[group_field], []).append(row[value_field])
    return {name: mean(values) for name, values in sorted(groups.items())}


def pearson_correlation(xs, ys):
    xs, ys = list(xs), list(ys)
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("two equal-length series with at least two values required")
    x_bar, y_bar = mean(xs), mean(ys)
    numerator = sum((x - x_bar) * (y - y_bar) for x, y in zip(xs, ys))
    denominator = (
        sum((x - x_bar) ** 2 for x in xs)
        * sum((y - y_bar) ** 2 for y in ys)
    ) ** 0.5
    if not denominator:
        raise ValueError("correlation is undefined for a constant series")
    return numerator / denominator
