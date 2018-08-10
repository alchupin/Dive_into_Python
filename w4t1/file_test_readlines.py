with open('test.txt') as f:
    data = f.readlines()
for line in data:
    print(line)    
print(len(data))
