import numpy as np

def CTTenc(testStr, ctDic):
    testStr = testStr.replace(" ", "<SPACE>")
    normalCodeList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")", "[", "]", "<", ">", "@", "=", "+", "-", "/", ",", ".", "!", "?", "#", "$", "%", "&", "~", "^", "_", "'"]
    exCodeList = ["≪AR≫", "≪AS≫", "≪BK≫", "≪CFM≫", "≪COL≫", "≪NO≫", "≪NW≫", "≪OK≫", "≪PSE≫", "≪RQ≫", "≪RPT≫", "≪SVC≫", "≪TFC≫", "≪DE≫", "≪TU≫", "≪TXT≫", "≪VA≫", "≪KA≫", "≪SPACE≫", "≪QSU≫", "≪QSW≫", "≪QSX≫"]
    afterCodeStr = ""
    tmpStr = ""
    wpc = 0 # WhileProcessCount

    while len(testStr) > wpc:
        if testStr[wpc] == "≪":
            tmpStr = "≪"
            wlc = 1
            while True:
                if len(testStr) < (wpc + wlc):
                    print("ERROR: 構文が異常")
                    quit()
                elif testStr[wpc + wlc] == "≫":
                    tmpStr += "≫"
                    break
                else:
                    tmpStr += testStr[wpc + wlc]
                    wlc += 1
                
            if tmpStr in exCodeList:
                afterCodeStr += ctDic[tmpStr]
                #print(tmpStr)
                wpc += len(tmpStr)
            else:
                print("ERROR: 構文が異常")
                quit()
        elif testStr[wpc] in normalCodeList:
            afterCodeStr += ctDic[testStr[wpc]]
            #print(testStr[wpc])
            wpc += 1
        else:
            print("ERROR: 構文が異常")
            quit()
    afterCodeStr = CTTshift(afterCodeStr, "+")
    return afterCodeStr

def CTTdec(testStr, ctDic):
    testStr = CTTshift(testStr, "-")
    afterCodeStr = ""
    wpc = 0
    tmpStr = ""

    while len(testStr) > wpc:
        tmpStr = testStr[wpc]+testStr[wpc+1]
        #print(tmpStr)
        if tmpStr in ctDic:
            afterCodeStr += ctDic[tmpStr]
            #print(ctDic[tmpStr])
            wpc += 2
        else:
            print("ERROR: 構文が異常")
            quit()
    afterCodeStr = afterCodeStr.replace("<SPACE>", " ")
    return afterCodeStr

def CTTshift(cnvStr, modeStr):
    aftStr = ""
    if modeStr == '+':
        for i in range(len(cnvStr)):
            aftStr += str(int(cnvStr[i])+1)
    elif modeStr == '-':
        for i in range(len(cnvStr)):
            aftStr += str(int(cnvStr[i])-1)
    return aftStr