s=input("Enter string")
print(len(s))
"""i=1
l=[]
count=0
for i in range (1,300):
    t=s[0:len(s)-i]
    for j in range (i,len(s)):
        if s[j]==t[j-i]:
            count+=1
    l.append(count)
    count=0
    print(t)
print(l)"""
ltr_freq=[0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
strr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#ltr_freq=[]
#for i in range(0,26):
    #ltr_freq.append(s.count(strr[i]))
key=[]
for l in range(0,8):
    result=[]
    lr=[]
    freq=[]
    freq2=[]
    temp=[]
    sumfreq=0
    for j in range(l,len(s),8):
        lr.append(s[j])
    for j in range(0,26):
        freq.append(lr.count(strr[j]))
    #for l in range(0,26):
    sumfreq=sum(freq)
    for j in range(0,len(freq)):
        freq2.append(freq[j]/sumfreq)
    for j in range(0,len(freq)):
        temp=freq[j:len(freq)]+freq[0:j]
        add=0
        for k in range (0,len(freq)):
            add+=temp[k]*ltr_freq[k]
        result.append(add)
    for i in range(0,len(result)):
        if(result[i]==max(result)):
            key.append(i)
            break
print(key)
        
    
                    
    

    
