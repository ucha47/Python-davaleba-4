text = 'სწავლის ძირი მწარე არის კენწეროში გატკბილდების'

print(text[:20])

count = 0
for i in text:
    if i == 'ს':
        count = count + 1
print(count)