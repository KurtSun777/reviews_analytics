data = []
count = 0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))

print('there are', len(data), 'datas')

print(len(data[0]))

sum_len = 0
for length in data:
    sum_len += len(length)
    
print('Total analytics are', sum_len)
print('average analytics are', sum_len / len(data))

new = []

for length in data:
    if len(length) < 100:
        new.append(length)
print('there are', len(new), 'datas which len < 100')
print(new[0])
