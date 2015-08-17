#! /usr/bin/env python

import math, os

class game():

  players=0
  totaldice=0

def setup():
  """
  Reads the input for number of players and initializes the world
  """

  while game.players not in range(1,7):
    game.players=int(raw_input("Players? (1-6): "))
  game.totaldice=5*game.players

def checkbet(pal,bet):
  """
  Receives a bet (<number of dice>x<value of dice>) and outputs the chances of it being right.
  It also outputs the best current bet.

  The 'pal' flag indicates if the round is palific or not
  """

  betv=[int(i) for i in bet.split("x")]
  betdices=betv[0]
  betvalue=betv[1]
  chancesingle=0.1666 if pal else 0.3333
  totalprob=0
  # Sum all the probabilities of throwing 1,2,3...n dices of a given value
  for i in range(betdices,game.totaldice+1):
    outcomes=math.factorial(game.totaldice)/(math.factorial(i)*math.factorial(game.totaldice-i))
    prob=outcomes*(chancesingle**i)*((1-chancesingle)**(game.totaldice-i))
    totalprob+=prob
  
  print "Chance of rolling %s is %f"%(bet,totalprob)
  print "\n"


  raw_input("Press enter for next round")

if __name__=="__main__":

  setup()
  print "Game starting"
  while 1:
    os.system('clear')
    print "Game status: %i dice left"%game.totaldice
    print "1.- Remove die"
    print "2.- Check bet"
    print "3.- Check palific bet"
    sel=raw_input("> ")
    if sel=="1": 
      game.totaldice-=1
      if not game.totaldice: 
        raw_input("Done")
        break
    elif sel=="2": checkbet(0,raw_input("DxV> "))
    elif sel=="3": checkbet(1,raw_input("DxV> "))


