def solution(n):
    cnt = 0
    for start in range(1, n+1):
        sum = 0
        for i in range(start, n+1):
            sum += i
            if sum == n :
                cnt += 1
                break
            elif sum > n :
                break
            
    return cnt