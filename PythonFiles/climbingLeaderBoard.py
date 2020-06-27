#!/usr/bin/python3


def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    index = 0
    rank_list = []
    n = len(scores)
    for score in alice:
        while(index < n and score >= scores[index]):
            index = index + 1

        rank_list.append(n - index + 1)

    return rank_list
        
print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))

