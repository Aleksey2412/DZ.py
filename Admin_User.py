import random
import tkinter as tk
from tkinter import simpledialog, messagebox

class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    # Getters
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def __repr__(self):
        return f"User(ID={self.__user_id}, Name={self.__name}, AccessLevel={self.__access_level})"


class Admin(User):
    def __init__(self, user_id, name, admin_level):
        super().__init__(user_id, name, access_level='admin')
        self.__admin_level = admin_level

    def add_user(self, user_list, name):
        user_id = random.randint(1000, 9999)
        new_user = User(user_id, name)
        user_list.append(new_user)
        messagebox.showinfo("Успех", f"Пользователь {name} успешно добавлен с ID {user_id}.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                messagebox.showinfo("Успех", f"Пользователь {user.get_name()} успешно удалён.")
                return
        messagebox.showerror("Ошибка", "Пользователь не найден.")

    def show_users(self, user_list):
        user_display = "\n".join(str(user) for user in user_list)
        messagebox.showinfo("Список пользователей", user_display)


def main_menu(current_user, users):
    def admin_menu():
        while True:
            choice = simpledialog.askstring("Меню администратора", "1. Показать пользователей\n2. Добавить пользователя\n3. Удалить пользователя\n4. Выйти")
            if choice == "1":
                current_user.show_users(users)
            elif choice == "2":
                name = simpledialog.askstring("Добавить пользователя", "Введите имя нового пользователя:")
                if name:
                    current_user.add_user(users, name)
            elif choice == "3":
                try:
                    user_id = int(simpledialog.askstring("Удалить пользователя", "Введите ID пользователя для удаления:"))
                    current_user.remove_user(users, user_id)
                except ValueError:
                    messagebox.showerror("Ошибка", "Неверный ID пользователя.")
            elif choice == "4":
                break
            else:
                messagebox.showerror("Ошибка", "Неверный выбор.")

    def user_menu():
        while True:
            choice = simpledialog.askstring("Меню пользователя", "1. Показать пользователей\n2. Выйти")
            if choice == "1":
                user_display = "\n".join(str(user) for user in users)
                messagebox.showinfo("Список пользователей", user_display)
            elif choice == "2":
                break
            else:
                messagebox.showerror("Ошибка", "Неверный выбор.")

    if isinstance(current_user, Admin):
        admin_menu()
    else:
        user_menu()


def main():
    admin = Admin(1234, "Админ", admin_level=1)
    users = [admin]

    while True:
        try:
            root = tk.Tk()
            root.withdraw()  # Hide main window
            user_id = int(simpledialog.askstring("Вход", "Введите ваш ID пользователя:"))
            current_user = next((user for user in users if user.get_user_id() == user_id), None)

            if current_user is None:
                messagebox.showerror("Ошибка", "Неверный ID пользователя.")
                continue

            main_menu(current_user, users)

        except ValueError:
            messagebox.showerror("Ошибка", "Неверный ввод. Пожалуйста, введите числовой ID.")


if __name__ == "__main__":
    main()