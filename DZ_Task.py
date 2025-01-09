class Task:
    def __init__(self, description, due_date, status=False):
        self.description = description
        self.due_date = due_date
        self.status = status

    def set_status(self, new_status):
        """Изменяет статус задачи."""
        self.status = new_status

    def is_completed(self):
        """Проверка, завершена ли задача."""
        return self.status


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Добавление новой задачи."""
        self.tasks.append(task)

    def change_task_status(self, index, new_status):
        """Изменение статуса задачи по индексу."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].set_status(new_status)
            self.print_current_tasks()  # После изменения статуса выводим список текущих задач

    def get_current_tasks(self):
        """Получение списка текущих (не выполненных) задач."""
        current_tasks = [task for task in self.tasks if not task.is_completed()]
        return current_tasks

    def print_current_tasks(self):
        """Вывод списка текущих задач."""
        tasks = self.get_current_tasks()
        if tasks:
            print("\nТекущие задачи:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task.description} (до {task.due_date})")
        else:
            print("\nНет текущих задач.")


if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Изменить статус задачи")
        print("3. Вывести список не выполненных задач")
        print("4. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            desc = input("Описание задачи: ")
            date = input("Срок выполнения (ДД-ММ-ГГГГ): ")
            status = input("Задачу считать выполненной? (да/нет): ").lower().strip() == 'да'

            task = Task(desc, date, status)
            manager.add_task(task)
            print("Задача успешно добавлена!")

        elif choice == '2':
            index = int(input("Укажите номер задачи: "))
            status = input("Установить статус 'Выполнена'? (да/нет): ").lower().strip() == 'da'

            manager.change_task_status(index - 1, status)

        elif choice == '3':
            manager.print_current_tasks()

        elif choice == '4':
            break

        else:
            print("Неверный выбор. Попробуйте снова.")