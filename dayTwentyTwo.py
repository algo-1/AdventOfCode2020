from collections import deque 
from copy import deepcopy

q1 = deque()
q2 = deque()

with open("dayTwentyTwoPlayerOne.txt") as file:
    for line in file:
        line = line.rstrip()
        q1.append(int(line))

with open("dayTwentyTwoPlayerTwo.txt") as f:
    for line in f:
        line = line.rstrip()
        q2.append(int(line))
q3 = deepcopy(q1)
q4 = deepcopy(q2)
while q1 and q2:
    
    v1 = q1[0]
    v2 = q2[0]

    if v1 > v2:
        top = q1.popleft()
        bottom = q2.popleft()
        q1.append(top)
        q1.append(bottom)
    
    elif v2 > v1:
        top = q2.popleft()
        bottom = q1.popleft()
        q2.append(top)
        q2.append(bottom)

def calc_score(q):
    n = len(q)
    score = 0
    for elem in q:
        score += elem*n 
        n -= 1
    return score 

if q1:
    score = calc_score(q1)
else:
    score = calc_score(q2)

print(f"score = {score}")

def play_game(q5, q6, seen):
    while q5 and q6:
        save_q5 = deepcopy(q5)
        if str(q5) in seen:
            return "x"
        else:

            new_q5 = deque([q5[i] for i in range(1, len(q5))])
            new_q6 = deque([q6[i] for i in range(1, len(q6))])

            if len(new_q5) >= q5[0] and len(new_q6) >= q6[0]:
                
                new_q5 = deque([q5[i] for i in range(1, q5[0]+1)])
                new_q6 = deque([q6[i] for i in range(1, q6[0]+1)])

                winner = play_game(new_q5, new_q6, set())

                if winner == "q5" or winner == "x":
                    top = q5.popleft()
                    bottom = q6.popleft()
                    q5.append(top)
                    q5.append(bottom)

                elif winner == "q6":
                    top = q6.popleft()
                    bottom = q5.popleft()
                    q6.append(top)
                    q6.append(bottom)
                
            else:
                winner = ""
                v1 = q5[0]
                v2 = q6[0]

                if v1 > v2:
                    top = q5.popleft()
                    bottom = q6.popleft()
                    q5.append(top)
                    q5.append(bottom)
                    winner = "q5"

                elif v2 > v1:
                    top = q6.popleft()
                    bottom = q5.popleft()
                    q6.append(top)
                    q6.append(bottom)
                    winner = "q6"
        seen.add(str(save_q5))
    return winner 

if play_game(q3, q4, set()) == "q5":
    score2 = calc_score(q3)

else:
    score2 = calc_score(q4)

print(f"score for game 2 = {score2}")