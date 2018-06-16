def merge(larr,rarr):
	result =[]
	i,j=0,0
	count=0
	while i<len(larr) and j<len(rarr):
		if larr[i]<= rarr[j] :
			result.append(larr[i])
			i+=1
		else:
			count += len(larr[i:])  #no of elements remaining in larr
			result.append(rarr[j])
			j+=1
	result += larr[i:]				#Do not forget to append all the remaining elements too
	result += rarr[j:]
	return result, count

def mergesort(arrlr):
	if len(arrlr) < 2:
		return arrlr, 0			#Do not forget the base condition again
	mid = int(len(arrlr)/2)
	larr,count1 = mergesort(arrlr[:mid])
	rarr, count2 = mergesort(arrlr[mid:])
	L, r1 = merge(larr,rarr)
	r = count1 + count2 + r1	#Count all the inversions and update r
	return L, r

num = input("Enter no of elements in array")
arr=list()
i=0
arr=[int(x) for x in input().split()]
arr1, cnt = mergesort(arr)	#mergesort([1,4,3,2,5])print(arr1)
print(cnt)

#Complexity O(nlogn)
#Sample input 7 8 9 1 2 3  Answer 9
#Sample input 1,4,3,2,5 Answer 3
