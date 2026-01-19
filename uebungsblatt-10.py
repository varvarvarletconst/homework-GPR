import re

with open('test.txt', 'r') as file:
    text = file.read()

pattern_numbers = r'\d+[.,]\d+'
numbers = re.findall(pattern_numbers, text)

print(" FLOATS ")
for num in numbers:
    print(num)
print()


pattern_closing_tags = r'</[^>]+>'
closing_tags = re.findall(pattern_closing_tags, text)

print(" </> ")
for tag in closing_tags:
    print(tag)
print()


pattern_href = r'href="[^"]+"'
hrefs = re.findall(pattern_href, text)

print(' href ')
for href in hrefs:
    print(href)
print()
