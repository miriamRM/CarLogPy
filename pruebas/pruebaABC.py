import abc

class ObjectManager(object):
	"""Class that defines the CRUD of the objects"""
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def create(self, obj):
		pass
	
	@abc.abstractmethod
	def update(self, objId):
		pass
	
	@abc.abstractmethod
	def read(self, objId):
		pass
	
	@abc.abstractmethod
	def delete(self, objId):
		pass

class Car(ObjectManager):

	def __init__(self):
		pass
	
	def create(self):
		pass

	def update(self):
		pass

	def read(self):
		pass

	def delete(self):
		pass

car = Car()
car.create()
