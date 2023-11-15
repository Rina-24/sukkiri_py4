age = [28,50,8,20,78,25,22,10,27,33]
num = 5
sample = list()
for age in ages:
    if 20 <= age < 30:
        if len(sample) < num:
            sample.append(age)
print(sample)