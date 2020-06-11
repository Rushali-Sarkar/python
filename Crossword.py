# Black Box = Black = 1
# White Box = White = 0

# Top Down Left Right
# 0    1     0    1
# 1    0     0    1
# 1    0     1    1
# 1    0     0    0
# 0    0     1    0
# 1    1     1    0
# 0    1     1    0



Black = 1 
White = 0

def add_sentinels ( crossword : [int] ) -> [int] :
    rc = len(crossword)
    sentinel = [Black for i in range (rc)]
    crossword = [sentinel] + crossword + [sentinel]
    for i in range (rc+2) :
         crossword[i] = [Black] + crossword[i] + [Black]
    return crossword

def number_positions ( crossword : [int]) -> [int]:
    RowsandColumns = len(crossword)
    crossword = add_sentinels(crossword)
    positions = []
    
    for i in range ( 1 , RowsandColumns+1 ): 
        
        for j in range ( 1 , RowsandColumns+1 ):
            
            if crossword[i][j] == Black:
                continue
            
            
            elif crossword[i-1][j] == Black and crossword[i+1][j] == White and crossword[i][j-1] == Black and  crossword[i][j+1] == White:
                positions.append([i,j])
                    
            elif crossword[i-1][j] == Black and crossword[i+1][j] == White and crossword[i][j-1] == White and crossword[i][j+1] == Black:
                positions.append([i,j])
            
            elif crossword[i-1][j] == Black and crossword[i+1][j] == White and crossword[i][j-1] == Black and crossword[i][j+1] == Black:
                positions.append([i,j])
            
            elif crossword[i-1][j] == Black and crossword[i+1][j] == White and crossword[i][j-1] == White and crossword[i][j+1] == White:
                positions.append([i,j])
            
            elif crossword[i-1][j] == White and crossword[i+1][j] == White and crossword[i][j-1] == Black and crossword[i][j+1] == White:
                positions.append([i,j])
                
            elif crossword[i-1][j] == Black and crossword[i+1][j] == Black and crossword[i][j-1] == Black and crossword[i][j+1] == White:
                positions.append([i,j])
                   
            elif crossword[i-1][j] == White and crossword[i+1][j] == Black and crossword[i][j-1] == Black and crossword[i][j+1] == White:
                positions.append([i,j])                
                    
    
    return positions


crossword1 = [[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[1,1,1,0,1,1,1,0,1,1,1,0,1,1,1],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[1,0,1,0,1,0,1,0,1,0,1,1,1,0,1],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]]
crossword2 = [[0,0,0,0,0,0,1,1,1],[1,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,0],[0,1,0,1,0,1,0,1,0],[0,1,0,0,0,0,0,1,0],[0,1,0,1,0,1,0,1,0],[0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1],[1,1,1,0,0,0,0,0,0]]
crossword3 = [[1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,1,0,1,0,1,0,1,0,1,0,1,1,1,0],[1,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],[0,1,1,1,0,1,0,1,0,1,0,1,0,1,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,1]]
crossword4 = [[1,0,1,0,0,0,1,0,1],[0,0,0,0,1,0,0,0,0],[1,0,1,0,0,0,1,0,1],[0,0,0,0,1,0,0,0,0],[0,1,0,1,1,1,0,1,0],[0,0,0,0,1,0,0,0,0],[1,0,1,0,0,0,1,0,1],[0,0,0,0,1,0,0,0,0],[1,0,1,0,0,0,1,0,1]]

total_positions_one = 29
total_positions_two = 14
total_positions_three = 30
total_positions_four = 21














                    
        
                
