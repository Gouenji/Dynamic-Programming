def LongestIncreasingSubsequence(array):
    temp_array=[]
    temp_locator=[]
    for i in range(len(array)):
        temp_array.append(1)
        temp_locator.append(0)
    i=1
    j=0
    while i<len(array):
        temp_tracker = temp_array[i]
        while(i!=j):
            temp_tracker = temp_array[i]
            if array[i] > array[j]:
                temp_array[i] = max(temp_array[i],1+temp_array[j])   
            if temp_array[i] != temp_tracker:
                temp_locator[i] = j
            j+=1
        i+=1
        j=0
    lengthLCS=max(temp_array)
    index=temp_array.index(lengthLCS)
    temp_length=lengthLCS
    LCS=[]
    while temp_length>0:
        LCS.append(array[index])
        index=temp_locator[index]
        temp_length-=1
    LCS.reverse()   
    return lengthLCS,LCS
array=map(int,raw_input("Enter the sequence:\n").strip().split(" "))
length,LCS=LongestIncreasingSubsequence(array)
print "\nLength Of Longest Increasing Subsequence: "+str(length)+"\n\nSequence:"
print LCS
