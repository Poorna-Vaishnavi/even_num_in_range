def count_even_numbers(A, B):
    counts = []
    for query in B:
        start_index, end_index = query
        count = 0
        for i in range(start_index, end_index + 1):
            if A[i] % 2 == 0:
                count += 1
        counts.append(count)
    return counts

# Get input from the user
A = list(map(int, input("Enter the elements of array A (space-separated): ").split()))
B = []
q = int(input("Enter the number of queries: "))
print("Enter the queries in the format B[i][0] B[i][1]:")
for _ in range(q):
    query = list(map(int, input().split()))
    B.append(query)

output = count_even_numbers(A, B)
print("Output:", output)