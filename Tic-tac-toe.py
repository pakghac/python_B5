# Функция вывода игровой таблицы на экран
def print_game_table(matrix):
    for row in matrix:
        print(*row)
    print()

# Функция получения от игрока номера строки/столбца и проверка его корректности
def get_index():
    input_data = ''
    while input_data not in ('1', '2', '3'):
        input_data = input()
    return int(input_data)

# Функция изменения игровой таблицы на основании данных, введенных игроками 
def player_data_input(player, game_table):
    while True:
        print('Введите номер строки от 1 до 3')
        row = get_index()
        print('Введите номер столбца от 1 до 3')
        col = get_index()
        if game_table[row][col] == '-':
            game_table[row][col] = player
            break
        else:
            print('Эта клетка уже заполнена! Введите строку и столбец снова.')

# Функция проверки победителя
def check_winner(gt):
    if gt[1][1] == gt[2][2] and gt[2][2] == gt[3][3] and gt[1][1] != '-':
        return True, gt[1][1]
    
    if gt[1][3] == gt[2][2] and gt[2][2] == gt[3][1] and gt[1][3] != '-':
        return True, gt[1][3]
    
    for m in range(1, 4):
        if gt[m][1] == gt[m][2] and gt[m][2] == gt[m][3] and gt[m][1] != '-':
            return True, gt[m][1]
        
    for n in range(1, 4):
        if gt[1][n] == gt[2][n] and gt[2][n] == gt[3][n] and gt[1][n] != '-':
                return True, gt[1][n]
    return False, None

# Создание игровой таблицы
table = []
for i in range(4):
    table.append([])
    if i == 0:
        table[i].append(' ')
    else:
        table[i].append(i)
    for j in range(1, 4):
        if i == 0:
            table[i].append(j)
        else:
            table[i].append('-')
            
print_game_table(table)

# Ход игры
for k in range(9):
    if k % 2 == 0:
        symbol = 'x'
        print('Ход x')
    else:
        symbol = 'o'
        print('Ход o')
    player_data_input(symbol, table)
    print_game_table(table)
    if k >= 4:
        if check_winner(table)[0]:
            print(f'Победили {check_winner(table)[1]}!')
            break
else:
    print('Ничья!')
        
        
        

