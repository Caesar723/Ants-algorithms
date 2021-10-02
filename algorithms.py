import numpy
import random
import  time
import  pandas
import numpy as np
map=numpy.zeros((10,10))
map[0][0]=1
map[9][9]=1
c=[3,5,7,2,8,3,1,1,3,5,3,4,6,6,9]
r=[3,4,2,1,4,6,4,6,8,3,4,7,9,7,4]
for i in range(len(c)):
        map[c[i]][r[i]]=2
#sign=numpy.zeros((10,10))
sign=numpy.zeros((100,100))
#sign=pandas.read_csv('ants.csv')

ant=[0,0]
c=0
pre=0
def uniquelist(list):
    arr=[]
    for i in list:
        if not (i in arr):
            arr.append(i)
    return arr
def ranc(list,indexV):
    arr=[]
    for i in range(len(list)):
        if list[i]==indexV:
            arr.append(i)
    return arr[random.randint(0,len(arr)-1)]
def check(m):
    a=random.randint(0,3)
    if m[a]==-1:
        return check(m)
    else:
        return a
def Df2Lis(data):
    if type(data)==list or type(data)==range or type(data)==np.ndarray:
        #print(list(data))
        return list(data)
    else:
        arr=[]
        arr2=[]
        for i in range(len(data[list(data)[0]])):
            for ii in range(len(data[list(data)])):
                arr2.append(data[list(data)[ii]][i])
            #arr2.append(data[list(data)[1]][i])
            #arr2.append(100)
            arr.append(arr2)
            arr2=[]
        return arr
sign=Df2Lis(pandas.read_csv('ants.csv'))
#print(Df2Lis(sign))
def chooseA(x,y):
    a=[]

    if x - 1 <= -1 or map[ant[1]][ant[0]-1]==2:
        a.append(-1)
        #print(map[ant[1]][ant[0]-1])
    else:
        a.append(sign[int(str(y)+str(x-1))][int(str(y)+str(x))])
    if x + 1 >= 10 or map[ant[1]][ant[0]+1]==2:
        a.append(-1)
    else:
        #print(x,y)
        a.append(sign[int(str(y)+str(x+1))][int(str(y)+str(x))])
    if y - 1 <= -1 or map[ant[1]-1][ant[0]]==2:
        a.append(-1)
    else:
        a.append(sign[int(str(y-1)+str(x))][int(str(y)+str(x))])
    if y + 1 >= 10 or map[ant[1]+1][ant[0]]==2:
        a.append(-1)
    else:
        a.append(sign[int(str(y+1)+str(x))][int(str(y)+str(x))])
    if random.random()<=0.8 :
        ma=max(a)
        #print(ma)
        ma=ranc(a,ma)
        return ma
    else:

        return check(a)
num=0
while c<=5000:
    run=True
    path=[]
    ok=False
    ant=[0,0]
    while run:
        istate=ant.copy()
        Act=chooseA(ant[0],ant[1])
        #print(Act)
        if Act==0:
            ant[0]-=1
        elif Act==1:
            ant[0]+=1
        elif Act==2:
            ant[1]-=1
        elif Act==3:
            ant[1]+=1
        m=map.copy()
        m[ant[1]][ant[0]]=999
        #print(m)
        #time.sleep(0.3)
        path.append([int(str(istate[1])+str(istate[0])),int(str(ant.copy()[1])+str(ant.copy()[0]))])
        #print(len(path))
        if ant==[9,9]:
            run=False
            ok=True
        if len(path)>=300:
            run=False
    #print(path)
    if ok==True:
        #print(path)
        path=uniquelist(path)
        #print(path)
        for ii in path:
            sign[ii[1]][ii[0]]+=1
        for iii in range(10):
            for iiii in range(10):
                sign[iiii][iii]-=0.2 if sign[iiii][iii]>0 else 0
        #print(sign)
        num+=1
    c+=1
    print(len(path))
pd=pandas.DataFrame(sign)
pd.to_csv('ants.csv',index=False)
#print(list(sign))
print(num)