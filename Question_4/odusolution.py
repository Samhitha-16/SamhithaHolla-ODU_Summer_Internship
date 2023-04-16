str = input('enter the string:')
def repeating_string(str):
    n = len(str)
    a = [[0 for j in range(n+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and str[i-1] == str[j-1]:
                a[i][j] = a[i-1][j-1] + 1
            else:
                a[i][j] = max(a[i-1][j], a[i][j-1])
    return a[n][n]
print(repeating_string(str))

