class Movie:
    __title: str
    __duration: int
    __age_rating: int

    def __init__(self, title: str, duration: int, age_rating: int) -> None:
        self.__title = title
        self.__duration = duration
        self.__age_rating = age_rating

    def get_info(self) -> str:
        return f"{self.__title} — {self.__duration} мин, {self.__age_rating}+"