import csv

with open("cones.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

n = len(rows)

arr = []
for i in range(n):
    x = float(rows[i][1])
    y = float(rows[i][2])
    d = (x**2 + y**2)**0.5
    arr.append((d, rows[i][0], x, y, rows[i][3]))  

print(arr)

class SelectionSort:
    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

obj = SelectionSort()
result = obj.selection_sort(arr)
print("Sorted list:", result)

blue = []
yellow = []
for item in result:
    colour = item[4]     
    if colour == "blue":
        blue.append(item)
    elif colour == "yellow":
        yellow.append(item)


with open("blue_cones.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "x", "y", "colour"])  
    for item in blue:
        d, cone_id, x, y, colour = item
        writer.writerow([cone_id, x, y, colour])


with open("yellow_cones.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "x", "y", "colour"])   
    for item in yellow:
        d, cone_id, x, y, colour = item
        writer.writerow([cone_id, x, y, colour])

midpoints = []
for b in blue:
    d_b, id_b, xb, yb, colour_b = b
    
    nearest_dist = None
    nearest_yellow = None
    
    for y in yellow:
        d_y, id_y, xy, yy, colour_y = y
        dist = ((xb - xy)**2 + (yb - yy)**2)**0.5
        
        if nearest_dist is None or dist < nearest_dist:
            nearest_dist = dist
            nearest_yellow = y
    
    xy_n, yy_n = nearest_yellow[2], nearest_yellow[3]
    mx = (xb + xy_n) / 2
    my = (yb + yy_n) / 2
    midpoints.append((mx, my))

print(midpoints)

with open("centreline.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y"])
    for mx, my in midpoints:
        writer.writerow([mx, my])

print("centreline.csv written")


