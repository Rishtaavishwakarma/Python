def find_rooms(N,K,coins):
    start , end, current_sum=0,0,0
    result_start, result_end =0,float('inf')

    while end < N:
        current_sum += coins[end]

        while current_sum > K:
            current_sum -= coins[start]
            start += 1

        if current_sum == K:
            if end - start < result_end - result_start :
                result_start, result_end = start, end

        end += 1

    if result_end == float('inf'):
        return "No solution found"
    else:
        return result_start + 1, result_end +1
    
N = int(input("Enter Number of rooms: "))
K = int(input("Enter Value of K: "))
coins = list(map(int, input().split()))   

result = find_rooms(N,K,coins)
print("Enter room no", result[0],"and exit room",result[1])

 
        