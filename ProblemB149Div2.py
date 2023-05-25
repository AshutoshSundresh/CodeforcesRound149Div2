n = int(input())  

for i in range(n):
    num = int(input())
    s = input()  
    
    max_len = 1  # maximum length of consecutive subarray
    cur_len = 1  # current length of consecutive subarray
    
    # Iterate through the string and update the lengths
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cur_len += 1
        else:
            max_len = max(max_len, cur_len)
            cur_len = 1
    
    # Check if the last subarray is longer than the previous maximum
    max_len = max(max_len, cur_len)
    
    # Print the maximum length
    print(max_len + 1)
