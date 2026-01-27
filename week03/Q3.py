point1 = (3, 5)
point2 = (7, 2)
print(f"Point 1: {point1}\nPoint 2: {point2}")
x1, y1 = point1
x2, y2 = point2
print(f"x1: {x1}, y1: {y1}\nx2: {x2}, y2: {y2}")
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Distance between point 1 and point 2", distance)
