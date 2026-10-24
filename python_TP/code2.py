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
n = int(input("Enter number of strings: "))
string_list = []
for i in range(n):
    string_list.append(input("Enter string: "))
obj = SelectionSort()
result = obj.selection_sort(string_list)
print("Sorted list:", result)







