# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)
import re


def distance(sensor, beacon):
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    return distance


def min_max_points(sensors, beacons):
    x_min = sensors[0][0]
    x_max = sensors[0][0]
    y_min = sensors[0][1]
    y_max = sensors[0][1]
    for sensor, beacon in zip(sensors, beacons):
        x_min = min(x_min, sensor[0], beacon[0])
        x_max = max(x_max, sensor[0], beacon[0])
    return x_min, x_max


def is_this_a_beacon(point, beacons):
    for beacon in beacons:
        if beacon[0] == point[0] and beacon[1] == point[1]:
            return True
    return False


def perimeter(sensor, beacon):
    perimeter = []
    x_sensor = sensor[0]
    y_sensor = sensor[1]
    distance_sensor_beacon = distance(sensor, beacon)
    top_coordinates = (x_sensor, y_sensor - distance_sensor_beacon - 1)
    x_start = top_coordinates[0]
    y_start = top_coordinates[1]
    number_of_steps = abs(y_start - y_sensor)
    perimeter.append((x_start, y_start))
    for _ in range(number_of_steps):
        x_start += 1
        y_start += 1
        perimeter.append((x_start, y_start))

    for _ in range(number_of_steps):
        x_start -= 1
        y_start += 1
        perimeter.append((x_start, y_start))

    for _ in range(number_of_steps):
        x_start -= 1
        y_start -= 1
        perimeter.append((x_start, y_start))

    for _ in range(number_of_steps - 1):
        x_start += 1
        y_start -= 1
        perimeter.append((x_start, y_start))

    return perimeter


def possible_beacon(point, sensors, beacons):
    possible_beacon = True
    for sensor, beacon in zip(sensors, beacons):
        if beacon[0] == point[0] and beacon[1] == point[1]:
            possible_beacon = True
            break

        if distance(sensor, point) <= distance(sensor, beacon):
            possible_beacon = False
            break
    return possible_beacon


def find_range(y, sensors, beacons):
    x_min, x_max = min_max_points(sensors, beacons)

    x = x_max
    while True:
        point = (x, y)
        #  as soon as you have found a True value for an x-coordinate; every x > than that  will also be True
        if possible_beacon(point, sensors, beacons):
            print(f'max found at {point=}')
            range_max = x
            break
        x += 1

    x = x_min
    while True:
        point = (x, y)
        #  as soon as you have found a True value for an x-coordinate; every x < than that  will also be True
        if possible_beacon(point, sensors, beacons):
            print(f'min found at {point=}')
            range_min = x
            break
        x -= 1

    return range_min, range_max


def read_input_file(filename):
    sensor_locations = []
    beacon_locations = []
    with open(filename) as f:
        content = f.read().splitlines()
        for c in content:
            items = [int(a) for a in re.findall("[0-9-]+", c)]
            sensor_location = (items[0], items[1])
            beacon_location = (items[2], items[3])
            sensor_locations.append(sensor_location)
            beacon_locations.append(beacon_location)
    return sensor_locations, beacon_locations


if __name__ == '__main__':
    filename = "input/input15.txt"
    sensors, beacons = read_input_file(filename)

    x_min, x_max = min_max_points(sensors, beacons)
    print(f'{x_min= }, {x_max= }')
    print('x-range: ', x_max - x_min)

    y = 2000000
    # y = 10
    range_min, range_max = find_range(y, sensors, beacons)

    number_impossible_positions = 0
    for y in range(2000000, 2000000):
    # for y in range(10, 11):
        # print(y, end='')
        for x in range(range_min - 25, range_max + 25):
            if x % 10000 == 0:
                pass
                print(x)
            point = (x, y)
            if not possible_beacon(point, sensors, beacons):
                number_impossible_positions += 1
                # print('#', end='')
            else:
                pass
                # print('.', end='')
        print()

    print()
    print(f'partI: {number_impossible_positions= }')

    # for each sensor, loop the outside perimeter (sensor-beacon distance+1)
    # if there is a point on this outside perimenter that is outside the reach of all sensors
    # we have found are distress beacon : - )

    outside_perimeter = []
    for sensor, beacon in zip(sensors, beacons):
        outside_perimeter += perimeter(sensor, beacon)
        print(f'{len(outside_perimeter)= }')

    teller = 0
    for point in outside_perimeter:
        teller += 1
        if teller % 100_000 == 0:
            pass
            # print(teller)
        beacon_found = True
        for sensor, beacon in zip(sensors, beacons):
            if distance(point, sensor) <= distance(sensor, beacon):
                beacon_found = False
                break  # break out of the sensor loop
        if beacon_found:
            if 0 <= point[0] <= 4_000_000 and 0 <= point[1] <= 4_000_000:
                print('we have found it', point)
                break  # break out of the point loop

    distress_frequency = 4_000_000 * point[0] + point[1]
    # beacon_found = False
    # for y in range(0, 4_000_001):
    #     print(f'searching at {y= }')
    #     # print(y, end='')
    #     for x in range(0, 4_000_001):
    #         point = (x, y)
    #         if not possible_beacon(point, sensors, beacons):
    #             number_impossible_positions += 1
    #             # print('#', end='')
    #         else:
    #             if is_this_a_beacon(point, beacons):
    #                 # print('B', end='')
    #                 pass
    #             else:
    #                 # print('.', end='')
    #                 print(f'found distress beacon at: {point= }')
    #                 beacon_found = True
    #                 break
    #     if beacon_found:
    #         break
    #     print()

    print(f'partII: {distress_frequency= } ')
