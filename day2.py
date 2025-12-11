def day2(data: str):
    IDranges = data.replace('\n', '').split(',')

    ans = 0
    for IDrange in IDranges:
        start, end = IDrange.split('-')
        start = int(start)
        end = int(end)
        for IDnum in range(start, end + 1):
            ID = str(IDnum)
            if isContinuous(ID, 1):
                ans += IDnum
                print(IDnum)
    print(ans)

def isContinuous(ID: str, subNum: int) -> bool:
    sub = ID[:subNum]
    nextIndex = ID.find(sub, subNum)
    if nextIndex == -1:
        return False
    maxTimes = len(ID)//len(sub)
    if len(sub*maxTimes) > len(ID):
        return False
    if sub*maxTimes == ID:
        return True

    return isContinuous(ID, subNum+1)
