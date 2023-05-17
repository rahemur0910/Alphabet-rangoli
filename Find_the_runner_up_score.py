def second_largest(arr,n):
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

    second_high = 0
    for i in range (n-2,-1,-1):
        if arr[i] != arr[n-1]:
            second_high = arr[i]
            break

    print(second_high)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    second_largest(arr,n)