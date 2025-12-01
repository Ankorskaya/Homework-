import random
class Player:
    def __init__(self, money=1000):
        self.money = money

    def change_money(self, amount):
        self.money += amount
        if self.money < 0:
            self.money = 0

    def is_broke(self):
        return self.money <= 0


def choose(prompt, options):
    while True:
        ans = input(prompt)
        if ans in options:
            return ans
        print("Неверный выбор! Попробуйте снова.")


def club(player):
    print("Я решил, что мы поедем в ночной клуб. Я оделся и вышел из дома.")
    choice = choose("Как мы доберёмся? (машина/такси) ", ["машина", "такси"])

    if choice == "машина":
        print("Сели в машину, запустились и поехали в клуб.")
        print("Доехали до клуба, видим весёлую компанию внутри.")
        action = choose("Что делать? (сидеть у бара/потанцевать/познакомиться) ",
                        ["сидеть у бара", "потанцевать", "познакомиться"])

        if action == "сидеть у бара":
            print("Попробовали все фирменные коктейли. Машину оставили у клуба — домой поехали на такси.")
        elif action == "потанцевать":
            print("Танцуем до закрытия! Уезжаем на машине в утренний туман.")
        else:
            print("Познакомились с интересной компанией и укатили продолжать вечер в приватной обстановке.")
    elif choice == "такси":
        print("Таксист со сломанным навигатором увёз нас не туда. Вечер закончился разочарованием.")


def casino(player):
    print(f"Мы решили поехать в казино. У тебя {player.money} монет для игры!")
    choice = choose("На чём поедем? (машина/такси) ", ["машина", "такси"])

    if choice == "машина":
        print("Доехали до казино, вкусно покушали на фуршете...")
        while not player.is_broke():
            print(f"\nУ тебя {player.money} монет.")
            bet = int(input("Сколько ставим? "))
            if bet > player.money:
                print("Ты не можешь поставить больше, чем у тебя есть!")
                continue

            outcome = random.randint(1, 100)
            if outcome <= 45:
                player.change_money(bet)
                print(f"Фух, повезло! Я выиграл {bet} монет!")
            elif outcome <= 90:
                player.change_money(-bet)
                print(f"Не повезло... Я проиграл {bet} монет.")
            else:
                jackpot = player.money * 2
                player.change_money(jackpot)
                print(f"ДЖЕКПОТ, мы выиграли просто невероятное количество денег, уехали счастливые и богатые домой спать")
                break

            if player.is_broke():
                print("У тебя закончились деньги. Тебя вышибают из казино.")
                break

            cont = choose("Хотите продолжить игру? (да/нет) ", ["да", "нет"])
            if cont == "нет":
                print("Я решил уйти из казино и зафиксировать доход/убыток")
                break

    elif choice == "такси":
        print("Я вбил не тот адрес! Такси увезло в ночной клуб. Вечер испорчен — пришлось идти домой пешком.")


def main():
    player = Player()

    while True:
        print("\nВечер после знойного дня... Мне позвонил друг и позвал развлечься.")
        choice = choose("Куда едем??? (тетка/тайгердекристалл) ",
                        ["тетка", "тайгердекристалл"])

        if choice == "тетка":
            club(player)
        elif choice == "тайгердекристалл":
            casino(player)

        game = choose("Хотите сыграть снова? (да/нет) ", ["да", "нет"])
        if game == "нет":
            print(f"Игра окончена. У тебя осталось {player.money} монет.")
            break


main()
