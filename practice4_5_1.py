temp = list()
count = 0
ans = True
while ans == True:
    key = input("データの入力をしますか？（y/n)＞＞")
    if key == "y":
        data = float(input(f"{count + 1}個目のデータを入力＞＞"))
        temp.append(data)
        count += 1
    elif key == "n":
        print("入力を終了します")
        ans = False

for count in range(len(temp)):
    print(f"{count + 8}時 {temp[count]}度")

temp_new = list()
for count in range(len(temp)):
    if count == 5:
        temp_new.append("N/A")
    else:
        temp_new.append(temp[count])
print(temp)
print(temp_new)

total = 0
for data in temp_new:
    if isinstance(data,float):
       total = total +data
print(total / (len(temp_new)-1))
