import csv

# TIME-TABLE FOR B-TECH FIRST YEAR

faculty_lecture_final_map = {}

class Faculty:
    def __init__(self):
        self.preferences_map = {}
        self.max_lectures = {}
        self.faculty_slot_map = {}
    def fill_the_map(self,name,row,column):
        if name not in self.preferences_map:
            self.preferences_map[name]=[]
            self.preferences_map[name].append((row,column))
        else:
            self.preferences_map[name].append((row,column))
        #print(name,row,column)
    def printxyz(self):
        print(self.preferences_map)
    def set_max_lectures(self,name,max_lec):
        self.max_lectures[name] = max_lec
    def get_max_lectures(self,name):
        return self.max_lectures[name]
    def add_faculty_and_slot(self,name,slot):
        self.faculty_slot_map[name] = slot
 
class Time_table:
    def __init__(self):
        self.time_table_map = {}    
        self.faculties_name = []
        self.final_time_table = {}
        self.counter = {}
        self.max_lec = {}
        self.blocked_slot = []
        self.faculty_lectures = {}
        self.batch = ""
    def set_max_lectures(self,name,max_lecs):
        self.max_lec[name] = max_lecs
    def fill_the_map(self,name,row,column):
        if (row,column) not in self.time_table_map:
            self.time_table_map[(row,column)]=[]
            self.time_table_map[(row,column)].append(name)
        else:
            self.time_table_map[(row,column)].append(name)
        #print(name,row,column)
    def fill_counter(self,name):
        self.counter[name] = 0
    def add_faculty(self,name):
        self.faculties_name.append(name)
        self.faculty_lectures[name] = []
    def make_time_table(self):
        while_count = 0
        while 1:
            delete = []
            while_count += 1
            if while_count >= 5:
                while_count = 1
                for name in self.faculties_name:
                    if self.max_lec[name] == self.counter[name]:
                        continue
                    for i in range(1,6):
                        if self.max_lec[name] == self.counter[name]:
                            break
                        for j in range(1,6):
                            if self.max_lec[name] == self.counter[name]:
                                break
                            if (str(i),str(j)) in self.blocked_slot:
                                continue
                            binary = 0
                            for slot_batch in faculty_lecture_final_map[name]:
                                if slot_batch[0]==str(i) and slot_batch[1]==str(j):
                                    binary = 1
                                    break
                            for k in range(1,6):
                                if (str(i),str(k)) in self.blocked_slot and (str(i),str(k)) in self.final_time_table:
                                    if self.final_time_table[(str(i),str(k))] == name:
                                        binary = 1
                                        break
                            if binary == 0:
                                if (str(i),str(j)) not in self.blocked_slot:
                                    self.faculty_lectures[name].append((str(i),str(j)))
                                    self.final_time_table[(str(i),str(j))] = name
                                    if name not in faculty_lecture_final_map:
                                        faculty_lecture_final_map[name] = []
                                        faculty_lecture_final_map[name].append((str(i),str(j),self.batch))
                                    else:
                                        faculty_lecture_final_map[name].append((str(i),str(j),self.batch))
                                    self.counter[name] += 1
                                    temp = name
                                    self.blocked_slot.append((str(i),str(j)))
                                    print(temp,self.counter[temp],(str(i),str(j)))
                                    for k in range(1,6):
                                        if (str(i),str(k)) not in self.time_table_map:
                                            continue
                                        if temp in self.time_table_map[(str(i),str(k))]:
                                            self.time_table_map[(str(i),str(k))].remove(temp)
                                    delete.append((str(i),str(j)))
                                    
            cnt = 0
            for name in self.faculties_name:
                if self.max_lec[name] == self.counter[name]:
                    cnt += 1 
                    for arr in self.time_table_map:
                        if name in self.time_table_map[arr]:
                            self.time_table_map[arr].remove(name)        
            if cnt == len(self.faculties_name):
                break
            for arr in self.time_table_map:
                if len(self.time_table_map[arr]) == 1:
                    if self.counter[self.time_table_map[arr][0]] == self.max_lec[self.time_table_map[arr][0]]:
                        continue
                    binary = 0
                    if self.time_table_map[arr][0] in faculty_lecture_final_map:
                        for slot_batch in faculty_lecture_final_map[self.time_table_map[arr][0]]:
                            if slot_batch[0]==arr[0] and slot_batch[1]==arr[1]:
                                binary = 1
                                break
                        if binary==1:
                            continue
                    self.faculty_lectures[self.time_table_map[arr][0]].append(arr)
                    self.final_time_table[arr] = self.time_table_map[arr][0]
                    self.counter[self.time_table_map[arr][0]] += 1
                    temp = self.time_table_map[arr][0]
                    if temp not in faculty_lecture_final_map:
                        faculty_lecture_final_map[temp] = []
                        faculty_lecture_final_map[temp].append((arr[0],arr[1],self.batch))
                    else:
                        faculty_lecture_final_map[temp].append((arr[0],arr[1],self.batch))
                    self.blocked_slot.append(arr)
                    #print(temp,self.counter[temp],arr)
                    while_count = 0
                    for i in range(1,6):
                        if (arr[0],str(i)) not in self.time_table_map:
                            continue
                        if temp in self.time_table_map[(arr[0],str(i))]:
                            self.time_table_map[(arr[0],str(i))].remove(temp)
                    delete.append(arr)
                else:
                    flag = 0
                    minimum = 20
                    for prof in self.time_table_map[arr]:
                        if self.counter[prof] == self.max_lec[prof]:
                            continue
                        binary = 0
                        if prof in faculty_lecture_final_map:
                            for slot_batch in faculty_lecture_final_map[prof]:
                                if slot_batch[0]==arr[0] and slot_batch[1]==arr[1]:
                                    binary = 1
                                    break
                            if binary==1:
                                continue
                        if self.counter[prof] <= minimum:
                            minimum = self.counter[prof]
                            flag = 1
                            temp = prof
                    if flag == 1:
                        while_count = 0
                        self.faculty_lectures[temp].append(arr)
                        self.final_time_table[arr] = temp
                        self.counter[temp] += 1
                        if temp not in faculty_lecture_final_map:
                            faculty_lecture_final_map[temp] = []
                            faculty_lecture_final_map[temp].append((arr[0],arr[1],self.batch))
                        else:
                            faculty_lecture_final_map[temp].append((arr[0],arr[1],self.batch))      
                        #print(temp,self.counter[temp],arr)
                        for i in range(1,6):
                            if (arr[0],str(i)) not in self.time_table_map:
                                continue
                            if temp in self.time_table_map[(arr[0],str(i))]:
                                self.time_table_map[(arr[0],str(i))].remove(temp)
                        delete.append(arr)
                        self.blocked_slot.append(arr)
            for x in delete:
                if x in self.time_table_map:
                    del self.time_table_map[x]
    def print_time_table(self):
        for i in range(1,6):
            for j in range(1,6):
                if (str(i),str(j)) in self.final_time_table:
                    print(self.final_time_table[(str(i),str(j))],(str(i),str(j)),end=' ')
                else:
                    print("     ",(str(i),str(j)),"     ", end=' ')
                print("")
            print("")
    def printxyz(self):
        print(self.time_table_map)
    def set_batch(self,batch):
        self.batch = batch

def get_input_1():
    print("Give the name of the preferences csv file for B-Tech First Year:")
    file = input()
    with open(file, newline='') as csvfile:
        input_data = csv.reader(csvfile, quotechar='|')
        for row in input_data:
            c = 0
            for column in row:
                if c == 0:
                    name = str(column)
                    print("Maximum lectures of",name,":-")
                    max_lec = int(input())
                    faculty_map_1.set_max_lectures(name,max_lec)
                    time_table_1.set_max_lectures(name,max_lec)
                    time_table_1.fill_counter(name)
                    time_table_1.add_faculty(name)
                    time_table_1.set_batch("btech1")
                else:
                    if len(column) == 3:
                        time_table_1.fill_the_map(name,column[0],column[2])
                        faculty_map_1.fill_the_map(name,column[0],column[2])
                c = c+1
                #print(column)

faculty_map_1 = Faculty()
time_table_1 = Time_table()
get_input_1()
#faculty_map.printxyz()
time_table_1.make_time_table()
print()
print()
print()
time_table_1.print_time_table()



# TIME-TABLE FOR B-TECH SECOND YEAR

def get_input_2():
    print("Give the name of the preferences csv file for B-Tech Second Year:")
    file = input()
    with open(file, newline='') as csvfile:
        input_data = csv.reader(csvfile, quotechar='|')
        for row in input_data:
            c = 0
            for column in row:
                if c == 0:
                    name = str(column)
                    print("Maximum lectures of",name,":-")
                    max_lec = int(input())
                    faculty_map_2.set_max_lectures(name,max_lec)
                    time_table_2.set_max_lectures(name,max_lec)
                    time_table_2.fill_counter(name)
                    time_table_2.add_faculty(name)
                    time_table_2.set_batch("btech2")
                else:
                    if len(column) == 3:
                        time_table_2.fill_the_map(name,column[0],column[2])
                        faculty_map_2.fill_the_map(name,column[0],column[2])
                c = c+1
                #print(column)

faculty_map_2 = Faculty()
time_table_2 = Time_table()
get_input_2()
#faculty_map.printxyz()
time_table_2.make_time_table()
print()
print()
print()
time_table_2.print_time_table()


# TIME-TABLE FOR B-TECH THIRD YEAR


class Time_table_with_slots:
    def __init__(self):
        self.time_table_map = {}    
        self.slot_faculty_map = {}
        self.slots_name = []
        self.final_time_table = {}
        self.counter = {}
        self.max_lec = {}
        self.blocked_slot = []
        self.faculty_lectures = {}
        self.batch = ""
        self.preferences = {}
        self.weighted_preferences = {}
        for i in range(1,6):
            for j in range(1,6):
                self.final_time_table[(str(i),str(j))] = []
    def set_max_lectures(self,name,max_lecs):
        self.max_lec[name] = max_lecs
    def fill_the_map(self):
        for slot in self.weighted_preferences:
            for preference,weight in self.weighted_preferences[slot]:
                if preference not in self.time_table_map:
                    self.time_table_map[preference] = []
                    self.time_table_map[preference].append((slot,weight))
                else:
                    self.time_table_map[preference].append((slot,weight))
    def fill_counter(self,name):
        self.counter[name] = 0
    def add_slots(self,name):
        self.slots_name.append(name)
        if name in self.slot_faculty_map:
            for faculty in self.slot_faculty_map[name]:
                self.faculty_lectures[faculty] = []
    def make_time_table(self):
        while_count = 0
        while 1:
            delete = []
            while_count += 1
            if while_count >= 5:
                while_count = 0
                for slot in self.slots_name:
                    if self.max_lec[slot] == self.counter[slot]:
                        continue
                    for i in range(1,6):
                        if self.max_lec[slot] == self.counter[slot]:
                            break
                        for j in range(1,6):
                            if self.max_lec[slot] == self.counter[slot]:
                                break
                            if (str(i),str(j)) in self.blocked_slot:
                                continue
                            binary = 0
                            for faculty in self.slot_faculty_map[slot]:
                                if faculty in faculty_lecture_final_map:
                                    for slot_batch in faculty_lecture_final_map[faculty]:
                                        if slot_batch[0]==arr[0] and slot_batch[1]==arr[1]:
                                            binary = 1
                                            break
                            for k in range(1,6):
                                if (str(i),str(k)) in self.blocked_slot and (str(i),str(k)) in self.final_time_table:
                                    if self.slot_faculty_map[slot][0] in self.final_time_table[(str(i),str(k))]:
                                        binary = 1
                                        break
                            if binary == 0:
                                if (str(i),str(j)) not in self.blocked_slot:
                                    for faculty in self.slot_faculty_map[slot]:
                                        self.faculty_lectures[faculty].append((str(i),str(j)))
                                        self.final_time_table[(str(i),str(j))].append(faculty)
                                    self.counter[slot] += 1
                                    for faculty in self.slot_faculty_map[slot]:
                                        if faculty not in faculty_lecture_final_map:
                                            faculty_lecture_final_map[faculty] = []
                                        faculty_lecture_final_map[faculty].append((str(i),str(j),self.batch))
                                    for l in range(1,6):
                                        if (str(i),str(l)) not in self.time_table_map:
                                            continue
                                        for slots,weight in self.time_table_map[(str(i),str(l))]:
                                            if slots == slot:
                                                self.time_table_map[(str(i),str(l))].remove((slots,weight))
                                    self.blocked_slot.append((str(i),str(j)))
                                    while_count = 0
                                    delete.append((str(i),str(j)))
            cnt = 0
            for name in self.slots_name:
                if self.max_lec[name] == self.counter[name]:
                    cnt += 1 
                    for arr in self.time_table_map:
                        for slot,weight in self.time_table_map[arr]:
                            if name == slot:
                                self.time_table_map[arr].remove((slot,weight))        
            if cnt == len(self.slots_name):
                break
            for arr in self.time_table_map:
                if len(self.time_table_map[arr]) == 1:
                    if self.counter[self.time_table_map[arr][0][0]] == self.max_lec[self.time_table_map[arr][0][0]]:
                        continue
                    binary = 0
                    for faculty in self.slot_faculty_map[self.time_table_map[arr][0][0]]:
                        if faculty in faculty_lecture_final_map:
                            for slot_batch in faculty_lecture_final_map[faculty]:
                                if slot_batch[0]==arr[0] and slot_batch[1]==arr[1]:
                                    binary = 1
                                    break
                    if binary==1:
                        continue
                    for faculty in self.slot_faculty_map[self.time_table_map[arr][0][0]]:
                        #print(self.faculty_lectures)
                        self.faculty_lectures[faculty].append(arr)
                        self.final_time_table[arr].append(faculty)
                    self.counter[self.time_table_map[arr][0][0]] += 1
                    for faculty in self.slot_faculty_map[self.time_table_map[arr][0][0]]:
                        temp = faculty
                        if temp not in faculty_lecture_final_map:
                            faculty_lecture_final_map[temp] = []
                        faculty_lecture_final_map[temp].append((arr[0],arr[1],self.batch))
                    temp = self.time_table_map[arr][0][0]
                    for i in range(1,6):
                        if (arr[0],str(i)) not in self.time_table_map:
                            continue
                        for slot,weight in self.time_table_map[(arr[0],str(i))]:
                            if temp == slot:
                                self.time_table_map[(arr[0],str(i))].remove((slot,weight))
                    self.blocked_slot.append(arr)
                    while_count = 0
                    delete.append(arr)
                else:
                    flag = 0
                    maximum = 0
                    for slot,weight in self.time_table_map[arr]:
                        if self.counter[slot] == self.max_lec[slot]:
                            continue
                        binary = 0
                        for faculty in self.slot_faculty_map[slot]:
                            if faculty in faculty_lecture_final_map:
                                for slot_batch in faculty_lecture_final_map[faculty]:
                                    if slot_batch[0]==arr[0] and slot_batch[1]==arr[1]:
                                        binary = 1
                                        break
                        if binary==1:
                            continue
                        if weight >= maximum:
                            maximum = weight
                            flag = 1
                            temp = slot
                    if flag == 1:
                        for faculty in self.slot_faculty_map[temp]:
                            self.faculty_lectures[faculty].append(arr)
                            self.final_time_table[arr].append(faculty)
                        self.counter[temp] += 1
                        for faculty in self.slot_faculty_map[temp]:
                            if faculty not in faculty_lecture_final_map:
                                faculty_lecture_final_map[faculty] = []
                            faculty_lecture_final_map[faculty].append((arr[0],arr[1],self.batch))
                        for i in range(1,6):
                            if (arr[0],str(i)) not in self.time_table_map:
                                continue
                            for slot,weight in self.time_table_map[(arr[0],str(i))]:
                                if slot == temp:
                                    self.time_table_map[(arr[0],str(i))].remove((slot,weight))
                        self.blocked_slot.append(arr)
                        while_count = 0
                        delete.append(arr)
            for x in delete:
                if x in self.time_table_map:
                    del self.time_table_map[x]
    def print_time_table(self):
        for i in range(1,6):
            for j in range(1,6):
                if (str(i),str(j)) in self.final_time_table:
                    print(self.final_time_table[(str(i),str(j))],(str(i),str(j)),end=' ')
                else:
                    print("     ",(str(i),str(j)),"     ", end=' ')
                print("")
            print("")
    def printxyz(self):
        print(self.time_table_map)
    def set_batch(self,batch):
        self.batch = batch
    def add_preference(self,slot,row,column):
        if slot not in self.preferences:
            self.preferences[slot] = []
            self.preferences[slot].append((row,column))
        else:
            self.preferences[slot].append((row,column))
    def make_weighted_preferences(self):
        for slot in self.preferences:
            self.weighted_preferences[slot] = []
        for slot in self.preferences:
            weights_of_preferences = {}
            for preference in self.preferences[slot]:
                if preference not in weights_of_preferences:
                    weights_of_preferences[preference] = 1
                else:
                    weights_of_preferences[preference] += 1
            for preference in weights_of_preferences:
                self.weighted_preferences[slot].append((preference,weights_of_preferences[preference]))
    def fill_slot_to_faculty_map(self,slot,faculty):
        if slot not in self.slot_faculty_map:
            self.slot_faculty_map[slot] = []
            self.slot_faculty_map[slot].append(faculty)
        else:
            self.slot_faculty_map[slot].append(faculty)    

def get_input_3():
    print("Give the name of the csv file which contains eight slots and its faculties for B-Tech Third Year:")
    file = input()
    with open(file, newline='') as csvfile:
        input_data = csv.reader(csvfile, quotechar='|')
        for row in input_data:
            c = 0
            for column in row:
                if c == 0:
                    slot = column
                    print("Maximum lectures for",slot,":-")
                    max_lec = int(input())
                    time_table_3.set_max_lectures(slot,max_lec)
                    time_table_3.fill_counter(slot)
                    time_table_3.set_batch("btech3")
                else:
                    time_table_3.fill_slot_to_faculty_map(slot,column)
                    faculty_map_3.add_faculty_and_slot(column,slot)
                c = c+1
                #print(column)
            time_table_3.add_slots(slot)

    print("Give the name of the csv file which conatins preferences for B-Tech Third Year:")
    file = input()
    slot_preferences = {}
    with open(file, newline='') as csvfile:
        input_data = csv.reader(csvfile, quotechar='|')
        for row in input_data:
            c = 0
            for column in row:
                if c == 0:
                    name = str(column)
                    slot = faculty_map_3.faculty_slot_map[name]
                else:
                    if len(column) == 3:
                        time_table_3.add_preference(slot,column[0],column[2])
                c = c+1
    time_table_3.make_weighted_preferences()
    time_table_3.fill_the_map()

faculty_map_3 = Faculty()
time_table_3 = Time_table_with_slots()
get_input_3()
#faculty_map.printxyz()
time_table_3.make_time_table()
time_table_3.print_time_table()


# TIME-TABLE FOR B-TECH FOURTH YEAR


def get_input_4():
    print("Give the name of the csv file which contains eight slots and its faculties for B-Tech Fourth Year:")
    file = input()
    with open(file, newline='') as csvfile:
        input_data = csv.reader(csvfile, quotechar='|')
        for row in input_data:
            c = 0
            for column in row:
                if c == 0:
                    slot = column
                    print("Maximum lectures for",slot,":-")
                    max_lec = int(input())
                    time_table_4.set_max_lectures(slot,max_lec)
                    time_table_4.fill_counter(slot)
                    time_table_4.set_batch("btech3")
                else:
                    time_table_4.fill_slot_to_faculty_map(slot,column)
                    faculty_map_4.add_faculty_and_slot(column,slot)
                c = c+1
                #print(column)
            time_table_4.add_slots(slot)

    print("Give the name of the csv file which conatins preferences for B-Tech Fourth Year:")
    file = input()
    slot_preferences = {}
    with open(file, newline='') as csvfile:
        input_data = csv.reader(csvfile, quotechar='|')
        for row in input_data:
            c = 0
            for column in row:
                if c == 0:
                    name = str(column)
                    slot = faculty_map_4.faculty_slot_map[name]
                else:
                    if len(column) == 3:
                        time_table_4.add_preference(slot,column[0],column[2])
                c = c+1
    time_table_4.make_weighted_preferences()
    time_table_4.fill_the_map()

faculty_map_4 = Faculty()
time_table_4 = Time_table_with_slots()
get_input_4()
#faculty_map.printxyz()
time_table_4.make_time_table()
time_table_4.print_time_table()
