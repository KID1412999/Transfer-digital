#递归解法
def convert(n):
    global s,k,w,l
    if len(n)>1:
        #print(n[1:],'--',n[0])
        convert(n[1:])
        convert(n[0])
    else:
        #print(len(s),len(s)-1,w[(len(s)-1)%4],n,l[n],'-->>>')
        if len(s)-1>=0:
            k+=w[(len(s)-1)%4]
        s+=l[n]
def transfer(number):
    import re
    global s,k,w,l
    s=''
    k=''
    l={'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}
    w=['十','百','千','万']
    i=0
    convert(number)
    t=list(zip(list(reversed([i for i in s])),list(reversed([i for i in k]))))
    t.append(('',list(reversed([i for i in s]))[-1]))
    c=''
    #print(c,1)
    for i in t:
        for j in i:
            if i==('零', '千') or i==('零', '百') or i==('零', '十'):
                c+='零'
                continue
            elif i==('零', '万'):
                c+='万'
                continue
            c+=j
    #print(c,2)
    while len(re.findall('(万万)',c))>=1:
        c=re.sub('(万万)','万',c)
    #print(c,3)
    while len(re.findall('(零零)',c))>=1:
        c=re.sub('(零零)','零',c)
    #print(c,4)
    x=0
    b=''
    for i in range(len(c)):
        if c[-i-1]=='万':
            x+=1
            if x==2:
                v='亿'
            elif x<=1:
                v=c[-i-1]
            b+=v
        else:
            b+=c[-i-1]
    kj=''.join(list(reversed([i for i in b])))
    if kj[-1]=='零':
        print(kj[:-1])
    else:
        print(kj)
   if __name=='__main__':
        transfer(1463154')
