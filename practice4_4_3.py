for num1 in range(9):
   for num2 in range(9):
        ans = ((num1 + 1) * (num2 + 1))
        if ans < 50 and ans % 2 == 1:
                print(f"{num1 + 1} × {num2 + 1} = {ans}")
        elif ans >= 50:
             continue
