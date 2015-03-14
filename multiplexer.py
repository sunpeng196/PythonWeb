import collections
import random


class Counter(object):
	def __init__(self,*names):
		self.anonymous = not bool(names)
		if self.anonymous:
			self.count=0
		else:
			for name in names:
				if not name.isidentifier():
					raise ValueError("name must be valid identifiers")
				setattr(self,name,0)
	def __call__(self,event):
		if self.anonymous:
			self.count += event.count
		else:
			count=getattr(self,event.name)
			setattr(self,event.name,count + event.count)
			
			
class Event:
	def __init__(self,name,count=1):
		if not name.isidentifier():
			raise ValueError("names must be valid identifiers")
		self.name=name
		self.count=count
		
class Multiplexer:
	
		
		
		
		
		
		
		
		
		
		