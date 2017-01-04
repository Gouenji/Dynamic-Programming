print ("Enter the array to find Maximum Sum Increasing Subsequence (space separated)")
a=map(int,raw_input().strip(' ').split(' '))
from copy import copy
def MaximumSumIncreasingSubsequence(array):
    max_sum_array=copy(array)
    actual_sequence=[]
    for i in range(len(array)):
        actual_sequence.append(i)   
    j=0
    i=1
    while(i<len(array)):
        while(j!=i):
            temp=max_sum_array[i]
            if array[j]<array[i]:
                max_sum_array[i]=max(array[i]+max_sum_array[j],max_sum_array[i])
            if max_sum_array[i]!=temp:
                actual_sequence[i]=j
            j+=1
        j=0
        i+=1
    maxSum=max(max_sum_array)
    temp_sum=maxSum
    position_max_sum=max_sum_array.index(maxSum)
    #print actual_sequence
    #print max_sum_array
    sequence=[]
    while(temp_sum > 0):
        sequence.append(array[position_max_sum])
        temp_sum-=array[position_max_sum]
        position_max_sum=actual_sequence[position_max_sum]
    sequence.reverse()
    print "1.To print Maximum Sum Increasing Subsequence and Max Sum\n2.Return the values of  Max Sum and Maximum Sum Increasing Subsequence "
    choice=int(raw_input())
    if choice == 1:
        print "\nMax Sum: "+str(maxSum)
        print "Sequence:"
        for i in range (len(sequence)):
            print " "+str(sequence[i]),
    
    elif choice == 2: 
        print "Returned"
        return sequence,maxSum
MaximumSumIncreasingSubsequence(a)        
