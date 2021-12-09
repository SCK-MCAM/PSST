import random
import datetime
import numpy as np
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

ctList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")", "[", "]", "<", ">", "@", "=", "+", "-", "/", ",", ".", "!", "?", "#", "$", "%", "&", "~", "^", "_", "'", "≪AR≫", "≪AS≫", "≪BK≫", "≪CFM≫", "≪COL≫", "≪NO≫", "≪NW≫", "≪OK≫", "≪PSE≫", "≪RQ≫", "≪RPT≫", "≪SVC≫", "≪TFC≫", "≪DE≫", "≪TU≫", "≪TXT≫", "≪VA≫", "≪KA≫", "≪SPACE≫", "≪QSU≫", "≪QSW≫", "≪QSX≫"]
#print(len(ctList))
ctShuffledList = random.sample(ctList, len(ctList))
#print(ctShuffledList)

ctArray = [[],[],[],[],[],[],[],[],[]]
LoopCount = 0

for i in range(9): # X座標カウント
    for j in range(9): # Y座標カウント
        ctArray[i].append(ctShuffledList[LoopCount])
        #print(f'[{i}][{j}] = {ctShuffledList[LoopCount]}')
        LoopCount += 1

#print(ctArray)
ctNpArray = np.array(ctArray)

d = int(now.strftime('%y%m%d%H%M%S'))
e = str(np.base_repr(d, 36))

np.save('psst_'+e, ctNpArray)