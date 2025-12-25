# 1. Break: Stops the loop completely when i is 34
for i in range(101):
    if(i == 34):
        break # Stops here, no more printing
    print(i)

# 2. Continue (For Loop): Skips specific numbers (34-39, 99) but keeps looping
for i in range(101):
    if(i in range(34,40)) or (i == 99):
        continue # Skip these, go to next number
    print(i)

# 3. Continue (While Loop): Skips numbers, but we must manually increase 'i' first
i = 0
while i < 101:
    if i in range(34,40):
        i += 1 # Increase i by 1
        continue # Skip printing for these numbers
    print(i)
    i += 1