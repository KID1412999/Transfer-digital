import re
def convert(t):
    l={'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}
    s=['十','百','千','万']
    n=t
    m=[l[i] for i in str(n)]
    w=''
    for i in range(len(m)-1):
        #print(m[i],(len(m)-1)%4-(i+1)%len(s))
        w+=m[i]+s[(len(m)-1)%4-(i+1)%len(s)]
    #print(w)
    w=w.replace('十零','十')
    while len(re.findall('(零零|零百|零千|零万)',w))>=1:
        w=re.sub('(零零|零百|零千|零万)','零',w)
    if w.count('万')>=2:
        w=w.replace('万','亿',1)
    if w[-1]=='零':
        w=w[:-2]
    w=w.replace('一十','十')
    print(w)
    if name='__main__':
        convert(1020160)
