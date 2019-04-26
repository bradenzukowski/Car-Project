from ParkedCar.py import *
from ParkingMeter.py import *
from ParkingTicket.py import *
from PoliceOfficer.py import *
def main():
  car = ParkedCar()
  meter = ParkingMeter()
  officer = PoliceOfficer("Jeff", 002)
  car.set_make("Chevy")
  car.set_model("1969 Corvette Stingray")
  car.set_color("Red")
  car.set_liscenseNumber("YVX-3345")
  car.set_minutesParked(136)
  meter.set_minutespurchased(120)
  ticket = officer.examinecar(car, meter)
  print(ticket)
main()
