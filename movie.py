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

    def __str__(self):
        print('-'*80)
        print("FILMES CADASTRADOS".center(75))
        print('-'*80)
        print(f'{"Titulo":<3}{"Complexo".center(65)}{"Sala":>5}')
        print('-'*80)
        return f'{self.title}{self.theater.rjust(20," ").ljust(20, " ")}{self.room:>45}'
