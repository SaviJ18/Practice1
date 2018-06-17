def partition(arr,left,right):
	p = right
	i = left - 1
	for j in range(left , right):
		if(arr[j] <= arr[p]):
			i += 1
			arr[j], arr[i] = arr[i], arr[j]
	i += 1
	arr[i], arr[p] = arr[p], arr[i]
	return i

def quick(arr,left,right):
	if(left < right):
		pivot = partition(arr, left, right)
		quick(arr, left, pivot - 1)
		quick(arr, pivot + 1, right)
	return arr

arr = [6,6,3,8,7,7]
arr = quick(arr, 0, len(arr)-1)
print(arr)
