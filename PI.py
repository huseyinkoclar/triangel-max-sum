
def isprime(num):
    num = int(num)
    if num == 1:
        return False
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

#recursive sum function
def sum(lines):
    if 1 == len(lines):
        lines[0][0]
    else:
        for i in range(len(lines[1])):
            #controls to stay inside the range
            temp = lines[1][i]
            if isprime(lines[1][i]):
                lines[1][i] = 0
                continue
            if len(lines[0]) == 1:
                lines[1][i] += lines[0][0]
                continue
            elif i < len(lines[0])-1 and i>0:
                lines[1][i] += max(lines[0][i-1],lines[0][i],lines[0][i+1])
            elif i > 0 and i != len(lines[0]):
                lines[1][i] += max(lines[0][i-1], lines[0][i])
            elif i > 0:
                lines[1][i] += lines[0][i-1]
            elif i < len(lines[0])-1:
                lines[1][i] += max(lines[0][i], lines[0][i+1])
            if temp - lines[1][i] == 0:
                lines[1][i] = 0

            
        return sum(lines[1:])

'''
with open("input.txt") as textFile:
    global lines
    lines = [line.split() for line in textFile]
'''
lines = [['215'], ['193', '124'], ['117', '237', '442'], ['218', '935', '347', '235'], ['320', '804', '522', '417', '345'], ['229', '601', '723', '835', '133', '124'], ['248', '202', '277', '433', '207', '263', '257'], ['359', '464', '504', '528', '516', '716', '871', '182'], ['461', '441', '426', '656', '863', '560', '380', '171', '923'], ['381', '348', '573', '533', '447', '632', '387', 
'176', '975', '449'], ['223', '711', '445', '645', '245', '543', '931', '532', '937', '541', '444'], ['330', '131', '333', '928', '377', '733', '017', '778', '839', '168', '197', '197'], ['131', '171', '522', '137', '217', '224', '291', '413', '528', '520', '227', '229', '928'], ['223', '626', '034', '683', '839', '053', '627', '310', '713', '999', '629', '817', '410', '121'], ['924', '622', '911', '233', '325', '139', '721', '218', '253', '223', '107', '233', '230', '124', '233']] 

#convert string to int for list
ints = [list( map(int,i) ) for i in lines]
sum(ints)
print("answer is: " + str(max(ints[len(ints)-1])))