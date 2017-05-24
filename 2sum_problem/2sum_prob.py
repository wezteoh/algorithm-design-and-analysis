import time

num_set = set()
with open("prob-2sum.txt") as f:
    for line in f:
        num = line.split()
        num = int(num[0])
        num_set.add(num)

numlist = list(num_set)
count = 0

lower_bound = -10000
upper_bound = 10000


start = time.time()
for i in range(lower_bound,upper_bound+1):
    sum_appear = False
    num_processed = 0
    while sum_appear == False and num_processed < len(num_set):
        diff = i - numlist[num_processed]
        if diff != numlist[num_processed] and diff in num_set:
            sum_appear = True
        num_processed += 1
    count+=sum_appear

end = time.time()
print(end - start)
