#4. Distance functions
# euclideandistancefunction1.py

#Lasketaan euklidinen etäisyys pisteiden välillä
import math

print("Anna x1")
x1 = int(input())
print("Anna y1")
y1 = int(input())
print("Anna x2")
x2 = int(input())
print("Anna y1")
y2 = int(input())


# Example points in 3-dimensional space...
p1 = (x1, y1)
p2 = (x2, y2)
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(p1, p2)]))
print("Distance between", p1 ,"and", p2, "is",distance)