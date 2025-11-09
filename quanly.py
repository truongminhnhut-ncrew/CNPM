 LỚP QUẢN LÝ TOÀN HỆ THỐNG
class HotelManagementSystem:
    """Lớp trung tâm quản lý toàn bộ hoạt động của khách sạn."""

    def __init__(self):
        self.room_types: List[RoomType] = []
        self.rooms: List[Room] = []
        self.customers: List[Customer] = []
        self.bookings: List[Booking] = []
        self.payments: List[Payment] = []
        self.invoices: List[Invoice] = []
        self.notifications: List[Notification] = []

    # --- QUẢN LÝ PHÒNG & LOẠI PHÒNG ---
    def add_room_type(self, type_id: int, name: str, price: float, max_guest: int):
        room_type = RoomType(type_id, name, price, max_guest)
        self.room_types.append(room_type)
        print(f"[System] Thêm loại phòng: {name}")
        return room_type

    def add_room(self, room_id: int, room_number: str, room_type: RoomType):
        room = Room(room_id, room_number, room_type)
        self.rooms.append(room)
        print(f"[System] Thêm phòng: {room_number} ({room_type.type_name})")
        return room

    def find_available_rooms(self, room_type_name: str) -> List[Room]:
        """Tìm các phòng trống theo loại."""
        available = [
            r for r in self.rooms 
            if r.is_available() and r.room_type.type_name == room_type_name
        ]
        print(f"[System] Tìm thấy {len(available)} phòng trống loại '{room_type_name}'")
        return available

    # --- QUẢN LÝ KHÁCH HÀNG ---
    def register_customer(self, customer_id: int, name: str, email: str):
        customer = Customer(customer_id, name, email)
        self.customers.append(customer)
        print(f"[System] Đăng ký khách hàng: {name}")
        return customer
