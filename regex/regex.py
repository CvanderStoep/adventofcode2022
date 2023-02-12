import re

string = "Starting items: -85, 91, 90"
# items = [int(a) for a in re.findall("(\d+)", string)]
items = [int(a) for a in re.findall("[0-9-]+", string)]

print(items)

string = "Operation: new = old + 4"
items = re.findall("(\+|\*)\s(old|\d+)", string)[0]

a, b = items
print(items)

c = '2' + a + '3'
print(f'{c= }')
print(f'{eval(c)= }')

string = "Monkey 2:"
items = re.findall("\d+", string)

print(items)

path = "10R5L5R10L4R5L5"
steps = [int(a) for a in re.findall("[0-9]+", path)]
headings = re.findall("[L,R]", path)
print(steps)
print(headings)
path_list = []
for i in range(min(len(steps), len(headings))):
    path_list.append(steps[i])
    path_list.append(headings[i])
path_list.append(steps[-1])
print(path_list)

