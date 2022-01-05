import csv
import random

class Astronaut:
    def __init__(self, name, flight_duration, status, *extra):
        self.name = name
        self.flight_duration = flight_duration
        self.status = status
        for item in extra:
            self.item = item

    def __str__(self):
        return f"{self.name}, {self.status}"

    def __gt__(self, other):
        print('%s > %s' % (self, other))
        if self.flight_duration > other.flight_duration:
            return True
        else:
            return False

    def __ge__(self, other):
        print('%s >= %s' % (self, other))
        if self.flight_duration >= other.flight_duration:
            return True
        else:
            return False

    def __eq__(self, other):
        print('%s == %s' % (self, other))
        if self.flight_duration == other.flight_duration:
            return True
        else:
            return False


# Extracts information from csv file as is
astronauts_data = []

with open('astronauts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        astronauts_data.append(row)

# Creates Astronaut objects and adds to iterable list
astronauts = []

for astronaut in astronauts_data:
    # need Name, Space Flight (hr), Status
    astronauts.append(Astronaut(astronaut["Name"], astronaut["Space Flight (hr)"], astronaut["Status"]))

# Gets active astronauts
# for num in range(len(astronauts)):
#     if astronauts[num].status == "Active":
#         print(astronauts[num])

print(vars(astronauts[0]))

r1 = random.choice(astronauts)
r2 = random.choice(astronauts)

print(r1 > r2)
print(r1 >= r2)
print(r1 == r2)

for astronaut in astronauts:
    print(astronaut)
