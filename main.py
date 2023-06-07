# Определяем игровое поле
playing_field = [1, 2, 3,
4, 5, 6,
7, 8, 9]
# Определяем выигрышные комбинации
win_combination = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],
[3, 6, 9], [1, 5, 9], [3, 5, 7]]
# Определяем функцию вывода игрового поля
def show_field():
    print(playing_field[1 - 1], end = " ")
    print(playing_field[2 - 1], end = " ")
    print(playing_field[3 - 1])
    print(playing_field[4 - 1], end = " ")
    print(playing_field[5 - 1], end = " ")
    print(playing_field[6 - 1])
    print(playing_field[7 - 1], end = " ")
    print(playing_field[8 - 1], end = " ")
    print(playing_field[9 - 1])
# Определяем функцию проверки выигрыша
def player_win():
    pl_win = None
    for i in win_combination:
        if playing_field[i[0] - 1] == "X" and playing_field[i[1] - 1] == "X" and playing_field[i[2] - 1] == "X":
            pl_win = "X"
            show_field()
            return pl_win
        elif playing_field[i[0] - 1] == "O" and playing_field[i[1] - 1] == "O" and playing_field[i[2] - 1]== "O":
            pl_win = "O"
            show_field()
            return pl_win
        elif playing_field.count("X") == 5:
            pl_win = "Ничья"
            show_field()
            return pl_win
    return False
# Определяем функцию добавления хода
def make_move(symbol, move):
    playing_field[playing_field.index(move)] = symbol
# Тело программы
player = True
winner = False
while winner == False:
    show_field()
    if player == True:
        symbol = "X"
        move = int(input("Игрок 1, сделайте свой ход: "))
        if move not in playing_field:
            print("Вы пытаетесь использовать занятое окно, выберете другое")
            continue
    else:
        symbol = "O"
        move = int(input("Игрок 2, сделайте свой ход: "))
        if move not in playing_field:
            print("Вы пытаетесь использовать занятое окно, выберете другое")
            continue
    make_move(symbol, move)
    win = player_win()
    if win != False:
        print(f"Winner: {win}")
        winner = not winner
    player = not player