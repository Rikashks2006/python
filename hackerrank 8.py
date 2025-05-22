import numpy

# Read input and convert to numpy arrays
A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))

# Compute and print inner product
print(numpy.inner(A, B))

# Compute and print outer product
print(numpy.outer(A, B))
