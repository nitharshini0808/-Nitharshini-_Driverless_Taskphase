def build_hash_table(n):
    
    table = [[] for _ in range(10)]

    for _ in range(n):
        num = int(input("Enter a number: "))
        index = num % 10          
        table[index].append(num)  

    return table
def print_hash_table(table):

    for i in range(len(table)):
        print(f"{i}: {table[i]}")
n = int(input("How many numbers? "))
hash_table = build_hash_table(n)
print("\nHash Table:")
print_hash_table(hash_table)