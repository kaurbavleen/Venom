def compute_hcf(a, b):
    smaller = a if a < b else b
    hcf = 1
    for i in range(1, smaller + 1):
        if (a % i == 0) and (b % i == 0):
            hcf = i   # return mat karo yaha, sirf update karo
    return hcf   # loop ke baad return karo

# user input
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print(f"\nUsing Iterative function = HCF of n1 and n2 is:", compute_hcf(n1, n2))
