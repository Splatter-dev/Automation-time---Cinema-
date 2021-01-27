class Hour:
    def __init__(self, hour):
        self._hour = str(hour)

    @property
    def hour(self):
        return self._hour.strip()

    @hour.setter
    def hour(self, hour):
        self._hour = hour

    # def __str__(self):
    #    return f'{self._hour}'


class Minutes:
    def __init__(self, minutes):
        self._minutes = str(minutes)

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        self._minutes = minutes.strip()


class Seconds:
    def __init__(self, seconds):
        self._seconds = str(seconds)

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        self._seconds = seconds.strip()
