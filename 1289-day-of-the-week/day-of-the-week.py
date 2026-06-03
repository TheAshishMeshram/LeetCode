from datetime import date

class Solution:
    def dayOfTheWeek(self, day, month, year):
        days = [
            "Monday","Tuesday","Wednesday",
            "Thursday","Friday","Saturday","Sunday"
        ]

        return days[date(year, month, day).weekday()]