import random
import heapq

random_items = [random.randint(-50,100) for c in range(32)]




def bubble_sort(items):
	for i in range(len(items)):
		for j in range(len(items)-1-i):
			if items[j] > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j]
				

				
def insertion_sort(items):
	for i in range(1, len(items)):
		j=i
		while j>0 and items[j] < items [j-1]:
			items[j], items[j-1] = items[j-1], items[j]
			j -= 1
				
def merge_sort(items):

	if len(items) > 1:
	
		mid = len(items)/2
		left = items[0:mid]
		right = items[mid:]
		
		merge_sort(left)
		merge_sort(right)
		
		l, r = 0,0
		
		for i in range(len(items)):
		
			lval = left[l] if l < len(left) else None
			rval = right[r] if r < len(right) else None
			
			if (lval and rval and lval < rval) or rval is None:
				items[i] = lval
				l += 1
			
			elif (lval and rval and lval >= rval) or lval is None:
				items[i] = rval
				r += 1
				
			else:
				raise Exception('Could not merge, sub arrays sizes do not match the main array')

				
				
def quick_sort(items):
	if len(items)>1:
		pivot = len(items)/2
		smaller_items = []
		larger_items = []
		
		for i,val in enumerate(items):
			if i != pivot:
				if val < items[pivot]:
					smaller_items.append(val)
				else:
					larger_items.append(val)
		
		quick_sort(smaller_items)
		quick_sort(larger_items)
		items[:] = smaller_items + [items[pivot]] + larger_items
			
		
def heap_sort(items):
	heapq.heapify(items)
	items[:] = [heapq.heappop(items) for i in range(len(items))]




	
				
print 'Before: ', random_items
heap_sort(random_items)
print 'After: ', random_items
