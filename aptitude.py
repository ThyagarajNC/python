import sys
class Aptitude:
	def __init__(self):
		pass
	
	def find_HCF(self, num1, num2):
		if(num1<1 or num2<1):
			print("invalid")
			return
			
		if num1>num2:
			dividend = num1
			divisor = num2
		else:
			dividend = num2
			divisor = num1
		
		while(dividend%divisor):
			temp = dividend
			dividend = divisor
			divisor = temp%divisor
			
		return divisor
		
	def find_LCM(self, num1, num2):
		if(num1<1 or num2<1):
			print("invalid")
			return
			
		self.hcf = self.find_HCF(num1,num2)
		self.lcm = (num1*num2)/self.hcf
		print("LCM of ",num1,num2,' : ',self.lcm)
		
	def find_average(self, num1, num2):
		self.avg = (num1 + num2) / 2
		print("Average of ", num1, "and", num2, " : ", self.avg)
		
	def find_speed(self, dis, time):
		self.speed = dis/time
		print("Speed : ",self.speed,"kmph")
		
apt_obj = Aptitude()
while(True):
	print("\n----------------------------------\n")
	print("Enter")
	print("1.Find H.C.F of 2 numbers")
	print("2.Find L.C.M of 2 numbers")
	print("3.Find Average of numbers")
	print("4.Find Speed ")
	print("5.exit")
	
	choice = int(input("Enter your Option : "))
	if(choice == 1):
		num1 = int(input("Enter num1 : "))
		num2 = int(input("Enter num2 : "))
		hcf = apt_obj.find_HCF(num1,num2)
		print("HCF of ",num1,num2,":",hcf)
	elif(choice == 2):
		num1 = int(input("Enter num1 : "))
		num2 = int(input("Enter num2 : "))
		apt_obj.find_LCM(num1,num2)
	elif(choice == 3):
		num1 = int(input("Enter num1 : "))
		num2 = int(input("Enter num2 : "))
		apt_obj.find_average(num1,num2)
	elif(choice == 4):
		distance = int(input("Enter Distance in km : "))
		time = int(input("Enter Time in hours : "))
		apt_obj.find_speed(distance,time)
	elif(choice == 5):
		sys.exit(0)
	else:
		print("Enter Correct Option")
	
