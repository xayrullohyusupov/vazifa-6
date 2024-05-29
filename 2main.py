class Students:

    objects=[]
    counter=0

    def __init__(self,f_name):
        self.f_name=f_name
        self.objects.append(self)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            object=self.objects[self.counter]
            self.counter+=1
            return object.f_name
        except IndexError:
            self.counter=0
            raise StopIteration

Students('Xayrulloh')
Students('Muhammadmuso')
Students('Abdulaziz')
Students('Yigitali')


for student in Students('Xayrulloh'):
     print(student)