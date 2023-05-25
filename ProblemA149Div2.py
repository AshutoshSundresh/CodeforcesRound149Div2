num = int(input())

for i in range(num):
    x, k = map(int, input().split())
    
    if x % k == 0:
        # Two steps: x-1 and 1
        n = 2
        moves = [x-1, 1]
    else:
        # One step: x
        n = 1
        moves = [x]
    
    # Print the number of moves
    print(n)
    
    # Print the moves in a single line
    print(" ".join(map(str, moves)))
