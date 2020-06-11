import re


BOARD = [y + x for x in "12345678" for y in "abcdefgh"]


def setup():
    squares = [y + x for x in "12345678" for y in "abcdefgh"]
    start = "RNBQKBNR" + "P" * 8 + " " * 32 + "p" * 8 + "rnbqkbnr"
    board_view = dict(zip(squares, start))
    
    piece_view = {_:[] for _ in start}
    for sq in board_view:
        piece = board_view[sq]
        if piece != " ":
            piece_view[piece].append(sq)
            
    return board_view, piece_view

def pgn_to_moves(gamefile: str) -> [str]:
    
    raw_pgn = " ". join([line.strip() for line in open(gamefile)])
    
    comments_marked = raw_pgn.replace("{", "<").replace("}", ">")
    STRC = re.compile("<[^>]*>")
    comments_removed = STRC.sub(" ", comments_marked)
    
    STR_marked = comments_removed.replace("[", "<").replace("]", ">")
    str_removed = STRC.sub(" ", STR_marked)
    
    MOVE_NUM = re.compile("[1-9][0-9]* *\.")
    just_moves = [_.strip() for _ in MOVE_NUM.split(str_removed)]
    
    last_move = just_moves[-1]
    RESULT = re.compile("( *1 *- *0 | *0 *- *1 | *1/2 *- *1/2 *)")
    last_move = RESULT.sub("", last_move)
    moves = just_moves[:-1] + [last_move]
    
    return [_ for _ in moves if len(_) > 0]

def pre_process_a_move(move: str) -> (str, str):
    wmove, bmove = move.split()
    if wmove[0] in "abcdefgh":
        wmove = "P" + wmove
    if bmove[0] in "abcdefgh":
        bmove = "p" + bmove
    else:
        bmove = bmove.lower()
        
    return wmove, bmove

def pre_process_moves(moves: str) -> [(str, str)]:
    return [pre_process_a_move(move) for move in moves[:-1]]

moves = pre_process_moves(pgn_to_moves("./pgn01.txt"))
board_view, piece_view = setup()

WHITE = " w"
BLACK = " b"

all_castling = {"o-o":("e8", "g8", "h8", "f8"), "o-o-o":("e8", "c8", "a8", "d8"), "O-O":("e1", "g1", "h1", "f1"), "O-O-O":("e1", "c1", "a1", "d1")}

files_to_numbers = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

files_to_alpha = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8 : "h"}

def update_whose_move(whose_move: str) -> str:
    if whose_move == WHITE:
        return BLACK
    return WHITE

def can_pawn_move(pawn: str, file1: int, file2: int, rank1: int, rank2: int, board_view: {str: str}, capturing: bool) -> bool:
    
    final_position = files_to_alpha[file2] + str(rank2)
    
    def is_occupied_white_diagonals():
        
        occupied = [" "]
        
        if 1 <= file1 - 1 <=8 and 1 <= rank1 + 1 <=8:
            right_diagonal_square = files_to_alpha[file1 - 1] + str(rank1 + 1)
            if board_view[right_diagonal_square] != " ":
                occupied.append(right_diagonal_square)
            
        if 1 <= file1 + 1 <=8 and 1 <= rank1 + 1 <=8:
            left_diagonal_square = files_to_alpha[file1 + 1] + str(rank1 + 1)
            if board_view[left_diagonal_square] != " ":
                occupied.append(left_diagonal_square)
            
        return occupied
            
    def is_occupied_black_diagonals():
        
        occupied = [" "]
        
        if 1 <= file1 - 1 <=8 and 1 <= rank1 - 1 <=8:
            right_diagonal_square = files_to_alpha[file1 - 1] + str(rank1 - 1)
            if board_view[right_diagonal_square] != " ":
                occupied.append(right_diagonal_square)
            
        if 1 <= file1 + 1 <=8 and 1 <= rank1 - 1 <=8:
            left_diagonal_square = files_to_alpha[file1 + 1] + str(rank1 - 1)
            if board_view[left_diagonal_square] != " ":
                occupied.append(left_diagonal_square)
        
        return occupied
        
    if pawn == "P":
        
        if capturing:
            positions = is_occupied_white_diagonals()
            for each in positions:
                if each == final_position:
                    return True
        if rank1 == 2:
            return file2 == file1 and rank2 - rank1  in [1, 2]
        return file2 == file1 and rank2 - rank1 == 1
    
    if pawn == "p":
        
        if capturing:
            positions = is_occupied_black_diagonals()
            for each in positions:
                if each == final_position:
                    return True
        if rank1 == 7:
            return file2 == file1 and rank1 - rank2 in [1,2]
        return file2 == file1 and rank1 - rank2 == 1
    

        

def check_valid(piece: str, current_position: str, final_position: str, board_view: {str: str}, capturing: bool) -> bool:
    
    file1, rank1 = files_to_numbers[current_position[0]], int(current_position[1])
    file2, rank2 = files_to_numbers[final_position[0]], int(final_position[1])
    
    if piece in "pP":
        return can_pawn_move(piece, file1, file2, rank1, rank2, board_view, capturing)
    
    piece = piece.upper()
                             
    def is_left_diagonal_clear(file1: int, file2: int, rank1: int, rank2: int): 
        limit = abs(file1 - file2) - 2
        if file1 > file2:
            file1 = file2
            rank1 = rank2
        file1 += 1
        rank1 += 1
        for i in range(limit):
            position = files_to_alpha[file1] + str(rank1)
            if board_view[position] != " ":
                return False
            file1 += 1
            rank1 += 1    
        return True
    
    def is_right_diagonal_clear(file1: int, file2: int, rank1: int, rank2: int):
        limit = abs(file1 - file2) - 2
        if file1 > file2:
            file1 = file2
            rank1 = rank2
        file1 += 1
        rank1 -= 1
        for i in range(limit):
            position = files_to_alpha[file1] + str(rank1)
            if board_view[position] != " ":
                return False
            file1 += 1
            rank1 -= 1
        return True 
          
    def is_rank_clear(file1: int, file2: int, rank1: int):
        file1, file2 = min(file1, file2), max(file1, file2)
        for file in range(file1 + 1, file2):
            position = files_to_alpha[file] + str(rank1)
            if board_view[position] != " ":
                return False
        return True
    
    def is_file_clear(file1: int, rank1: int, rank2: int):    
        file = files_to_alpha[file1]
        rank1, rank2 = min(rank1, rank2), max(rank1, rank2)
        for rank in range(rank1 + 1, rank2):
            position = file + str(rank)
            if board_view[position] != " ":
                return False
        return True 
    
    def can_king_move():
        return (abs(file2 - file1), abs(rank2 - rank1)) in [(1, 0), (0, 1), (1, 1)]  
    
    def can_rook_move():    
        if rank1 == rank2:
            return is_rank_clear(file1, file2, rank1)    
        if file1 == file2:
            return is_file_clear(file1, rank1, rank2)    
        return False
    
    def can_bishop_move():    
        if rank1 < rank2 and file1 < file2 or rank1 > rank2 and file1 > file2:
            return is_left_diagonal_clear(file1, file2, rank1, rank2) and abs(file1 - file2) == abs(rank1 - rank2)     
        if rank1 < rank2 and file1 > file2 or rank1 > rank2 and file1 < file2:
            return is_right_diagonal_clear(file1, file2, rank1, rank2) and abs(file1 - file2) == abs(rank1 - rank2)    
        return False
    
    def can_knight_move():
        return (abs(file2 - file1) , abs(rank2 - rank1)) in [(1, 2), (2, 1)] 
    
    def can_queen_move():
        return can_bishop_move() or can_rook_move()
    
    return {"K": can_king_move, "Q": can_queen_move, "B": can_bishop_move,"R": can_rook_move, "N": can_knight_move, }[piece]()
    
def current_pos(piece: str, piece_view: {str: str}, board_view: {str: str}, final_position: str, capturing: bool) -> str:
    
    for current_position in piece_view[piece]:
        if check_valid(piece, current_position, final_position, board_view, capturing):
            return current_position
        
def  current_one_given(piece: str, FileOrRank: str, piece_view: {str: str}, board_view: {str: str}, final_position: str, capturing: bool) -> str:
    
    
    for current_position in piece_view[piece]:
        if FileOrRank in current_position and check_valid(piece, current_position, final_position, board_view, capturing):
            return current_position
        

def remove_captured(final_position: str, board_view: {str: str}, piece_view: {str, str}) -> ({str: str}):
    
    piece = board_view[final_position]
    board_view[final_position] = " "
    piece_view[piece].remove(final_position)
    return board_view, piece_view

def move_piece(piece: str, current_position: str, final_position: str, board_view: {str: str}, piece_view: {str: str}) -> ({str: str}) :
    
    board_view[current_position] = " "
    board_view[final_position] = piece
    piece_view[piece].remove(current_position)
    piece_view[piece].append(final_position)
    return board_view, piece_view
        
    
def seperate_move(move: str, piece_view: {str: str}, board_view: {str, str}) -> [str]:
    
    square = re.compile("[a-h][1-8]")
    capturing = False
    check = False
    positions = square.findall(move)
    piece = move[0]
    move = move[1: ]

    
    if "x" in move:
        capturing = True
        move = move.replace("x", "")
        
    if "+" in move:
        check = True
        move = move.replace("+", "")
        
    if len(positions) == 2:
        initial_position, final_position = positions
        return piece, initial_position, final_position, capturing, check

    final_position = positions[0]
    move = square.sub("", move)
    
    if len(move) != 0:
        return piece, current_one_given(piece, move, piece_view, board_view, final_position, capturing), final_position, capturing, check
      
    return piece, current_pos(piece, piece_view, board_view, final_position, capturing), final_position, capturing, check

def castling(king: str, rook: str, move: str, board_view: {str: str}, piece_view: {str: str}) -> ({str: str}):
    king_initial, king_final, rook_initial, rook_final = all_castling[move]
    board_view, piece_view = move_piece(king, king_initial, king_final, board_view, piece_view)
    board_view, piece_view = move_piece(rook, rook_initial, rook_final, board_view, piece_view)
    return board_view, piece_view
    

def board_view_to_fen(board_view: {str, str}) -> str:
    square_count = 0
    fen = []
    each_line = ""
    seperator = "/"
    space_count = 0
    
    for square in board_view:
        square_count += 1
        if board_view[square] == " ":
            space_count += 1
        else:
            if space_count != 0:
                each_line = each_line + str(space_count)
                space_count = 0
            each_line = each_line + board_view[square]
            
        if square_count == 8:
            if space_count != 0:
                each_line = each_line + str(space_count)
                space_count = 0
            fen.append(each_line)
            square_count = 0
            each_line = ""
    
    return seperator.join(fen[::-1])




def pgn_to_fen(moves: [(str, str)]) -> [str]:
    
    whose_move = WHITE
    board_view, piece_view = setup()
    all_fen = ["rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w"]
    
    
    
    for each in moves:
        for move in each:
            
            if move in all_castling:
                if whose_move == WHITE:
                    board_view, piece_view = castling("K", "R", move, board_view, piece_view)
                    
                else:
                    board_view, piece_view = castling("k", "r", move, board_view, piece_view)
                
                whose_move = update_whose_move(whose_move)
                all_fen.append(board_view_to_fen(board_view) + whose_move)
                
                
            else:
                piece, current_position, final_position, capturing, check = seperate_move(move, piece_view, board_view)
                if capturing:
                    board_view, piece_view = remove_captured(final_position, board_view, piece_view)
                
                board_view, piece_view = move_piece(piece, current_position, final_position, board_view, piece_view)
                
                whose_move = update_whose_move(whose_move)
                all_fen.append(board_view_to_fen(board_view) + whose_move)
                
                
    return all_fen, board_view, piece_view


fen, board_view, piece_view = pgn_to_fen(moves) 
for each in fen :
    print(each)
    
x = 1

for each in board_view:
    print(board_view[each], end = "|")
    if x % 8 == 0:
        print()
        
    x += 1

                 
                
                    
            
    
