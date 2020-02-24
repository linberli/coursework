import random
def select (arr, dim):
    alg_count=[0,0]
    for i in range(0,dim-1):
        first= arr[i]
        minindex=i
        for j in range(i+1,dim):
            alg_count[0]+=1
            if arr[minindex]>arr[j]:
                minindex=j
                alg_count[1]+=1
        arr[i],arr[minindex]=arr[minindex],arr[i]
    return alg_count
a= [1,2,3,4,5]
random.shuffle(a)
b = 5
select(a,b)

