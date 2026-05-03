from participant import Participant


class Captain(Participant):
    __team_name: str

    def __init__(self, name: str, school_class: str, team_name: str):
        super().__init__(name, school_class)
        self.__team_name = team_name

    def add_points(self, points: int):
        if points > 0:
            self._score += points + 2

    def get_role(self):
        return f"Капитан команды {self.__team_name}"

    def __str__(self):
        return f"{self._Participant__name}, {self._Participant__school_class} класс — {self._score} баллов, роль: {self.get_role()}"

    def __repr__(self):
        return f"Captain(name='{self._Participant__name}', school_class='{self._Participant__school_class}', team_name='{self.__team_name}', score={self._score})"