def day1(data: str):
    steps = data.split('\n')
    ans = 0
    position = 50
    for step in steps:
        num = int(step[1:])
        if step[0] == 'L':
            num *= -1

        nextMove = position + num

        if (position > 0 and nextMove <= 0) or (position < 0 and nextMove >= 0):
            ans += 1

        position = nextMove
        if abs(position) >= 100:
            ans += abs(int(position / 100))
            if position < 0:
                position = position % -100
            else:
                position = position % 100
                
        print(step, num, position)
    print(ans)