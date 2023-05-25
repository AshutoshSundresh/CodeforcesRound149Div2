num = int(input())

for i in range(num):
    n = int(input())
    s = input()
    balance = 0

    for i in range(n):
        balance = balance + 1 if s[i] == '(' else balance - 1

    if balance != 0:
        print("-1")
        continue

    color_count = 0
    min_color = 0

    for i in range(n):
        min_color = min_color + 1 if s[i] == '(' else min_color - 1
        if min_color < 0:
            color_count += 1
            break

    min_color = 0

    for i in range(n):
        min_color = min_color + 1 if s[i] == ')' else min_color - 1
        if min_color < 0:
            color_count += 1
            break

    if color_count < 2:
        print("1")
        for _ in range(n):
            print("1", end=" ")
        print()
    else:
        colors = [0] * n
        left = 0
        right = n - 1

        while left < right:
            if s[left] == ')' and s[right] == ')':
                colors[left] = 2
                colors[right] = 1
                left += 1
                right -= 1
            elif s[left] == '(' and s[right] == '(':
                colors[left] = 1
                colors[right] = 2
                left += 1
                right -= 1
            elif s[left] == ')' and s[right] == '(':
                colors[right] = 2
                colors[left] = 2
                left += 1
                right -= 1
            else:
                colors[left] = 1
                colors[right] = 1
                left += 1
                right -= 1

        print("2")
        for color in colors:
            print(color, end=" ")
        print()
