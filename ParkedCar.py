class ParkedCar():
 def __init__(self):
   self.__make=""
   self.__model=""
   self.__color = ""
   self.licenseNumber= ""
   self.__minutesParked=0
 def set_minutesParked(self,minutesParked):
   self.__minutesParked = minutesParked
 def set_make(self,make):
   self.__make=make
 def set_model(self,model):
   self.__model=model
 def set_color(self,color):
   self.__color=color
 def set_licenseNumber(self,licenseNumber):
   self.licenseNumber=licenseNumber
 def get_make(self):
   return self.__make
 def get_minutesParked(self):
   return self.__minutesParked
 def get_model(self):
   return self.__model
 def get_color(self):
   return self.__color
 def get_licenseNumber(self):
   return self.licenseNumber
