def print_to_hundred(num):
    print(num)
    if num < 100:
        print_to_hundred(num+1)
    return ''
result = print_to_hundred(1)

print(result)