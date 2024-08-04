def norm(v: list, p = 2):
    return (sum((vec)**(p) for vec in v))**(1/p) 

print(norm([4,3]))
print(norm([4,3,4,5], 3))

#def norm(v, p=None):
#    if p is None:
#        # Default to Euclidean norm (p = 2)
#        p = 2
#        
#    if p <= 0:
#        raise ValueError("Norm order p must be greater than 0")
#    
#    # Compute p-norm
#    norm_value = sum(abs(x)**p for x in v)**(1/p)
#    return norm_value
#
## Example usage:
#vector = [4, 3]
#
## Compute Euclidean norm
#print(norm(vector))  # Output: 5.0
#
## Compute p-norm with p=3
#print(norm(vector, p=3))  # Output: 4.3267487109222245 (example output)


