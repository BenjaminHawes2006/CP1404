"""
CP1404 Practical 9
Test taxi class for prac 9 activity
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

my_taxi =  Taxi("prius 1", 100)
my_taxi.drive(40)
print(my_taxi, my_taxi.get_fare())
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi, my_taxi.get_fare())

my_fancy_taxi =  SilverServiceTaxi(3, name="silver service", fuel=100)
my_fancy_taxi.drive(40)
print(my_fancy_taxi, my_fancy_taxi.get_fare())
my_fancy_taxi.start_fare()
my_fancy_taxi.drive(100)
print(my_fancy_taxi, my_fancy_taxi.get_fare())