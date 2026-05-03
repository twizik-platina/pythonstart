class Participant:
    __name: str
    __school_class: str
    _score: int

    def __init__(self, name: str, school_class: str):
        self.__name = name
        self.__school_class = school_class
        self._score = 0

    @property
    def score(self):
        return self._score

    @property
    def status(self):
        if self._score == 0:
            return "нет баллов"
        elif self._score >= 50:
            return "лидер"
        else:
            return "участник"

    def add_points(self, points: int):
        if points > 0:
            self._score += points

    def remove_points(self, points: int):
        if points > 0:
            if self._score - points < 0:
                self._score = 0
            else:
                self._score -= points

    def get_role(self):
        return "Участник"

    def __str__(self):
        return f"{self.__name}, {self.__school_class} класс — {self._score} баллов, роль: {self.get_role()}"

    def __repr__(self):
        return f"Participant(name='{self.__name}', school_class='{self.__school_class}', score={self._score})"