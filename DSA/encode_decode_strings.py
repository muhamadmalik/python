def encode(list):
    res = ''
    for i in list:
        res += str(len(i)) + '#' + i
    return res


def decode(str):
    i = 0
    res = []
    while i < len(str):
        j = i
        while str[j] != '#':
            j = j + 1
        wordLength = int((str[i:j]))
        res.append(str[j+1:wordLength+j+1])
        i = j + 1 + wordLength 
    return res
encoded_string = encode(['apple', 'ciderdd', 'yeahhh'])
print(encoded_string)
print(decode(encoded_string))
# when there is first number we use this as an for loop limit and when comes hash
# 5#apple7#ciderdd6#yeahhh
