# triangle numbers

# x sub n = n(n + 1)/2 

i = 0 

while i < 100: 
    triangle = int(i * (i + 1) / 2)
    print(f"List: {i} is triangle number {triangle}")
    i += 1 