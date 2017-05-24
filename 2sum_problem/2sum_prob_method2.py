import time

num_dic = {}
with open("prob-2sum.txt") as f:
    for line in f:
        num = line.split()[0]
        key = int(num[:-4])
        num = int(num)
        if key in num_dic:
            num_dic[key].add(num)
        else:
            num_dic[key]={num}

sums = set()
for key in num_dic:
    if key > 0:
        if -key in num_dic:
            for num in num_dic[key]:
                for num2 in num_dic[-key]:
                    sums.add(num+num2)
        if -key-1 in num_dic:
            for num in num_dic[key]:
                for num3 in num_dic[-key-1]:
                    candidate = num+num3 
                    if candidate >=-10000:
                        sums.add(num+num3)
        if -key+1 in num_dic:
            for num in num_dic[key]:
                for num4 in num_dic[-key+1]:
                    candidate = num+num4 
                    if candidate <= 10000:
                        sums.add(num+num4)
                    
        
    
