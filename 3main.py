class PersonCollection:
    def __init__(self):
        self.people = []

    def add_person(self, name, age):
        self.people.append({'name': name, 'age': age})

    def __iter__(self):
        return iter(self.people)

    def filter(self, condition):
        return [i for i in self.people if condition(i)]


people = PersonCollection()
people.add_person("Alice", 30)
people.add_person("Bob", 25)
people.add_person("Charlie", 35)

for b in people:
    print(b['name'], b['age'])


print("Age >= 30:")
for person in people.filter(lambda x: x['age'] >= 30):
    print(person['name'], person['age'])

print("Name start 'bo':")
for person in people.filter(lambda y: 'bo' in y['name'].lower()):
    print(person['name'], person['age'])
