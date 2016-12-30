from copy import copy

def MinimumCostPathDynamicProgramming(array,m,n):
    temp_array=[]
    #fill first row
    temp_array=copy(array)
    for y in range(n-1):
        temp_array[0][y+1]+=temp_array[0][y]
    #fill first column
    for x in range(m-1):
        temp_array[x+1][0]+=temp_array[x][0]

    for x in xrange(1,m):
        for y in xrange(1,n):
            temp_array[x][y]+=min(temp_array[x-1][y],temp_array[x][y-1])
    I=m-1
    J=n-1
    minCost=temp_array[I][J]
    path=[]
    while(I!=0 or J!=0):
        path.append([I+1,J+1])
        if temp_array[I-1][J] < temp_array[I][J-1]:
            I=I-1
        elif temp_array[I][J-1] < temp_array[I-1][J]:
            J=J-1
    path.append([1,1])
    path.reverse()
    
    print "1.To print Mincost and Path\n2.Return the values of Mincost and path"
    choice=int(raw_input())
    if choice == 1:
        print "\nMinCost of Traveling: "+str(minCost)
        print "Path:"
        for i in range (len(path)):
            print " -> "+str(path[i]),
    
    elif choice == 2: 
        print "Returned"
        return minCost,path


print "Enter m-row, n-column"
m,n=map(int,raw_input().strip().split(" "))
array=[]
print "Enter cost-Elements of array"
for x in range(m):
    row=map(int ,raw_input().strip().split(" "))
    array.append(row)
MinimumCostPathDynamicProgramming(array,m,n)
