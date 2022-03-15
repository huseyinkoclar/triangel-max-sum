

def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def sum(total,i,j):
    if i != 5:
        total += int(lines[i][j])
        total += int(sum(total, i+1,j))
    else:
        return int(total)
    
    


with open("input1.txt") as textFile:
    global lines
    lines = [line.split() for line in textFile]
i,j = 0,0
print(lines)
print(sum(0,0,0))




"""
f = open("input1.txt", "r")
global Lines
Lines = f.readlines()
for line in Lines:
    print(line)
    print("-")
"""