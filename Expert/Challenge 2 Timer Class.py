class Timer:
    def __init__(self):
        self.hour = 12
        self.period = "AM"
        self.minute = 00
    def __str__(self):
        return "It is currently " + str(self.hour) + ":" + str(self.minute) + " " + self.period
    def __round__(self):
        if self.minute == 00:
            return "It is currently " + str(self.hour) + " " + self.period
        elif self.minute < 30:
            return "It is a bit past " + str(self.hour) + " " + self.period
        elif self.minute >= 30:
            return "It is a bit before  " + str(self.hour+1) + " " + self.period
    def __ge__(self, period, hour, minute):
        shour = self.hour
        if self.period == "PM":
            shour += 12
        shour = shour % 24
        if period == "PM":
            hour += 12
        hour = hour % 24
        if shour != hour:
            return(shour < hour)
        return(self.minute <= minute)
    def __le__(self, period, hour, minute):
        shour = self.hour
        if self.period == "PM":
            shour += 12
        shour = shour % 24
        if period == "PM":
            hour += 12
        hour = hour % 24
        if shour != hour:
            return(shour > hour)
        return(self.minute >= minute)
        
    def __add__(self, hour, minute):
        for i in hour:
            self.tickHour()
        for i in minute:
            self.tickMinute()
    def tickHour(self):
        if self.hour == 12:
            self.hour = 1
        elif self.hour == 11:
            self.hour += 1
            if self.period == "AM":
                self.period == "PM"
            else:
                self.period == "AM"
        else:
            self.hour += 1
    def tickMinute(self):
        if self.minute == 59:
            self.tickHour()
            self.minute = 0
        else:
            self.minute += 1