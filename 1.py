fhand = open('mbox-short.txt')
counts = dict()

for line in fhand:
    if line.startswith('From'):
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word]=1
            elif word in counts:
                counts[word]+=1

print(counts)