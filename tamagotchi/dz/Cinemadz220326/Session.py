from Movie import Movie

class Session:
    __movie: Movie
    __time: str
    __price: int
    __total_seats: int
    __booked_seats: list[int]

    def __init__(self, movie: Movie, time: str, price: int, total_seats: int) -> None:
        self.__movie = movie
        self.__time = time
        self.__price = price
        self.__total_seats = total_seats
        self.__booked_seats = []

    def show_free_seats(self) -> list[int]:
        free_seats = []
        for seat in range(1, self.__total_seats + 1):
            if seat not in self.__booked_seats:
                free_seats.append(seat)
        return free_seats

    def book_seat(self, seat_number: int) -> bool:
        if seat_number < 1 or seat_number > self.__total_seats:
            return False
        if seat_number in self.__booked_seats:
            return False
        self.__booked_seats.append(seat_number)
        return True

    def cancel_booking(self, seat_number: int) -> bool:
        if seat_number < 1 or seat_number > self.__total_seats:
            return False
        if seat_number not in self.__booked_seats:
            return False
        self.__booked_seats.remove(seat_number)
        return True

    def is_seat_free(self, seat_number: int) -> bool:
        if seat_number < 1 or seat_number > self.__total_seats:
            return False
        return seat_number not in self.__booked_seats

    def get_info(self) -> str:
        free_count = len(self.show_free_seats())
        return f"{self.__time} | {self.__movie.get_info()} | {self.__price} руб. | свободно: {free_count}"
    