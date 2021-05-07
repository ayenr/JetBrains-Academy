grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
turn = 1

winner = ''

while True:

    print(f"""---------
| {grid[0][0]} {grid[0][1]} {grid[0][2]} |
| {grid[1][0]} {grid[1][1]} {grid[1][2]} |
| {grid[2][0]} {grid[2][1]} {grid[2][2]} |
---------""")

    game = ''
    for row in grid:
        game += ''.join(row)
    horizontal = [[u for u in game[i: i + 3]] for i in range(0, len(game), 3)]
    vertical = [[game[i] for i in range(0, 7, 3)], [game[i] for i in range(1, 8, 3)], [game[i] for i in range(2, 9, 3)]]
    diagonal = [[game[i] for i in range(0, 9, 4)], [game[i] for i in range(2, 7, 2)]]

    if turn >= 5:
        for row in horizontal:
            if row[0] != ' ' and row[0] == row[1] and row[0] == row[2]:
                winner = row[0]

        for row in vertical:
            if row[0] != ' ' and row[0] == row[1] and row[0] == row[2]:
                winner = row[0]

        for row in diagonal:
            if row[0] != ' ' and row[0] == row[1] and row[0] == row[2]:
                winner = row[0]

        if winner != '':
            print(winner, "wins")
            break

    if turn > 9:
        print('Draw')
        break

    n = [1, 2, 3]

    coord = [int(item) for item in input('Enter the coordinates: ').split() if item.isdigit()]

    if not coord:
        print('You should enter numbers!')
    elif len(coord) != 2:
        print('Please put two digits')
    elif coord[0] not in n or coord[1] not in n:
        print('Coordinates should be from 1 to 3!')
    elif grid[(coord[0] - 1)][(coord[1] - 1)] != ' ':
        print('This cell is occupied! Choose another one!')
    else:
        grid[coord[0] - 1][coord[1] - 1] = 'X' if turn % 2 else 'O'
        turn += 1

