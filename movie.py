class Movie:
    def __init__(self, title, theater, room):
        self._title = title
        self._theater = theater
        self._room = room

    @property
    def title(self):
        title = self.title_name()
        self._title = title
        return self._title

    def title_name(self):
        title = ''
        count = 0
        splitted_title = self._title.split()
        for c in splitted_title:
            for l in c:
                count += 1
            if count > 2:
                c = c.title()
            title += f'{c} '
            count = 0
        self._title = title.strip()
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def theater(self):
        return self._theater.title()

    @theater.setter
    def theater(self, theater):
        self._theater = theater

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        self._room = room
