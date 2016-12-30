from numpy import inf
def Minimumjumptoreachend(array):
    temp_arry_jumps=[]
    temp_array_locator=[]
    for x in range(len(array)):
        temp_arry_jumps.append(inf)
        temp_array_locator.append(0)
    temp_arry_jumps[0]=0
    i=1
    j=0
    while(i<len(array)):
        while(i!=j):
            temp_tracker=temp_arry_jumps[i]
            if array[j]>=(i-j):
                temp_arry_jumps[i]=min(temp_arry_jumps[i],1+temp_arry_jumps[j])
            
            if temp_tracker != temp_arry_jumps[i]:
                temp_array_locator[i]=j
            j+=1
        i+=1
        j=0
    path=[]
    X=len(array)-1
    path.append(X)
    minJumps=temp_arry_jumps[X]

    while(temp_array_locator[X]!=0):
        X=temp_array_locator[X]
        path.append(X)
    path.append(0)
    path.reverse()
    print "1.To print Min no of Jumps and Path\n2.Return the values of Mincost and path"
    choice=int(raw_input())
    if choice == 1:
        print "\nMinJumps of Traveling: "+str(minJumps)
        print "Path:"
        for i in range (len(path)):
            print " -> "+str(path[i]),
    
    elif choice == 2: 
        print "Returned"
        return minJumps,path
print "Enter the Jump - Cost Array ( space separated ):"

array=map(int ,raw_input().strip().split(" "))
Minimumjumptoreachend(array)
        
