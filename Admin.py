class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def login(self, password):
        if self.password == password:
            print(f"{self.name} đã đăng nhập thành công.")
            return True
        else:
            print("Sai mật khẩu!")
            return False

    def logout(self):
        print(f"{self.name} đã đăng xuất.")


class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.users = []  # Danh sách người dùng do admin quản lý

    def addUser(self, user):
        self.users.append(user)
        print(f" Admin đã thêm người dùng mới: {user.name}")

    def removeUser(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print(f" Người dùng {user.name} đã bị xóa.")
                return
        print(" Không tìm thấy người dùng cần xóa.")

    def systemReport(self):
        print(" Báo cáo hệ thống:")
        print(f"Tổng số người dùng: {len(self.users)}")
        for u in self.users:
            print(f"- {u.user_id}: {u.name} ({u.email})")

