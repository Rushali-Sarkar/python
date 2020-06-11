scores = { 0 : "LOVE" , 1 : 15 , 2 : 30 , 3 : 40 }

def count_scores ( points : str ) -> [ int ] :

    PointsPlayerA = 0
    PointsPlayerB = 0

    index = 0

    for player in points :
        index = index + 1

        if player == 'A':
            PointsPlayerA += 1

        if player == 'B':
            PointsPlayerB += 1

        if PointsPlayerA == 3 and PointsPlayerB == 3:
             return deuce( points [ index : ] )

        if PointsPlayerA == 4 :
            return 1 , 0 , 0 , 0 , points [ index : ]

        if PointsPlayerB == 4:
            return 0 , 1, 0 , 0 , points [ index : ]

    return 0 , 0 , PointsPlayerA , PointsPlayerB , points [ index : ]


def deuce ( points : str ) :

    if len ( points ) >= 2 :

        if points [ 0 : 2 ] == "AA" :
            return 1 , 0 , 0 , 0 , points [ 2 : ]

        if points [ 0 : 2 ] == "BB" :
            return 0 , 1 , 0 , 0 , points [ 2 : ]

        if points [ 0 : 2 ] == "AB" or points [ 0 : 2 ] == "BA" :
            return deuce ( points [ 2 : ] )

    return 0 , 0 , 0 , 0 , points


def leader_board ( points : str ) :

    sets1 , sets2 , games1 , games2 , points1 , points2 , matches1 , matches2 = 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0
    Game1 , Game2 , Set1 , Set2 = 0 , 0 , 0 , 0

    while len ( points ) != 0 :
        player1 , player2 , points1 , points2 , points = count_scores ( points )

        games1 = games1 + player1
        games2 = games2 + player2

        Game1 = Game1 + player1
        Game2 = Game2 + player2

        if games1 >= 6 and games1 - games2 >= 2:
            sets1 += 1
            Set1 += 1
            games1 = 0
            games2 = 0

        if games2 >= 6 and games2 - games1 >= 2:
            sets2 += 1
            Set2 += 1
            games2 = 0
            games1 = 0

        if sets1 >= 2 and sets1 + sets2 == 3:
            matches1 += 1
            sets1 = 0
            sets2 = 0

        if sets2 >= 2 and sets1 + sets2 == 3:
            matches2 += 1
            sets2 = 0
            sets1 = 0

    return [ Game1 , Game2 ] , [ scores [ points1 ] , scores [ points2 ] ] , [ Set1 , Set2 ] , [ matches1 , matches2 ]

print(leader_board("ABABABAAB"))
