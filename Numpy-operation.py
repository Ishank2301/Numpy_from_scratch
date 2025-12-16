#Let's try Two Sum problem of LC

def two_sum(arr, target):

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return True
            
    return False
            
arr = [2,3,4,7,9,0]
target = 9

print(two_sum(arr, target))
        