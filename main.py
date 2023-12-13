from datetime import (datetime, 
                      timedelta)


class FreeWindow:

    def __init__(self, arrs):
        self.arrs = arrs
        self.start = '09:00'
        self.stop = '21:00'
    

    def sort_inquiry(self):
        """Отсортировываем временные ряды - так удобнее работать."""
        for i in range(len(self.arrs)):
            lowest = i
            for j in range(i + 1, len(self.arrs)):
                if self.arrs[j]['start'] < self.arrs[lowest]['start']:
                    lowest = j
            self.arrs[i], self.arrs[lowest] = self.arrs[lowest], self.arrs[i]
        return self.arrs
    

    def find_free_times(self):
        """Метод находит временные интервалы, в которые врач может принимать пациентов."""
        
        # С отсортированным массивом удобнее работать.
        sorted_inquiry = self.sort_inquiry()

        working_times = []


        # Находим первый "рабочий" интервал
        first_working_interval = {}
        first_working_interval['start'] = self.start
        first_working_interval['stop'] = sorted_inquiry[0]['start']
        working_times.append(first_working_interval)

        for i in range(len(sorted_inquiry) - 1):
            working_interval = {}
            start_working_interval = sorted_inquiry[i]['stop']
            stop_working_interval = sorted_inquiry[i + 1]['start']
            working_interval['start'] = start_working_interval
            working_interval['stop'] = stop_working_interval
            working_times.append(working_interval)

        # Находим последний "рабочий" интервал
        last_working_interval = {}
        last_working_interval['start'] = sorted_inquiry[-1]['stop']   
        last_working_interval['stop'] = self.stop 
        working_times.append(last_working_interval)

        return working_times



    def find_free_windows(self):
        """Получаем свободные временные окна."""

        # Для хранения временных интервалов.
        working_windows = []

        working_intervals = self.find_free_times()
        for i in working_intervals:
            start = i['start']
            marker_time = start
            while marker_time < i['stop']:
                result = {}
                start_ = datetime.strptime(marker_time, "%H:%M")
                result['start'] = str(start_)[11:16]
                start_ += timedelta(minutes=30)
                result['stop'] = str(start_)[11:16]
                marker_time = str(start_)[11:16]
                if result['stop'] <= i['stop']:
                    working_windows.append(result)
        print(working_windows)
                

busy = [
    {'start' : '10:30','stop' : '10:50'},
    {'start' : '18:40','stop' : '18:50'},
    {'start' : '14:40','stop' : '15:50'},
    {'start' : '16:40','stop' : '17:20'},
    {'start' : '20:05','stop' : '20:20'},
    ]

window = FreeWindow(busy)
window.find_free_windows()
