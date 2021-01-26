class TimeOffset:
    def __init__(self,hour, minutes, seconds):
        hour = self._hour
        minutes = self._minutes
        seconds = self._seconds

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, hour):
        self._hour = hour

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        self._minutes = minutes

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        self._seconds = seconds

