from .interfaces import SchadleInterface

class SchudleHandler(SchadleInterface):
    def get_all_days(self):
        return ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    
    def get_all_schadle(self):
        days = self.get_all_days()
        return {
            days[0]: {"Maths": 2, "English": 2},
            days[1]: {"Physics": 1, "Biology": 2},
            days[2]: {"History": 1, "Geography": 1},
            days[3]: {"Chemistry": 2, "PE": 1},
            days[4]: {"Computer Science": 2, "Art": 1},
            days[5]: {"Maths": 1, "Music": 1},
            days[6]: {"Day Off": 0}
        }
    
    def calc_all_hours(self):
        schadle = self.get_all_schadle()
        hours = {}
        total_hours = 0
        for day, subjects in schadle.items():
            day_total = sum(subjects.values())
            total_hours += day_total
            hours[day] = day_total
        return {
            "hoursForDays": hours,
            "allHours": total_hours
        }
    
    def clac_longest_day(self):
        longest_day = 0
        hours_of_days = self.calc_all_hours()["hoursForDays"]
        for day, hours in hours_of_days.items():
            if hours > longest_day:
                longest_day = hours
        return longest_day

    def get_schadle_load(self):
        allHours = self.calc_all_hours()["allHours"]
        if allHours < 15:
            key = "low"
        elif allHours > 25:
            key = "hard"
        else:
            key = "medium"  

        scheduleLoadFactory = {
            "low": lambda: print("Розклад дуже легкий"),
            "medium": lambda: print("Розклад урівноважений"),
            "hard":lambda: print("Розклад дуже завантажений"),
        }
        scheduleLoadFactory[key]()