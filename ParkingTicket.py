from ParkedCar import ParkedCar
from ParkingMeter import ParkingMeter
from PoliceOfficer import PoliceOfficer
import math

class ParkingTicket():

  def __init__(self, a, b, c, d, e, f, g, h):
    self.__make = a
    self.__model = b
    self.__color = c
    self.__licenseNumber = d
    self.__minutesParked = e
    self.__minutespurchased = f
    self.__minutesover = self.__minutespurchased - self.__minutesParked
    self.__officersName = g
    self.__badgeNumber = h

  def ticket_amount(self):
    self.__fine = 25
    self.__hoursover = math.ceil(self.__minutesover/60)
    self.__fine += self.__hoursover*10
    return self.__fine

  def ticketing_officer(self):
    return self.__officersName, self.__badgeNumber

  def ticketed_car(self):
    return self.__make, self.__model, self.__color, self.__licenseNumber
  
  def __str__(self):
    return ("Your fine is " + str(self.ticket_amount()) + " Your ticketing officer is " + str(self.ticketing_officer()))
