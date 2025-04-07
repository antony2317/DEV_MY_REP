import threading
import time
import random


MAX_BOOKING_THREADS = 3
booking_semaphore = threading.Semaphore(MAX_BOOKING_THREADS)

class Session:
    def __init__(self, film_title, session_id, total_seats):
        self.film_title = film_title
        self.session_id = session_id
        self.total_seats = total_seats
        self.available_seats = set(range(1, total_seats + 1))
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def book_seats(self, seat_list, user_id):
        with self.lock:
            print(f"[User {user_id}] Пытается забронировать места {seat_list} на сеанс '{self.film_title}'")

            if not set(seat_list).issubset(self.available_seats):
                print(f"[User {user_id}]  Некоторые места уже заняты: {seat_list}")
                return False

            for seat in seat_list:
                self.available_seats.remove(seat)

            print(f"[User {user_id}]  Успешно забронировано: {seat_list}")
            self.condition.notify_all()
            return True

    def __str__(self):
        return f"{self.film_title} (Session {self.session_id}): {len(self.available_seats)} мест доступно"

class Cinema:
    def __init__(self):
        self.sessions = {}
        self.lock = threading.Lock()

    def add_session(self, session):
        with self.lock:
            self.sessions[session.session_id] = session

    def get_session(self, session_id):
        with self.lock:
            return self.sessions.get(session_id)

class BookingThread(threading.Thread):
    def __init__(self, cinema, session_id, seat_list, user_id):
        super().__init__()
        self.cinema = cinema
        self.session_id = session_id
        self.seat_list = seat_list
        self.user_id = user_id

    def run(self):
        with booking_semaphore:
            session = self.cinema.get_session(self.session_id)
            if session:
                session.book_seats(self.seat_list, self.user_id)
            else:
                print(f"[User {self.user_id}]  Сеанс {self.session_id} не найден")



cinema = Cinema()
cinema.add_session(Session("Inception", 1, 10))
cinema.add_session(Session("Matrix", 2, 8))


threads = []


for user_id in range(1, 11):
    session_id = random.choice([1, 2])
    seat_count = random.randint(1, 3)
    seat_list = random.sample(range(1, 11), seat_count)
    thread = BookingThread(cinema, session_id, seat_list, user_id)
    threads.append(thread)


for t in threads:
    t.start()


for t in threads:
    t.join()


print("\n=== Финальное состояние сеансов ===")
for session in cinema.sessions.values():
    print(session)
