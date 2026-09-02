
n = int(input("Enter a number n "))

string_list = []

for i in range(n):
    u_s = input(f"Enter string: ")
    string_list.append(u_s)

print("Your list:", string_list)

letter_count = {}

a=len(string_list)

for i in range(a):

    k = string_list[i].lower()

    b=len(k)

    for j in range(b):

        letter = k[j]

        if letter in letter_count:
            letter_count[letter] = letter_count[letter]+1
        else:
            letter_count[letter] = 1
        j=j+1
    i=i+1
print(letter_count)





