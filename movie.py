class Movie:
    def __init__(self, tittle, theater, room):
        self._tittle = tittle
        self._theater = theater
        self._room = room

    @property
    def tittle(self):
        return self._tittle

    @tittle.setter
    def tittle(self, tittle):
        self._tittle = tittle

    @property
    def theater(self):
        return self._theater

    @theater.setter
    def theater(self, theater):
        self._theater = theater

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        self._room = room
