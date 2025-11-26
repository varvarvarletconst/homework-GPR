needle = input('needle: ') #the part we are looking for
haystack = input('haystack: ') #the group of symbols where we are looking for it
#I found out that needl and haystack are traditional named for this type of exercises 

def find_substring(needle, haystack):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i

print(find_substring(needle, haystack))

print('test 1: бал and хабалка')
print(find_substring('бал', 'хабалка'))
print('test 2: e and pi')
print(find_substring('2.718281828459045', '3.141592653589793')) #our function cannot work with numbers so that's why we have to put our numbers in '' and those are actually strings not numbers
print('test 3: ')
print(find_substring('', 'hello'))
