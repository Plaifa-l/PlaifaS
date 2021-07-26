class Student:
	def __init__(self,name):
		self.name = name
		self.exp = 0
		self.lesson = 0
		#Call function
		self.AddEXP(10)
		
	def Hello(self):
		print('สวัสดีจ้าาาา ผมชื่อ{}'.format(self.name))

	def coding(self):
		print('{}: กำลังเขียนโปรแกรม..'.format(self.name))
		self.exp += 5
		self.lesson += 1
	
	def ShowEXP(self):
		print('{} มีประสบการ์ณ {} EXP'.format(self.name,self.exp))
		print('- เรียนไป {} ครั้งแล้ว'.format(self.lesson))
	
	def AddEXP(self,score):
		self.exp += score
		self.lesson += 1


class SpecialScore():

	def __init__(self):
		self.score = 500 


class SpecialStudent(Student):

	def __init__(self,name,father):
		super().__init__(name)
		self.father = father
		mafia = ['Bill Gates','Thomas Edison']
		if father in mafia:
			self.exp += 100

	def AddEXP(self,score):
		self.exp += (score * 3)
		self.lesson += 1

	def AskEXP(self,score=10):
		print('Teacher!! Give me SPECIAL exp, give me {} EXP'.format(score))
		self.AddEXP(score)

print('MAIN: ', __name__)

  
if __name__ == '__main__':
	
	print('=====1 Jan=====')
	student0 = SpecialStudent('Mark Zugkerberg','Bill Gates')
	student0.AskEXP()
	student0.ShowEXP()

	student1 = Student('Albert')
	print(student1.name)
	student1.Hello()

	print('-----------')
	student2 = Student('Steve')
	print(student2.name)
	student2.Hello() 
	print('=====2 Jan=====')
	print('-----Plai: ใครอยากเรียนโคดดิ้ง?-(10 exp)----')
	print('=====3 Jan=====')
	student1.name = 'Albert EinStein'
	print('ตอนนี้ exp ของแต่ละคนได้เท่าไหร่กันแล้ว')
	student1.AddEXP(10)

	print(student1.name, student1.exp)
	print(student2.name, student2.exp)
	print('=====4 Jan=====')


	for i in range(5):
		student2.coding()

	student1.ShowEXP()
	student2.ShowEXP()




