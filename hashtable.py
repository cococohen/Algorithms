import sys	



class HashTable:
	def __init__(self):
		self.size=11
		self.slots = [None] * self.size
		self.data = [None] * self.size
		
	def test():
		print 'hello'
		
	def put(self,key,data):
		hv = self.hashfunction(key,len(self.slots))
		
		if self.slots[hv] == None:
			self.slots[hv] = key
			self.data[hv] = data
		else:
			if self.slots[hv]==key:
				self.data[hv] = data #replace
			else:
				nextslot = self.rehash(hv,len(self.slots))
				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot,len(self.slots))
					
				if self.slots[nextslot] == None:
					self.slots[nextslot] = key
					self.data[nextslot] = data
				else:
					self.data[nextslot] = data #replace
					
	def hashfunction(self,key,size):
		return key%size
		
	def rehash(self,oldhash,size):
		return (oldhash+1)%size
				
				
				
	def get(self,key):
		startslot = self.hashfunction(key,len(self.slots))
		
		data = None
		stop = False
		found = False
		position = startslot
		
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found=True
				data = self.data[position]
				
			else:
				position = self.rehash(position,len(self.slots))
				if position == startslot:
					stop = True
		return data
		
	
	def delete(self,key):
		startslot = self.hashfunction(key,len(self.slots))
		
		stop = False
		found = False
		position = startslot
		
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				self.data[position] = None
				self.slots[position] = None
			
			else:
				position = self.rehash(position,len(self.slots))
				if position == startslot:
					stop = True
		
	def len(self):
		position = 0
		counter = 0
		
		while position < self.size:
			if self.slots[position] != None:
				counter = counter + 1
			position = position + 1	
		print counter
		
	
	
	def __getitem__(self,key):
		return self.get(key)
		
	def __setitem__(self,key,data):
		self.put(key,data)
		
		
	
