result = 100
substrack = 4
looping = 8
for i in range(8):
    print(result, end=', ' if i < looping - 1 else '')
    result -= substrack
    substrack += 4