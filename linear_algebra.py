from math import sqrt

# Some helper linear algebra functions

def string_to_vector(A):
    assert type(A) == str
    return [ord(char) for char in A]

def dot_product(A, B):
    if len(A) > len(B): A, B = B, A
    while len(A) < len(B): A.append(0)
    return sum([i * j for i, j in zip(A, B)])

def magnitude(A):
    return sqrt(sum([i * i for i in A]))

def cosine_similarity(A, B):
    return dot_product(A, B) / (magnitude(A) * magnitude(B))