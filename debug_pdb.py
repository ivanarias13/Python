import pdb

def map (func, values):
    output_values = []
    index = 0
    while index < len(values):
        pdb.set_trace()
        output_values = func(values[index])
        index += 1
    return output_values

def add_one(val):
    return val +1

print(map(add_one, list(range(10))))


"""
PS C:\Users\ivana\Documents\Python> python.exe -m pdb .\debug_pdb.py
> c:\users\ivana\documents\python\debug_pdb.py(1)<module>()
-> import pdb
(Pdb)
"""