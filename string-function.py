sequence = input('give me a string: ')
#a  
print(len(sequence))
#b 
print(sequence.isalpha())
#c 
print(sequence.isidentifier())
#d 
print(sequence.endswith('ing')) 
#e 
print(sequence.lower())
#or
print(sequence.swapcase())
#f 
print(sequence.replace('a', 'e'))

a = 'My friend told me that it\'s time for me to stop trying to do programming because I\'m not cut out for it.'
b = 'ОПАСНОСТЬ'
c = 'I can recite pi from memory: 3.1415926...'

#test 1
print('test one: a = My friend told me that it\'s time for me to stop trying to do programming because I\'m not cut out for it.')
#a  
print(len(a))
#b 
print(a.isalpha())
#c 
print(a.isidentifier())
#d 
print(a.endswith('ing')) 
#e 
print(a.lower())
#or
print(a.swapcase())
#f 
print(a.replace('a', 'e'))

#test 2
print('test two')
#a  
print(len(b))
#b 
print(b.isalpha())
#c 
print(b.isidentifier())
#d 
print(b.endswith('ing')) 
#e 
print(b.lower())
#or
print(b.swapcase())
#f 
print(b.replace('a', 'e'))

#test 3
#a  
print(len(c))
#b 
print(c.isalpha())
#c 
print(c.isidentifier())
#d 
print(c.endswith('ing')) 
#e 
print(c.lower())
#or
print(c.swapcase())
#f 
print(c.replace('a', 'e'))