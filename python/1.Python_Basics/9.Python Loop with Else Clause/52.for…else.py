people = [{'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'Peter', 'age': 30},
        {'name': 'Jenifer', 'age': 28}]

name = 'Maria'

found = False
for person in people:
    if person['name'] == name:
        found = True
        print(person)
        break

if not found:
    print(f'{name} not found!')

for person in people:
    if person['name'] == name:
        found = True
        print(person)
        break
else:
    print("没找到")
