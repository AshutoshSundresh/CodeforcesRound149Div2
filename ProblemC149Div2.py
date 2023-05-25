def get_final_string(s):
    n = len(s)
    final_string = list(s)
    
    curr = '0'  # Current value
    
    # Traverse the string and replace '?' with the current value
    for i in range(n):
        if final_string[i] == '?':
            final_string[i] = curr
        else:
            curr = final_string[i]  # Update the current value
    
    return ''.join(final_string)


n = int(input())
for i in range(n):
    string = input()
    print(get_final_string(string))
