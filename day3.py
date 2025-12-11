def day3(data: str):
    batteries = data.split('\n')
    ans = 0
    digits = 12
    for battery in batteries:
        print(battery)
        ans += findMaxNumber(battery, (len(battery)-1)-(digits-1), 0, digits-1)
    print(ans)
    return ans

def findMaxNumber(battery: str, startIndex: int, endIndex: int, digit: int) -> int:
    if digit == -1:
        return 0
    max = 0
    for i in range(startIndex, endIndex-1, -1):
        if int(battery[i]) >= max:
            max = int(battery[i])
            endIndex = i+1
    print(max * 10**digit)
    return max * 10**digit + findMaxNumber(battery, startIndex+1, endIndex, digit-1)