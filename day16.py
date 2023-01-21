# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)
import re


class Valve:
    def __init__(self, ID=None, flowrate=0, open=False, visited=False):
        self.valve_IDs = []
        self.ID = ID
        self.flowrate = flowrate
        self.open = open
        self.valves = []
        self.visited = visited


def read_input_file(filename):
    valve_list = []
    with open(filename) as f:
        content = f.read().splitlines()
        for c in content:
            valve = Valve()
            flow_rate = int(re.findall("[0-9]+", c)[0])
            valves = re.findall("[A-Z]{2}", c)
            valve.flowrate = flow_rate
            valve.ID = valves[0]
            valve.valve_IDs = valves[1:]
            valve_list.append(valve)
    for valve in valve_list:
        for id in valve.valve_IDs:
            for v in valve_list:
                if id == v.ID:
                    valve.valves.append(v)
                    break
    return valve_list


if __name__ == '__main__':
    filename = "input/input16test.txt"
    valve_list = read_input_file(filename)

    time_left = 30  # simulation time left
    simulation_time = 0  # simulation time

    #  TODO below algorithm does not seem to work
    #  in each timestep, find the closed valve with the maximum flowrate reachable from the current valve
    #  if the valve flowrate is higher than the current highest value found, open the valve, otherwise leave closed
    #  update the maximum flowrates list
    #  move to this valve and repeat

    maximum_flowrates_list = {0}
    current_valve = valve_list[0]

    for _ in range(10):
        current_maximum = max(maximum_flowrates_list)
        local_maximum = 0
        for v in current_valve.valves:
            if not v.open:
                maximum_flowrates_list.add(v.flowrate)
                if v.flowrate > local_maximum:
                    local_maximum = v.flowrate
                    valve_with_highest_flowrate = v
        if local_maximum >= current_maximum:
            valve_with_highest_flowrate.open = True
            maximum_flowrates_list.remove(local_maximum)
            next_valve = valve_with_highest_flowrate
        else:
            for v in current_valve.valves:
                if not v.open:
                    next_valve = v
                    break
        print(f'{current_valve.ID= }, {next_valve.ID= }')
        current_valve = next_valve
        print(maximum_flowrates_list)

    print(f'partI: ')
    print(f'partII:  ')
