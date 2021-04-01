#recquetball.py

from random import random

def main():
    probA = float(input("Please enter the prob. player A wins a serve: "))
    probB = float(input("Please enter the prob. player B wins a serve: "))
    n = int(input("How many games to simulate: "))
    winA = 0
    winB = 0
    for i in range (n):
        
        scoreA = 0
        scoreB = 0
        serveA = True
        serveB = False
        while scoreA < 15 and scoreB < 15:
            if serveA:
                if random() < probA:
                    scoreA = scoreA + 1
                else:
                    serveA = False
                    serveB = True
            if serveB:
                if random() < probB:
                    scoreB = scoreB + 1
                else:
                    serveB = False
                    serveA = True

        if scoreA == 15:
            winA = winA + 1
        elif scoreB == 15:
            winB = winB + 1

    print("Game simulated:", n)
    print("Win for A: {} ({:.2f}%)".format(winA , winA / n ))
    print("Win for B: {} ({:.2f}%)".format(winB , winB / n ))
    input("")

main()
