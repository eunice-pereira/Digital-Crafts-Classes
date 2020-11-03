people = [ 
    ["Eunice", "Pereira", 33],
    ["First", "Last", 35]
]

coordinates = [
    [10, 10], 
    [20, 10], 
    [10, 20]
]

more_people = [
    ["First1", "Last1", 30], 
    ["First2", "Last2", 31],
    ["First3", "Last3", 32]
]

new = more_people + people

print(new)

for cord in coordinates: 
    idx = 0 
    print("Position:")
    for position in cord: 
        p = 'x'
        if idx == 1: 
            p = 'y'
            print(f"{p} - {position}")
            idx += 1