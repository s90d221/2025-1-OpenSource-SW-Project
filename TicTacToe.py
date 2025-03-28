# 틱택토 게임
# Copyright (C) 2025 Sujin Yoon
# Licensed under the MIT License.
# Contact : sujin@gmail.com

import random

# 3x3 크기의 빈 보드 생성
board = [[' ' for _ in range(3)] for _ in range(3)]

# 보드 출력
def print_board():
    for r in range(3):
        print(f" {board[r][0]} | {board[r][1]} | {board[r][2]} ")
        if r != 2:
            print("-----------")
    print()

# 사용자 입력
def player_move():
    while True:
        try:
            x, y = map(int, input("다음 수의 x y 좌표를 입력하시오: ").split())
            if board[x][y] != ' ':
                print("잘못된 위치입니다. 다시 입력하세요.")
            else:
                return x, y
        except (ValueError, IndexError):
            print("잘못된 입력입니다. 0, 1, 2 범위의 좌표를 입력하세요.")

# 컴퓨터 입력 (랜덤으로 선택)
def computer_move_random():
    # 사용자가 이기기 직전인 자리를 막는 함수
    block_move = find_block_move()
    if block_move:
        return block_move 

    # 랜덤으로 x, y 좌표 선택
    while True:
        x, y = random.randint(0, 2), random.randint(0, 2)
        if board[x][y] == ' ':
            return x, y

# 사용자가 이기기 직전인 자리를 막는 함수
def find_block_move():
    for i in range(3):
        # 가로 검사
        if board[i][0] == board[i][1] == 'X' and board[i][2] == ' ':
            return i, 2
        elif board[i][1] == board[i][2] == 'X' and board[i][0] == ' ':
            return i, 0
        elif board[i][0] == board[i][2] == 'X' and board[i][1] == ' ':
            return i, 1
        
        # 세로 검사
        if board[0][i] == board[1][i] == 'X' and board[2][i] == ' ':
            return 2, i
        elif board[1][i] == board[2][i] == 'X' and board[0][i] == ' ':
            return 0, i
        elif board[0][i] == board[2][i] == 'X' and board[1][i] == ' ':
            return 1, i
    
    # 대각선 검사
    if board[0][0] == board[1][1] == 'X' and board[2][2] == ' ':
        return 2, 2
    elif board[1][1] == board[2][2] == 'X' and board[0][0] == ' ':
        return 0, 0
    elif board[0][0] == board[2][2] == 'X' and board[1][1] == ' ':
        return 1, 1

    if board[0][2] == board[1][1] == 'X' and board[2][0] == ' ':
        return 2, 0
    elif board[1][1] == board[2][0] == 'X' and board[0][2] == ' ':
        return 0, 2
    elif board[0][2] == board[2][0] == 'X' and board[1][1] == ' ':
        return 1, 1

    return None  # 막을 자리가 없으면 None 반환

# 승자 검사
def check_winner():
    for i in range(3):
        # 가로 검사
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        # 세로 검사
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    
    # 대각선 검사
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None  # 승자가 없으면 None 반환

# 게임 루프
def play_game():
    # 초기 보드 설정
    global board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        # 보드 출력
        print_board()

        # 사용자 턴
        x, y = player_move()
        board[x][y] = 'X'

        # 승자 체크
        winner = check_winner()
        if winner:
            print_board()
            print(f"사용자({winner})가 이겼습니다!")
            break
        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print_board()
            print("비겼습니다!")  
            break

        # 컴퓨터 턴
        print("컴퓨터가 수를 두고 있습니다...")
        x, y = computer_move_random()  
        board[x][y] = 'O'

        # 승자 체크
        winner = check_winner()
        if winner:
            print_board()
            print(f"컴퓨터({winner})가 이겼습니다!")  
            break
        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print_board()
            print("비겼습니다!") 
            break

play_game()