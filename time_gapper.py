import datetime

import matplotlib.pyplot as plt
import matplotlib as mpl


class time_gapper(object):

    def __init__(self,slots= dict(),time_gap = 60,global_values = dict(),verbose = False):
        self.slots = slots
        self.time_gap = time_gap
        self.global_values = global_values
        self.verbose = verbose
    
    def increment_global_value(self,key,value=1):
        if self.verbose and key not in self.global_values.keys():
            print("WARNING: key " + str(key) +" not present in global values dictionary when incrementing value")
        self.global_values[key] += value
    
    def get_global_value(self,key):
        try:
            return self.global_values[key]
        except :
            print ("PROBLEM: key " + str(key) +" not present in global values dictionary when retrieving value")

    def get_timeslot(self,time):
        time_slot = datetime.time(time.hour,time.minute - (time.minute % self.time_gap))
        return time_slot
    
    def timestampToTime(self,timestamp):
        hour, min, sec = timestamp.split(":")
        time = datetime.time(int(hour),int(min),int(sec))
        return time
    
    def timeToLabel(self,timeslot):
        result = timeslot.strftime("%H") + ":" + timeslot.strftime("%M")
        return result

    def add_delay(self,time):
        window = (datetime.datetime.combine(datetime.date(1, 1, 1), time) + datetime.timedelta(minutes=self.time_gap)).time()
        return window

    def add_time_slot(self,slot):
        if slot not in self.slots.keys():
            self.slots[slot] = dict()
        
    def checkIfTimeslotExists(self,slot):
        self.add_time_slot(slot)
    
    def checkTimeFormat(self,timestamp):
        if not isinstance(timestamp,datetime.time):
            return self.timestampToTime(timestamp)
        else:
            return timestamp
    
    def add_value_to_slot(self,time,key,value):
        
        time= self.checkTimeFormat(time)

        timeslot = self.get_timeslot(time)
        label_slot = self.timeToLabel(timeslot)
        self.checkIfTimeslotExists(label_slot)

        self.slots[label_slot][key] = value
    
    def increment_value_in_slot(self,time,key):
       
        time = self.checkTimeFormat(time)

        timeslot = self.get_timeslot(time)
        label_slot = self.timeToLabel(timeslot)

        self.checkIfTimeslotExists(label_slot)

        
        if key in self.slots[label_slot].keys():
            self.slots[label_slot][key] += 1
        else:
            self.slots[label_slot][key] = 1
    
    def access_timeslot_value(self,timeslot,key):
        try:
            return self.slots[timeslot][key]

        except :
            return 0
    
    def plot_singleGraphic(self,key,plt,description=""):
        plt.figure(description)
        X = self.slots.keys()
        Y = []

        for time_slot_iterator in self.slots.keys():
            Y.append(
                self.access_timeslot_value(time_slot_iterator,key)
                )
        plt.scatter(X,Y)
        plt.plot(X,Y)
    
    """def plot(self,keys,description="graphic 1"):
        plt.figure(description)
        mpl.style.use('seaborn')
        X = self.slots.keys()
        Y = []

        for time_slot_iterator in self.slots.keys():
            Y.append(
                self.access_timeslot_value(time_slot_iterator,key)
                )
        plt.scatter(X,Y)
        plt.plot(X,Y)
       
        plt.show()"""

    def plot(self,keys,description="graphic 1"):
           
            mpl.style.use('seaborn')
          
            for key in keys:
                self.plot_singleGraphic(key,plt,key)
            plt.show()




        

