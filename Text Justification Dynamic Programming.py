from numpy import inf
def Line2Word(Line):
    Words=[]
    length=0
    start=0
    end=0
    for x in range(len(Line)):
        if Line[x] == ' ' or Line[x] == '.' :
            word=Line[start:end]
            Words.append([word,end-start])
            start=end+1
        end+=1
    return Words
def Cost_Matrix(Words,width):
    temp_array={}
    for i in range(len(Words)):
        for j in xrange(i,len(Words)):
            word_len_sum=0
            for k in range(i,j+1):
                word_len_sum+=len(Words[k][0])
            word_len_sum+=(j-i)
            if width-word_len_sum < 0:
                temp_array[str(i)+str(j)]=inf
            else:
                temp_array[str(i)+str(j)]=(width-word_len_sum)**2
    return temp_array


def TextJustificationDynamicProgramming(Line,width):
    Words=Line2Word(Line)
    temp_array = Cost_Matrix(Words,width)
    temp_array_1={}
    temp_array_2={}
    lines={}
    i=len(Words)-1
    j=len(Words)-1
    while(i>=0):
        if temp_array[str(i)+str(j)] == inf :
            Min=inf
            for k in range(len(Words)-1,i,-1):
                if temp_array_1[k] + temp_array[str(i)+str(k-1)] < Min:
                    Min=temp_array_1[k] + temp_array[str(i)+str(k-1)]
                    temp_array_2[i]=k   
            temp_array_1[i]=Min
            i-=1
            j=len(Words)-1  
        else:
            temp_array_1[i]=temp_array[str(i)+str(j)]
            temp_array_2[i]=j+1
            i-=1
    key=0
    lno=0
    while(key<len(Words)):
        lines[lno]=''
        for k in range(key,temp_array_2[key]):
            lines[lno]+=' '+Words[k][0]
        lno+=1
        key=temp_array_2[key]
    lines[lno-1]+='.'
    return lines

def justified(text):
    para={}
    pno=0
    start=end=0
    for it in range(len(text)):
        if text[it] == '.':
            line=text[start:it+1]
            start=it+1
            para[pno]=TextJustificationDynamicProgramming(line,10)
            pno+=1
    print "Justified Text:\n "
    for Key in para.keys():
        for key in para[Key].keys():
            print para[Key][key]
        print " "

text=raw_input("Enter text:\n")
justified(text)
    
        
