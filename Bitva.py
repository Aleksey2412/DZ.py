import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} побеждает!")
                break

            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} побеждает!")
                break

    def player_turn(self):
        input("Нажмите Enter, чтобы атаковать: ")
        self.player.attack(self.computer)
        print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")

    def computer_turn(self):
        print("Ход компьютера...")
        self.computer.attack(self.player)
        print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")

if __name__ == "__main__":
    game = Game()
    game.start()
