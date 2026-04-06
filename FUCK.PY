MOD = 10**9 + 7

def get_max_binary_value(N, A, B):

    A.sort(reverse=True)
    B.sort()
_
    total_bits = sum(A) + sum(B)
    current_pos = total_bits
    max_value = 0

    for i in range(N):
        size_1 = A[i]
        size_0 = B[i]

        start_pos = current_pos - size_1
        
        term = (pow(2, size_1, MOD) - 1) * pow(2, start_pos, MOD)
        max_value = (max_value + term) % MOD


        current_pos -= (size_1 + size_0)

    return max_value

# Example usage:
N = 2
A = [1,1]  # Blocks of 1s
B = [1,2]  # Blocks of 0s
print(get_max_binary_value(N, A, B))

