import random
arr = input("Enter stream of elements separated by spaces - ").split()
k = int(input("Enter value of k - "))
rand_arr = list()

pos = list()
for i in range(0,len(arr)):
	pos.append(i)

random.shuffle(pos)
samples = pos[0:k]   # Random Positions.
samp_dict = dict()	# Dictionary to store frquency of the element.

for i in samples:
	if(arr[i] not in samp_dict.keys()):
		samp_dict[arr[i]] = arr[i::].count(arr[i])		# arr[i::] is the array from ith element to the last element
	else:
		samp_dict[arr[i]] = arr[i::].count(arr[i]) + samp_dict[arr[i]]


print(int(len(arr) / float(len(samp_dict)) * sum((2 * v - 1) for v in samp_dict.values())))



