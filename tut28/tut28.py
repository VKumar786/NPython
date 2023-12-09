'''
    TODO: Set Methods in Python | Python Tutorial - Day #32 
    ? Venn diagram
    ? Symmetric difference
    *   A ∆ B = (A U B) – (A ∩ B)
    *   A ∆ B = (A – B) U (B – A)
    ? all operation are in perspective of A
    *   A.____(B)
    ? diff b/w remove and discard is that remove will raise exception when element not found in set
'''

# Set A
A = {1, 2, 3, 4, 5}

# Set B
B = {4, 5, 6, 7, 8}

# Set C
C = {3, 4, 5}

print(A.intersection(B))
print(A.union(B))
print(A.difference(B))  # A - B
print(B.difference(A))  # B - A

A.add(-1)
print(A)

B.remove(8)
print(B)

# print(A.difference_update(B))
A.update(B)  # A = A ∪ B
print(A)

A.intersection_update(B)  # A = A ∩ B
print(A)

# symmetric diff
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A.union(B).difference(A.intersection(B)))
print(A.difference(B).union(B.difference(A)))
print(A.symmetric_difference(B))

print(A.difference_update(B))  # A = A - B


# Disjoint
print(A.isdisjoint(B))  # A ∩ B = ϕ

# Super Set
A = {1, 2, 3, 4, 5, 6, 7, 8}
B = {4, 5, 6, 7, 8}

print(A.issuperset(B))  # A ⊃ B

# Sub Set
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A.issubset(B))  # A ⊂ B

print(B.pop())  # random value will be pop
print(B)

del C

A.clear()

if 8 in B:
    print("found")