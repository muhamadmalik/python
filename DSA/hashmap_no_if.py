def bit_wise(x):
    hash = {1:2, 2:1}
    return hash.get(x)


result = bit_wise(1)
print(result)