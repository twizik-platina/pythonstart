from decorators import log_action


class Tournament:
    __participants: list

    def __init__(self):
        self.__participants = []

    def add_participant(self, participant):
        self.__participants.append(participant)

    def show_participants(self):
        if len(self.__participants) == 0:
            print("Участников пока нет")
            return
        
        for i in range(len(self.__participants)):
            print(f"{i+1}. {self.__participants[i]}")

    def find_participant(self, name: str):
        for p in self.__participants:
            if p._Participant__name == name:
                return p
        return None

    @log_action
    def add_points_to_participant(self, name: str, points: int):
        participant = self.find_participant(name)
        if participant is None:
            print(f"Участник {name} не найден")
            return
        participant.add_points(points)
        print(f"Участнику {name} начислено {points} баллов")

    @log_action
    def remove_points_from_participant(self, name: str, points: int):
        participant = self.find_participant(name)
        if participant is None:
            print(f"Участник {name} не найден")
            return
        participant.remove_points(points)
        print(f"У участника {name} снято {points} баллов")

    def show_rating(self):
        if len(self.__participants) == 0:
            print("Участников пока нет")
            return
        
        sorted_participants = sorted(self.__participants, key=lambda p: p.score, reverse=True)
        
        print("=== РЕЙТИНГ УЧАСТНИКОВ ===")
        for i in range(len(sorted_participants)):
            print(f"{i+1}. {sorted_participants[i]._Participant__name} - {sorted_participants[i].score} баллов")

    def get_winner(self):
        if len(self.__participants) == 0:
            print("Участников пока нет")
            return None
        
        winner = self.__participants[0]
        for p in self.__participants:
            if p.score > winner.score:
                winner = p
        
        print(f"\nПОБЕДИТЕЛЬ: {winner._Participant__name} с {winner.score} баллами!")
        return winner

    def show_debug_info(self):
        print("\n=== DEBUG ИНФОРМАЦИЯ ===")
        for p in self.__participants:
            print(p.__dict__)

    def __len__(self):
        return len(self.__participants)