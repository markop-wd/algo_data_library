import random

random_values = [random.randint(1, 100) for _ in range(10)]

print(random_values)

for run in range(0, len(random_values)):
    for x_pos in range(len(random_values) - run):
        x = random_values[x_pos]
        y_pos = x_pos + 1
        try:
            y = random_values[y_pos]
        except IndexError:
            break
        if x > y:
            random_values[x_pos], random_values[y_pos] = random_values[y_pos], random_values[x_pos]
            x_pos, y_pos = y_pos, x_pos


