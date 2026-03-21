from Session import Session

class Cinema:
    __name: str
    __sessions: list[Session]

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__sessions = []

    def add_session(self, session: Session) -> None:
        self.__sessions.append(session)

    def show_sessions(self) -> list[str]:
        sessions_info = []
        for i, session in enumerate(self.__sessions, 1):
            sessions_info.append(f"{i}. {session.get_info()}")
        return sessions_info

    def find_session_by_number(self, index: int) -> Session | None:
        if index < 1 or index > len(self.__sessions):
            return None
        return self.__sessions[index - 1]

    def book_ticket(self, session_index: int, seat_number: int) -> bool:
        session = self.find_session_by_number(session_index)
        if session is None:
            return False
        return session.book_seat(seat_number)

    def cancel_ticket(self, session_index: int, seat_number: int) -> bool:
        session = self.find_session_by_number(session_index)
        if session is None:
            return False
        return session.cancel_booking(seat_number)