def selection(arr, count):
	 for  i in range(count):
	 	least = i
	 	for j in range(i+1, count):
	 		if(arr[j] < arr[least]):
	 			least = j
	 	arr[i], arr[least] = arr[least], arr[i]
	 return arr


def bubble(arr,count):
	for i in range(count):
		flag = False
		for j in range(i+1, count-1):
			if(arr[i] > arr[j]):
				arr[i], arr[j] = arr[j], arr[i]
				flag = True
		if flag is False:
			break
	return arr

def insertion(arr, count):
	for i in range(1, count):
		key = arr[i]
		j = i - 1
		while i >= 0 and arr[j] > key:
			arr[j+1] = arr[j]
			j = j - 1
		arr[j + 1] = key
	return arr

def counting(arr, count):
	high = max(arr)+1
	cnt = [0]*high
	values=[]
	for i in arr:
		cnt[i] += 1
	for j in range(len(cnt)):
		values.extend([j] * cnt[j])
	return values

def shellSort(arr):
    n = len(arr)
    gap = int(n/2)
    while gap > 0:
        for i in range(int(gap),n):
        	temp = arr[i]
        	j = i
        	while j >= gap and arr[j-int(gap)] > temp:
        		arr[j] = arr[j-gap]
        		j -= gap
        	arr[j] = temp
        gap /= 2
    return arr
A = [64, 34, 25, 12, 22, 11, 90]
count = len(A)
print(selection(A, count))
print(bubble(A, count))
print(insertion(A, count))
print(counting(A, count))
print(shellSort(A))

