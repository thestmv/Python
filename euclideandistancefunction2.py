#4. Distance functions
# euclideandistancefunction2.py

#Lasketaan euklidinen etäisyys pisteiden välillä



def read_value():
  try:
    line = input("Enter a number: ")
    res = float(line)
  except ValueError:
    print("You gave an illegal number, " \
          "using value 1 instead." )
    res = 1
  return res

x1 = read_value()
y1 = read_value("Enter y1 number: ")
x2 = read_value("Enter x2 number: ")
y2 = read_value("Enter y2 number: ")
p2 = (x2, y2)
p1 = (x1, y1)

import math
dist = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(dist)