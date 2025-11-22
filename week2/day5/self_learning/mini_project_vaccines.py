# ----------------------------
# Human class (no methods)
# ----------------------------
class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type

# ----------------------------
# Queue class
# ----------------------------
class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.priority or person.age > 60:
            # Manual insert at index 0
            new_list = [person]
            for h in self.humans:
                new_list.append(h)
            self.humans = new_list
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        i = 0
        for h in self.humans:
            if h == person:
                return i
            i += 1
        return None

    def swap(self, person1, person2):
        idx1 = self.find_in_queue(person1)
        idx2 = self.find_in_queue(person2)
        if idx1 is None or idx2 is None:
            return None
        self.humans[idx1], self.humans[idx2] = self.humans[idx2], self.humans[idx1]

    def get_next(self):
        if len(self.humans) == 0:
            return None
        first = self.humans[0]
        new_list = []
        for i in range(1, len(self.humans)):
            new_list.append(self.humans[i])
        self.humans = new_list
        return first

    def get_next_blood_type(self, blood_type):
        if len(self.humans) == 0:
            return None
        index = -1
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                index = i
                break
        if index == -1:
            return None
        found = self.humans[index]
        new_list = []
        for i in range(len(self.humans)):
            if i != index:
                new_list.append(self.humans[i])
        self.humans = new_list
        return found

    def sort_by_age(self):
        priority_list = []
        old_list = []
        young_list = []
        for person in self.humans:
            if person.priority:
                priority_list.append(person)
            elif person.age > 60:
                old_list.append(person)
            else:
                young_list.append(person)
        sorted_list = []
        for p in priority_list:
            sorted_list.append(p)
        for p in old_list:
            sorted_list.append(p)
        for p in young_list:
            sorted_list.append(p)
        self.humans = sorted_list

# ----------------------------
# Helper function to display humans
# ----------------------------
def format_human(human):
    return f"{human.name} (Age={human.age}, Priority={human.priority}, Blood={human.blood_type})"

# ----------------------------
# Test code
# ----------------------------

# Create humans
p1 = Human("001", "Alice", 30, False, "A")
p2 = Human("002", "Bob", 75, False, "B")
p3 = Human("003", "Charlie", 40, True, "O")
p4 = Human("004", "Dina", 22, False, "AB")

# Create queue
q = Queue()

# Add humans
q.add_person(p1)
q.add_person(p2)
q.add_person(p3)
q.add_person(p4)

# Display queue after adding
print("Queue after adding:")
print([format_human(h) for h in q.humans])

# Sort queue
q.sort_by_age()
print("\nAfter sorting:")
print([format_human(h) for h in q.humans])

# Get next person
next_person = q.get_next()
if next_person:
    print("\nNext person:", format_human(next_person))
else:
    print("\nNext person: None")

# Get next person by blood type "O"
next_o = q.get_next_blood_type("O")
if next_o:
    print("Next blood type O:", format_human(next_o))
else:
    print("Next blood type O: None")

# Display remaining queue
print("\nQueue now:")
print([format_human(h) for h in q.humans])
