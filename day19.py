# this_is_a_function()
# this_is_a_variable
# ThisClass()
# VARIABLE (constant)

# https://adventofcode.com/2022/day/19
from dataclasses import dataclass
import itertools
from itertools import cycle
import re


@dataclass
class Blueprint:
    ID: int
    ore_robot_costs: tuple  # type 0 tuple (ore, clay, obsidian)
    clay_robot_costs: tuple  # type 1
    obsidian_robot_costs: tuple  # type 2
    geode_robot_costs: tuple  # type 3


def check_build_robot(robot_type, blueprint, resources):
    if robot_type == 0:
        ore_costs = blueprint.ore_robot_costs[0]
        clay_costs = blueprint.ore_robot_costs[1]
        obsedian_costs = blueprint.ore_robot_costs[2]
    if robot_type == 1:
        ore_costs = blueprint.clay_robot_costs[0]
        clay_costs = blueprint.clay_robot_costs[1]
        obsedian_costs = blueprint.clay_robot_costs[2]
    if robot_type == 2:
        ore_costs = blueprint.obsidian_robot_costs[0]
        clay_costs = blueprint.obsidian_robot_costs[1]
        obsedian_costs = blueprint.obsidian_robot_costs[2]
    if robot_type == 3:
        ore_costs = blueprint.geode_robot_costs[0]
        clay_costs = blueprint.geode_robot_costs[1]
        obsedian_costs = blueprint.geode_robot_costs[2]

    new_ore = resources[0] - ore_costs
    new_clay = resources[1] - clay_costs
    new_obsidian = resources[2] - obsedian_costs
    new_geode = resources[3]
    new_resources = [new_ore, new_clay, new_obsidian, new_geode]
    if new_ore >= 0 and new_clay >= 0 and new_obsidian >= 0:
        return True, new_resources
    else:
        return False, resources

    return False, resources


def read_input_file(filename):
    with open(filename) as f:
        content = f.read().splitlines()
        blueprint_list = []
        for c in content:
            digits = re.findall("[0-9]+", c)
            digits = [int(a) for a in digits]
            ID = digits[0]
            ore_costs = (digits[1], 0, 0)
            clay_costs = (digits[2], 0, 0)
            obsedian_costs = (digits[3], digits[4], 0)
            geode_costs = (digits[5], 0, digits[6])
            blueprint = Blueprint(ID, ore_costs, clay_costs, obsedian_costs, geode_costs)
            blueprint_list.append(blueprint)
    return blueprint_list


if __name__ == '__main__':
    filename = "input/input19test.txt"
    blueprint_list = read_input_file(filename)

    for blueprint in blueprint_list:
        # robots1 = [1, 4, 2, 0]
        # resources1 = [2, 9, 6, 0]
        robots1 = [1, 0, 0, 0]
        resources1 = [0, 0, 0, 0]
        status_list = [[robots1, resources1]]
        max_geodes = 0
        for time in range(25):
            print(f'{time= }')
            new_status_list = []
            for status in status_list:
                robots = status[0]
                resources = status[1]
                max_geodes = max(max_geodes, resources[3])
                resource_production = [robots[i] for i in range(4)] # amount of resources the current robots produce
                for robot_type in range(4): # check all robots one-by-one, change resources and add to new-status-list
                    robot_build_possible, new_resources = check_build_robot(robot_type=robot_type, blueprint=blueprint, resources=resources)
                    if robot_build_possible:
                        new_robots = [robots[i] for i in range(4)]
                        new_robots[robot_type] += 1
                        if robots[0] > 1 or robots[1] > 14 or robots[2] > 7:
                            break
                        new_resources = [resource_production[i] + new_resources[i] for i in range(4)]
                        if [new_robots, new_resources] not in new_status_list:
                            new_status_list.append([new_robots, new_resources])
                        # if type == 4:
                        #     break
                resources = [resources[i] + resource_production[i] for i in range(4)]
                new_status_list.append([robots, resources])
            print(f'{len(new_status_list)= }')
            print(f'{max_geodes= }')
            status_list = []
            for s in new_status_list:
                if s[1][3] >= max_geodes:
                    status_list.append(s)
            # status_list = new_status_list.copy()
        break

    print(f'partI: ')
    print(f'partII:')


# TODO Don't build more robots of a given type than could possibly be necessary given the blueprint

# If a geode machine can be built, it must be built
# Prune any branches with fewer geodes at a given time than the best so far