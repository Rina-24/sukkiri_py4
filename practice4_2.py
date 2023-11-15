count = 1
ans = True
print("カレーを召し上がれ")
while ans == True:
    print(f"{count}皿のカレーを食べました")
    key = input("おかわりはいかがですか？(y/n)＞＞")
    if key == "y":
        ans = True
        count +=1
    elif key == "n":
        ans = False
print("ごちそうさまでした。")
    
