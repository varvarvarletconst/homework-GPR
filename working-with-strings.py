sequence = 'I\'m as shocked as you are' #escape the apostrophe using \
print(sequence)
print(sequence[-2:-21:-2]) #a
print(sequence[7:14]) #b
print(sequence[-1:-8:-1]) #c by default, Python moves from left to right, so when slicing from the end to the beginning, you need to specify a negative step
print(sequence[2:13:5]) #d
print(sequence[2:]) #c
print(sequence[5:]) #c
print(sequence[8:]) #c
print(sequence[11:]) #e
print(sequence[7:]) #f