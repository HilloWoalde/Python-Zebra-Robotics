import time
class Vaccine:
    def __init__(self, people=[]):
        self.people = people
    def enqueue(self, person):
        self.people.append(person)
        print(self.people)
    def dequeue(self):
        evt = 24.0
        evp = "Aidan"
        for i in self.people:
            a=i[(list(i)[0])]
            if a[1] < evt:
                evt = a[1]
                evp = list(i)[0]
        for i in self.people:
            if list(i)[0] == evp:
                print("Dequeueing to Vaccinate " + list(i)[0])
                self.people.remove(i)
    def __str__(self):
        for i in self.people:
            print(str(list(i)[0]))
    def __repr__(self):
        for i in self.people:
            print(str(list(i)[0]))
    def print(self):
        print(self.people)
    def reorder(self):
        people = []
        place = 0
        #print(self.people)
        for i in self.people:
            if people == []:
                people.append(i)
            else:
                while True:
                    #people[place][(list(people[place])[0])]
                    #time.sleep(2.5)
                    #print(people)
                    #print(people[place][(list(people[place])[0])][0])
                    #print(str(people[place][(list(people[place])[0])][0]) in str(people))
                    if len(people) > place:
                        #print(i[(list(i)[0])])
                        #print(people[place][(list(people[place])[0])])
                        if i[(list(i)[0])][0] > people[place][(list(people[place])[0])][0]:
                            place += 1
                        else:
                            #print(people)
                            people.insert(place, i)
                            #print(people)
                            place = 0
                            break
                    else:
                        #print(people)
                        people.insert(place, i)
                        #print(people)
                        place = 0
                        break
        self.people = people
#Henry = {"Henry":[14.5,20.5]}
#Henry["Henry"[1]] = Vaccination Time
#Henry["Henry"[0]] = Arrival Time

line = Vaccine()
for i in range(0,int(input("People to enqueue: "))):
    line.enqueue({input("Name: ") : [float(input("Arrival Time: ")), float(input("Vaccination Time: "))]})

while True:
    match input("What would you like to do?\n   1. Enqueue\n   2. Dequeue\n   3. View Queue\n   "):
        case "1":
            line.enqueue({input("Name: ") : [float(input("Arrival Time: ")), float(input("Vaccination Time: "))]})
        case "2":
            line.dequeue()
        case "3":
            line.reorder()
            line.print()
        case _:
            break