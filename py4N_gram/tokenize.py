def Ngram(x,n):
    x=x.split()
    temp=[]
    for i in range(len(x)-n+1):
        temp.append(x[i:n+i])
        temp[i]=" ".join(temp[i])
    return temp
