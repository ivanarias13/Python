def map (func, values):
    output_values = []
    index = 0
    while index < len(values):
        output_values.append(values[index])
        index += 1
    return output_values

def add_one(val):
    return val +1

print(map(add_one, list(range(10))))
