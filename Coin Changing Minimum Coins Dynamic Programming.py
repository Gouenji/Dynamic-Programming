from numpy import inf

coins=map(int,raw_input("Enter Denominations:\n").strip().split(" "))
total=int(raw_input("Enter total:\n"))


def CoinChangingMinimumCoinsDynamicProgramming(coins,total):
    temp_total=total

    minDenomination=min(coins)
    if total<minDenomination:
        print "! Possible"
        return
    list_1=[]
    list_2=[]
    dic_coins={}
    list_1.append(0)
    list_2.append(-1)
    for j in range(len(coins)):
        dic_coins[coins[j]]=0
    for i in xrange(1,temp_total+1):
        list_1.append(inf)
        list_2.append(-1)
    for j in range(len(coins)):
        i=0
        while(i<temp_total+1):
            temp=list_1[i]
            if i>=coins[j]:
                list_1[i]=min(list_1[i],1+list_1[i-coins[j]])
            if list_1[i]!=temp:
                list_2[i]=j
            i+=1
    while(temp_total>0):
        dic_coins[coins[list_2[temp_total]]]+=1
        temp_total-=coins[list_2[temp_total]]
    return dic_coins

while(total!=-1):
    Denominations=CoinChangingMinimumCoinsDynamicProgramming(coins,total)
    print "Denominations::::\nCoins-No."
    for j in range(len(Denominations)):
        print str(coins[j])+ " - " +str(Denominations[coins[j]])
    total=int(raw_input("Enter total (-1 to stop):\n"))

        
    
