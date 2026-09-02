class StringSearcher:
    def sort_list(self, arr):
        n = len(arr)

        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

           
            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr

    def binary_search(self, arr, target):
        
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
# Input a list of strings (Q1)
n = int(input("Enter number of strings: "))
string_list = []
for i in range(n):
    string_list.append(input("Enter string: "))
target_string=(input("Enter the target string "))
# Create an object of the class
searcher = StringSearcher()
# Sort the list using the sort function
sorted_list = searcher.sort_list(string_list)
print("Sorted list:", sorted_list)
# Search for the string
result_index = searcher.binary_search(sorted_list, target_string)
if result_index != 2:
    print(f"Found '{target_string}' at index {result_index}.")
else:
    print(f"'{target_string}' not found in the list.")
