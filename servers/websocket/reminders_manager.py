from datetime import datetime, timedelta
from threading import Thread

from api_helper import api_helper


class Reminder:
    def __init__(self, frequency, title, description, date=None, starts=None, expires=None, weekdays=None, doneDuration=None, tellBeforeDuration=None, nextReminding=None):
        self.frequency = frequency
        self.title = title
        self.description = description
        self.date = date
        self.starts = starts
        self.expires = expires
        self.weekdays = weekdays  # Llista amb els horaris dels dies de la setmana o False
        self.doneDuration = doneDuration
        self.tellBeforeDuration = timedelta(seconds=self.time_str_to_seconds(tellBeforeDuration)) if tellBeforeDuration else None
        self.nextReminding = nextReminding

    def time_str_to_seconds(self, time_str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s
    
    def getNextRemindingTime(self):
        if self.nextReminding: 
            return self.nextReminding

        if self.frequency == "once":
            # Calculate nextReminding for reminder
            self.nextReminding = self.date - self.tellBeforeDuration if self.tellBeforeDuration else self.date
        elif self.frequency == "multiple":
            # Busca el proper dia de la setmana amb un horari
            now = datetime.now()
            i= 0
            while True:  # Mirar els propers 7 dies
                day_index = (now.weekday() + i) % 7  # Càlcul del dia de la setmana
                day_schedule = self.weekdays[day_index]
                if day_schedule and day_schedule != False:
                    # Ordenar horaris i buscar la primera hora disponible
                    sorted_times = sorted(day_schedule)
                    for time_str in sorted_times:
                        first_time = datetime.strptime(time_str, "%H:%M:%S").time()
                        reminder_time = now + timedelta(days=i)
                        reminder_date = reminder_time.replace(hour=first_time.hour, minute=first_time.minute, second=first_time.second)
                        if reminder_date > now and ((not self.starts) or (reminder_date > self.starts)):
                            self.nextReminding = reminder_date - self.tellBeforeDuration if self.tellBeforeDuration else reminder_date
                            return self.nextReminding
                
                i += 1
                        
class RemindersManager:
    def __init__(self):
        self.reminders = []

        self._updateReminders()

    def _updateReminders(self):
        reminders = api_helper.reminders_db.get_all_reminders()

        for reminder in reminders:
            frequency = reminder.get('frequency')
            title = reminder.get("title")
            description = reminder.get("description")
            date = reminder.get("date")
            starts = reminder.get("starts")
            expires = reminder.get("expires")
            weekdays = reminder.get("weekdays")
            doneDuration = reminder.get("doneDuration")
            tellBefore = reminder.get("tellBefore")
            nextReminding = reminder.get("nextReminding")

            self.reminders.push(Reminder(frequency=frequency, title=title, description=description, date=date, starts=starts, expires=expires, weekdays=weekdays, doneDuration=doneDuration, tellBefore=tellBefore, nextReminding=nextReminding))

        for reminder in self.reminders:
            reminder.getNextReminding()

    def _run():
        pass

    def run(self):
        thread = Thread(name="RemindersRuntime", target=self._run, daemon=True)
        thread.start()

        return thread