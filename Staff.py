class User:
    def __init__(self, user_id, name, email, password):
        self.userID = user_id
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        return True

    def logout(self):
        return True


class RoomType:
    def __init__(self, type_id, type_name, price, max_guest):
        self.typeID = type_id
        self.typeName = type_name
        self.price = price
        self.maxGuest = max_guest

    def getPrice(self):
        return self.price


class Room:
    def __init__(self, room_id, room_number, room_type, status="available"):
        self.roomID = room_id
        self.roomNumber = room_number
        self.roomType = room_type
        self.status = status  

    def isAvailable(self):
        return self.status == "available"


class Booking:
    def __init__(self, booking_id, room, start_date, end_date, status="pending"):
        self.bookingID = booking_id
        self.room = room
        self.startDate = start_date
        self.endDate = end_date
        self.status = status  

    def confirmBooking(self):
        self.status = "confirmed"
        self.room.status = "booked"

    def cancelBooking(self):
        self.status = "cancelled"
        self.room.status = "available"


class Staff(User):
    def __init__(self, user_id, name, email, password, position):
        super().__init__(user_id, name, email, password)
        self.position = position  # string

    def manageRoom(self, room: Room):
        print(f"[STAFF] {self.name} is managing Room {room.roomNumber}. Current status: {room.status}")

    def approveBooking(self, booking: Booking):
        print(f"[STAFF] {self.name} approving Booking {booking.bookingID}...")
        booking.confirmBooking()
        print(f"[APPROVED] Booking {booking.bookingID} confirmed. Room {booking.room.roomNumber} is now booked.")


 