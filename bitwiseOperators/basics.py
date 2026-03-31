
def pr_binary(num):
    # Loop from bit 10 down to 0
    for i in range(10, -1, -1):
        # Shift the i-th bit to the 0th position and check if it's 1 or 0
        print((num >> i) & 1, end="")
    print() # Print a newline

pr_binary(13) # Output: 00000001101

def check_bit(num, i):
    mask = 1 << i
    if (num & mask) != 0:
        print(f"Bit {i} is Set")
    else:
        print(f"Bit {i} is Not set")

check_bit(13, 2) # 13 is 1101. The bit at index 2 (0-indexed from right) is 1. Output: Set.