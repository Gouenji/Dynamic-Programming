def doNotOverlap(job1,job2):
    if job1[0] < job2[0] and job2[1] < job1[1] :
        return 0
    if job2[0] < job1[0] and job1[1] < job2[1] :
        return 0
    if job1[1] > job2[0] and job1[0]<job2[0]:
        return 0
    if job2[1] > job1[0] and job2[0]<job1[0]:
        return 0
    else:
        return 1
from operator import itemgetter   

def WeightedJobScheduling(Jobs):

    sorted(Jobs,key=itemgetter(1))
    temp_array=[]
    temp_locator=[]
    for k in range(len(Jobs)):
        temp_array.append(Jobs[k][2])
        temp_locator.append(0)
    i=1
    j=0
    while(i<len(Jobs)):
        while(i!=j):
            temp_tracker=temp_array[i]
            if doNotOverlap(Jobs[i],Jobs[j]):
                temp_array[i]=max(temp_array[i],temp_array[j]+Jobs[i][2])
            if temp_array[i] != temp_tracker:
                temp_locator[i]=j
            j+=1
        i+=1
        j=0
    maxCost=max(temp_array)
    index=temp_array.index(maxCost)
    temp_maxCost=maxCost
    jobsindices=[]
    jobs=[]
    while temp_maxCost>0:
        jobsindices.append(index)
        temp_maxCost-=Jobs[index][2]
        index=temp_locator[index]
    jobsindices.reverse()
    for itr in range(len(jobsindices)):
        jobs.append(Jobs[jobsindices[itr]])

    return jobs,maxCost

Jobs=[]
n=int(raw_input("Enter the No of Jobs:\n"))
print "Enter jobs Start-Time  End-Time Cost"
for i in range(n):
    jobs=map(int,raw_input().strip().split(" "))
    Jobs.append(jobs)
jobs,maxCost = WeightedJobScheduling(Jobs)
for itr in range(len(jobs)):
    print "Start Time: " + str(jobs[itr][0]) + "  End Time: " + str(jobs[itr][1]) + "   Cost: "+str(jobs[itr][2])
print "Total Cost:  "+str(maxCost)

    