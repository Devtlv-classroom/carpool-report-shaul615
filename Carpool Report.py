cars_available = 100
max_passengers_per_car = 4
days_drivers = 30
days_passengers_waiting = 90
# always be more cars than drivers
if (cars_available < days_drivers):
    cars_available = days_drivers+1
empty_cars_today =   cars_available-(days_passengers_waiting /max_passengers_per_car)



print("The number of cars available on your app:",cars_available)
print("The number of drivers registered on your app:",days_drivers)
print("The number of empty cars today:",int(empty_cars_today))
print("The number of passengers that can be transported today:",cars_available*(max_passengers_per_car+1))
print("The average of passengers to put in each car:",days_passengers_waiting/days_drivers)


