def missing_number(arr, n):
    total = n * (n+1) // 2

    arrsum = sum(arr)

    missing = total - arrsum
    print(missing)

arr = [1,2,3,4,6,7,8]

missing_number(arr, 8)