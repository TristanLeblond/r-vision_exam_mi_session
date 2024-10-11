from abc import ABC, abstractmethod
from typing import List

# 1. SRP : Chaque classe a une responsabilité unique

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

class Member:
    def __init__(self, name: str):
        self.name = name
        self.books_issued: List[Book] = []

# 2. OCP : Système ouvert pour l'extension, fermé pour la modification

class BookRepository:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book_by_title(self, title: str) -> Book:
        return next((book for book in self.books if book.title == title), None)

# 3. LSP : Les classes dérivées doivent être remplaçables par leurs classes de base

class MemberService(ABC):
    @abstractmethod
    def issue_book(self, member: Member, book: Book):
        pass

    @abstractmethod
    def return_book(self, member: Member, book: Book):
        pass

class RegularMemberService(MemberService):
    def issue_book(self, member: Member, book: Book):
        member.books_issued.append(book)
        print(f'{member.name} has issued {book.title}')

    def return_book(self, member: Member, book: Book):
        member.books_issued.remove(book)
        print(f'{member.name} has returned {book.title}')

# 4. ISP : Créer des interfaces spécifiques pour chaque action

class Notifier(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass

class EmailNotifier(Notifier):
    def notify(self, message: str):
        print(f'Sending email: {message}')

# 5. DIP : Dépendre des abstractions, pas des implémentations

class LibrarySystem:
    def __init__(self, book_repo: BookRepository, member_service: MemberService, notifier: Notifier):
        self.book_repo = book_repo
        self.member_service = member_service
        self.notifier = notifier

    def issue_book_to_member(self, member: Member, book_title: str):
        book = self.book_repo.find_book_by_title(book_title)
        if book:
            self.member_service.issue_book(member, book)
            self.notifier.notify(f'Book {book.title} issued to {member.name}')
        else:
            print(f'Book {book_title} not found')

# Exemple d'utilisation

book_repo = BookRepository()
book_repo.add_book(Book("1984", "George Orwell"))

member_service = RegularMemberService()
notifier = EmailNotifier()

library_system = LibrarySystem(book_repo, member_service, notifier)

member = Member("Alice")
library_system.issue_book_to_member(member, "1984")

#---------------------------------- ou ------------------------------------

# 1. SRP : Chaque classe a une responsabilité unique

class Flight:
    def __init__(self, flight_number: str, destination: str):
        self.flight_number = flight_number
        self.destination = destination

class Passenger:
    def __init__(self, name: str):
        self.name = name
        self.flights_booked: List[Flight] = []

# 2. OCP : Système ouvert pour l'extension, fermé pour la modification

class FlightRepository:
    def __init__(self):
        self.flights: List[Flight] = []

    def add_flight(self, flight: Flight):
        self.flights.append(flight)

    def find_flight_by_number(self, flight_number: str) -> Flight:
        return next((flight for flight in self.flights if flight.flight_number == flight_number), None)

# 3. LSP : Les classes dérivées doivent être remplaçables par leurs classes de base

class BookingService(ABC):
    @abstractmethod
    def book_flight(self, passenger: Passenger, flight: Flight):
        pass

    @abstractmethod
    def cancel_flight(self, passenger: Passenger, flight: Flight):
        pass

class StandardBookingService(BookingService):
    def book_flight(self, passenger: Passenger, flight: Flight):
        passenger.flights_booked.append(flight)
        print(f'{passenger.name} has booked flight {flight.flight_number} to {flight.destination}')

    def cancel_flight(self, passenger: Passenger, flight: Flight):
        passenger.flights_booked.remove(flight)
        print(f'{passenger.name} has cancelled flight {flight.flight_number} to {flight.destination}')

# 4. ISP : Créer des interfaces spécifiques pour chaque action

class Notifier(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass

class SMSNotifier(Notifier):
    def notify(self, message: str):
        print(f'Sending SMS: {message}')

# 5. DIP : Dépendre des abstractions, pas des implémentations

class FlightBookingSystem:
    def __init__(self, flight_repo: FlightRepository, booking_service: BookingService, notifier: Notifier):
        self.flight_repo = flight_repo
        self.booking_service = booking_service
        self.notifier = notifier

    def book_flight_for_passenger(self, passenger: Passenger, flight_number: str):
        flight = self.flight_repo.find_flight_by_number(flight_number)
        if flight:
            self.booking_service.book_flight(passenger, flight)
            self.notifier.notify(f'Flight {flight.flight_number} booked for {passenger.name}')
        else:
            print(f'Flight {flight_number} not found')

# Exemple d'utilisation

flight_repo = FlightRepository()
flight_repo.add_flight(Flight("AF123", "Paris"))
flight_repo.add_flight(Flight("DL456", "New York"))

booking_service = StandardBookingService()
notifier = SMSNotifier()

flight_booking_system = FlightBookingSystem(flight_repo, booking_service, notifier)

passenger = Passenger("Bob")
flight_booking_system.book_flight_for_passenger(passenger, "AF123")
