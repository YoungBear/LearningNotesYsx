# hello_1.py
#!/usr/local/bin/python3

class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
bart.print_score()

class Student(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if  value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value
		
