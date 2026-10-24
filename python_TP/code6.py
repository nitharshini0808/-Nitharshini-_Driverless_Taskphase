def print_hash_table(table):
    for i in range(len(table)):
        print(f"{i}: {table[i]}")
def binary_search_insert_index(bucket, num):
    
    low, high = 0, len(bucket)

    while low < high:
        mid = (low + high) // 2
        if bucket[mid] < num:
            low = mid + 1
        else:
            high = mid

    return low  # this is the correct insertion point
def build_hash_table_sorted(n):
    table = [[] for _ in range(10)]

    for _ in range(n):
        num = int(input("Enter a number: "))
        index = num % 10                    
        bucket = table[index]
        pos = binary_search_insert_index(bucket, num)  
        bucket.insert(pos, num)             

    return table
n = int(input("How many numbers? "))
hash_table = build_hash_table_sorted(n)
print("\nHash Table:")
print_hash_table(hash_table)