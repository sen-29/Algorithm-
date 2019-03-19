import csv

class Faculty:
    def __init__(self):
        self.preferences_map = {}
        self.max_lectures = {}
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
    
class Time_table:
    def __init__(self):
        self.time_table_map = {}
    def fill_the_map(self,name,row,column):
        if (row,column) not in self.time_table_map:
            self.time_table_map[(row,column)]=[]
            self.time_table_map[(row,column)].append(name)
        else:
            self.time_table_map[(row,column)].append(name)
        #print(name,row,column)
    def printxyz(self):
        print(self.time_table_map)

class Output:
    def __init__(self):
        self.faculties_name = []
        self.final_time_table = {}
        self.counter = {}
        self.max_lec = {}
        self.blocked_slot = []
        self.faculty_lectures = {}
    def fill_counter(self,name):
        self.counter[name] = 0
    def add_faculty(self,name):
        self.faculties_name.append(name)
        self.faculty_lectures[name] = []
    def make_time_table(self):
        while_count = 0
        for name in self.faculties_name:
            self.max_lec[name] = faculty_map.get_max_lectures(name)
        while 1:
            delete = []
            while_count += 1
            if while_count >= 5:
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
                            for k in range(1,6):
                                if (str(i),str(k)) in self.blocked_slot and (str(i),str(k)) in self.final_time_table:
                                    if self.final_time_table[(str(i),str(k))] == name:
                                        binary = 1
                                        break
                            if binary == 0:
                                if (str(i),str(j)) not in self.blocked_slot:
                                    self.faculty_lectures[name].append((str(i),str(j)))
                                    self.final_time_table[(str(i),str(j))] = name
                                    self.counter[name] += 1
                                    temp = name
                                    self.blocked_slot.append((str(i),str(j)))
                                    print(temp,self.counter[temp],(str(i),str(j)))
                                    for k in range(1,6):
                                        if (str(i),str(k)) not in time_table.time_table_map:
                                            continue
                                        if temp in time_table.time_table_map[(str(i),str(k))]:
                                            time_table.time_table_map[(str(i),str(k))].remove(temp)
                                    delete.append((str(i),str(j)))
                                    break
                            else:
                                break
            cnt = 0
            for name in self.faculties_name:
                if self.max_lec[name] == self.counter[name]:
                    cnt += 1 
                    for arr in time_table.time_table_map:
                        if name in time_table.time_table_map[arr]:
                            time_table.time_table_map[arr].remove(name)        
            if cnt == len(self.faculties_name):
                break
            for arr in time_table.time_table_map:
                if len(time_table.time_table_map[arr]) == 1:
                    if self.counter[time_table.time_table_map[arr][0]] == self.max_lec[time_table.time_table_map[arr][0]]:
                        continue
                    self.faculty_lectures[time_table.time_table_map[arr][0]].append(arr)
                    self.final_time_table[arr] = time_table.time_table_map[arr][0]
                    self.counter[time_table.time_table_map[arr][0]] += 1
                    temp = time_table.time_table_map[arr][0]
                    self.blocked_slot.append(arr)
                    print(temp,self.counter[temp],arr)
                    while_count = 0
                    for i in range(1,6):
                        if (arr[0],str(i)) not in time_table.time_table_map:
                            continue
                        if temp in time_table.time_table_map[(arr[0],str(i))]:
                            time_table.time_table_map[(arr[0],str(i))].remove(temp)
                    delete.append(arr)
                else:
                    flag = 0
                    minimum = 20
                    for prof in time_table.time_table_map[arr]:
                        if self.counter[prof] == self.max_lec[prof]:
                            continue
                        if self.counter[prof] < minimum:
                            minimum = self.counter[prof]
                            flag = 1
                            temp = prof
                        elif self.counter[prof] == minimum:
                            flag = 1
                    if flag == 1:
                        while_count = 0
                        self.faculty_lectures[temp].append(arr)
                        self.final_time_table[arr] = temp
                        self.counter[temp] += 1
                        print(temp,self.counter[temp],arr)
                        for i in range(1,6):
                            if (arr[0],str(i)) not in time_table.time_table_map:
                                continue
                            if temp in time_table.time_table_map[(arr[0],str(i))]:
                                time_table.time_table_map[(arr[0],str(i))].remove(temp)
                        delete.append(arr)
                        self.blocked_slot.append(arr)
            for x in delete:
                if x in time_table.time_table_map:
                    del time_table.time_table_map[x]
    def print_time_table(self):
        for i in range(1,6):
            for j in range(1,6):
                if (str(i),str(j)) in self.final_time_table:
                    print(self.final_time_table[(str(i),str(j))],(str(i),str(j)),end=' ')
                else:
                    print("     ",(str(i),str(j)),"     ", end=' ')
            print("")
        
def get_input():
    print("Give the name of the csv file")
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
                    faculty_map.set_max_lectures(name,max_lec)
                    output.fill_counter(name)
                    output.add_faculty(name)
                else:
                    time_table.fill_the_map(name,column[0],column[2])
                    faculty_map.fill_the_map(name,column[0],column[2])
                c = c+1
                #print(column)

faculty_map = Faculty()
time_table = Time_table()
output = Output()
get_input()
#faculty_map.printxyz()
output.make_time_table()
output.print_time_table()
