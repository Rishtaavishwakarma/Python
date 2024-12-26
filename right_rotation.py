def right_circular(arr, k, indices):
    n = len(arr)

    def rotate_once(arr):
        last_element = arr[-1]
        for i in range (n-1, 0, -1):
            arr[i]= arr[i-1]
        arr[0] = last_element
    
    for i in range(k):
        rotate_once(arr)

    result = [arr[i] for i in indices]
    return result

arr = list(map(int,input("Enter intergers").split()))
k = int(input("Enter number rotations "))
indices = list(map(int,input("Enter index you want").split()))

result = right_circular(arr,k,indices)
print(result)
