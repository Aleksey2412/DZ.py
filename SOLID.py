from abc import ABC, abstractmethod
import random


# Шаг 1: Создание абстрактного класса Weapon
class Weapon(ABC):
    """Абстрактный класс для оружия."""

    @abstractmethod
    def attack(self):
        """Абстрактный метод атаки."""
        pass


# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    """Класс Меч."""

    def attack(self):
        """Реализация атаки мечом."""
        damage = random.randint(10, 20)
        print(f"Меч наносит {damage} урона!")
        return damage


class Bow(Weapon):
    """Класс Лук."""

    def attack(self):
        """Реализация атаки из лука."""
        damage = random.randint(5, 15)
        print(f"Лук наносит {damage} урона!")
        return damage


class Molot(Weapon):
    """Класс Молот."""

    def attack(self):
        """Реализация атаки молотом."""
        damage = random.randint(25, 30)
        print(f"Молот наносит {damage} урона!")
        return damage


# Шаг 3: Модификация класса Fighter
class Fighter:
    """Класс бойца."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None  # Поле для хранения оружия

    def change_weapon(self, weapon):
        """Смена оружия бойца."""
        self.weapon = weapon
        print(f"{self.name} сменил оружие на {weapon.__class__.__name__}.")

    def attack(self, target):
        """Атака бойца."""
        if self.weapon:
            damage = self.weapon.attack()
            target.take_damage(damage)
        else:
            print(f"{self.name} не может атаковать, у него нет оружия!")

    def take_damage(self, damage):
        """Получение урона."""
        self.health -= damage
        print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}.")


# Шаг 4: Реализация класса Monster
class Monster:
    """Класс монстра."""

    def __init__(self, name, health=50):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        """Получение урона."""
        self.health -= damage
        print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}.")

    def attack(self, target):
        """Атака монстра."""
        damage = random.randint(5, 10)
        print(f"{self.name} атакует {target.name} и наносит {damage} урона!")
        target.take_damage(damage)


# Шаг 5: Реализация сценария боя
if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Рыцарь")
    monster = Monster("Орк")

    # Создаем оружие
    sword = Sword()
    bow = Bow()
    molot = Molot()

    # Выбор оружия для бойца
    print("Выберите оружие для бойца:")
    print("1. Меч")
    print("2. Лук")
    print("3. Молот")
    choice = input("Введите номер оружия: ")

    if choice == "1":
        fighter.change_weapon(sword)
    elif choice == "2":
        fighter.change_weapon(bow)
    elif choice == "3":
        fighter.change_weapon(molot)
    else:
        print("Неверный выбор! Боец остается без оружия.")

    # Бой
    print("\n--- Бой начался! ---")
    while fighter.health > 0 and monster.health > 0:
        fighter.attack(monster)
        if monster.health > 0:
            monster.attack(fighter)

    # Результат боя
    print("\n--- Результат боя ---")
    if fighter.health > 0:
        print(f"{fighter.name} победил!")
    else:
        print(f"{monster.name} победил!")
