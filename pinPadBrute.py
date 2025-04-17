newList = [(w, x, y, z, a, b) for w in range(0, 10) for x in range(0, 10) for y in range(0, 10) for z in range(0, 10) for a in range(0, 10) for b in range(0, 10)]

with open('6pin.txt', 'w') as f:
    f.write(str(newList))
f.close()
print("Made the list!")
