x = 1
y = 1
numbers = [x,y]
count = 0
data = sum(numbers)
while data <=1000:
    numbers.append(data)
    data = data + numbers[count+1]
    count += 1
print(numbers )

ratius = list()
for count in range(len(numbers)):
    if count == len(numbers) - 1:
        break
    ratius.append(numbers[count+1] / numbers[count])
print(ratius)

for count in range(len(ratius)):
    ratius[count] = int(ratius[count] * 1000) / 1000
    print(ratius)