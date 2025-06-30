result = 40
substrack = 1
looping = 8
for i in range(8):
    print(result, end=', ' if i < looping - 1 else '\n')
    result -= substrack
    substrack += 2