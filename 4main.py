class PersonCollection:
    def __init__(self):
        self.people = []

    def add_person(self, name, age):
        person = {'id': id(self), 'name': name, 'age': age}
        self.people.append(person)

    def __iter__(self):
        return iter(person['id'] for person in self.people)

people = PersonCollection()
people.add_person("Alice", 30)
people.add_person("Bob", 25)
people.add_person("Charlie", 35)

print("Object ID:")
for person_id in people:
    print(person_id)
