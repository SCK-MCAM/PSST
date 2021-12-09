import numpy as np
import sys
from dll import CTTenc, CTTdec

if len(sys.argv) == 4:
    
    ctNpArray = np.load(sys.argv[3])

    i = 0
    j = 0
    ctDic = {}

    for i in range(9): # X座標カウント
        for j in range(9): # Y座標カウント
            ctDic[ctNpArray[i][j]] = str(i)+str(j)
            ctDic[str(i)+str(j)] = ctNpArray[i][j]
    if sys.argv[2] == 'e':
        print(str(np.base_repr(int(CTTenc(sys.argv[1], ctDic)), 36)))
    elif sys.argv[2] == 'd':

        print(CTTdec(str(int(sys.argv[1],36)), ctDic))
    else:
        print('ERROR: 引数が不正')
        quit()
else:
    print('ERROR: 引数が不正')