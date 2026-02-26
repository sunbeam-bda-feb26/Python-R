# optional parameter
# - parameter having default value
# - while calling function, optional parameter value may or may not be passed

def calculate_simple_interest(p: int, n: int, r: float = 8.5):
    print(f"p = {p}, n = {n}, r = {r}")
    interest = (p * n * r) / 100
    print(f"interest = {interest}")


# in all these function calls the value of r is 8.5
# which is taken from the default value
calculate_simple_interest(100000, 2)
calculate_simple_interest(500000, 1)
calculate_simple_interest(1000000, 2)

# if value of r is present, 
# the given value will be used instead of using the default value
# the value 7.5 will NOT change the default value
calculate_simple_interest(500000, 1, 7.5)

# if the value of r is missing, the default will be taken
calculate_simple_interest(1000000, 5)