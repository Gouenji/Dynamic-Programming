def CountNumberofBinaryTreePossiblegivenPreorderSequencelength(sequence):
    n=len(sequence)
    temp_array=[]
    temp_array.append(1)
    temp_array.append(1)    
    for i in range(2,n+1):
        temp_array.append(0)
    for i in range(2,n+1):
        for j in range(i):
            temp_array[i]+=temp_array[j]*temp_array[i-j-1]
    return temp_array[n]
sequence=map(int,raw_input().strip().split(" "))
print "Number of Binary Tree Possible given Preorder Sequence length: \n"+str(CountNumberofBinaryTreePossiblegivenPreorderSequencelength(sequence))
