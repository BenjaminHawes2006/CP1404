"""
CP1404 Practical 9
Test unreliable car subclass of car
"""

from prac_09.unreliable_car import UnreliableCar

my_car = UnreliableCar(30, name="Renault", fuel=200)
successful_drives = []

for j in range(0, 21):
    my_car.fuel = 100
    number_successful_drives = 0
    for i in range(0, 101):
        initial_odometer = my_car.odometer
        my_car.drive(2)
        if my_car.odometer > initial_odometer:
            number_successful_drives += 1

    print(f"{j}: Successfully drove {number_successful_drives} times")
    successful_drives.append(number_successful_drives)

average_number_successful_drives = (sum(successful_drives)/len(successful_drives))
print(f"Average: {average_number_successful_drives}")




