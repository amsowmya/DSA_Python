def add_number(arr, n):
    values = ()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i]+arr[j] == n:
                print(arr[i], arr[j])


arr = [2,7,1,2,8,9,0,7]
add_number(arr, 9)