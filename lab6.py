with open('input_1.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input_1.txt', 'r') as f:
    result = f.readlines()
    print(result)