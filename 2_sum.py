
# two sum python solution  


def towSum(arr , target):
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            if arr[i] + arr[j] == target:
                return [i , j]
    return []

arr = [11,3,7,9,14,2]
target = 17
result = towSum(arr , target)

print(result)

# Ans to be [1 , 4]

def twoNumberSum(array, targetSum):
    matches = {}
    for number in range(len(array)):
        match = targetSum - array[number]
        if match in matches:
            return [match, array[number] ]
        else:
            matches[array[number]] = True
    return []

array = [11,3,7,9,14,2]
targetSum = 17
results = twoNumberSum(array , targetSum)
print(results)

# Ans to be [3, 14]
