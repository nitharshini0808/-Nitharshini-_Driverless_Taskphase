n = int(input("Enter number of points: "))

c = []
for i in range(n):
    x = float(input(f"Enter x{i+1}: "))
    y = float(input(f"Enter y{i+1}: "))
    c.append((x, y))

m = float(input("Enter reference x: "))
k = float(input("Enter reference y: "))

arr = []
for i in range(n):
    d = ((c[i][0] - m)**2 + (c[i][1] - k)**2)**0.5
    arr.append((d, c[i][0], c[i][1]))

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