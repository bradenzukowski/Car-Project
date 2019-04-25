from ParkedCar import *
from ParkingMeter import *
from ParkingTiket import *
class PoliceOfficer

  def __init__(self,name,number):
    self.__officersName=name
    self.__badgeNumber=number
  
  def examineCar(self,car,meter):
    if meter.get_minutespurchased()>car.get_minutespurchased()
      ticket=ParkingTiket(car.get_make(),car.get_model(),car.get_color(),car.get_licenseNumber(),car.get_minutespurchased(),meter.get_minutespurchased(),self.__officersName,self.__badgeNumber)
      return(ticket)
      
  
