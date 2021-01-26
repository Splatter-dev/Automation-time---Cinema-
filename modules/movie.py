class Movie:
    def __init__(self, title, theater, room, time_offset):
        self._title = title
        self._theater = theater
        self._room = room
        self._time_offset = time_offset

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
    def title(self, new_title):
        self._title = new_title

    @property
    def theater(self):
        return self._theater.title()

    @theater.setter
    def theater(self, new_theater):
        self._theater = new_theater.title()

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        self._room = room

    @property
    def time_offset(self):
        return str(self._time_offset)

    @time_offset.setter
    def time_offset(self, time_offset):
        self._time_offset = time_offset

    def __str__(self):
        self.layout()

        title_splited = ''
        len_title_rest = 22 - len(self._title)
        title_splited = self.title[:19] + '...' if len(self._title) > 19 else self.title + " " * len_title_rest

        return f'{title_splited}{self.theater:^30}{self.room:>10}{self.time_offset:>18}'

    def layout(self):
        print('-'*85)
        print("FILMES CADASTRADOS".center(75))
        print('-'*85)
        print(f'{"Titulo":<15}{"Complexo":^45}{"Sala"}{"Time offset":>20}')
        print('-'*85)