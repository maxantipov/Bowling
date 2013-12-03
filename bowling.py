#! /usr/bin/env python

class Score:
    """Score class, stores score and whether or not is has been a strike or a spare"""
    score = None
    spare = False
    strike = False
    
    #strike and spare are false by default
    def __init__(self,score,spare=False,strike=False):
        self.score = score
        if strike: self.strike = True
        if spare: self.spare = True

class Scoreboard:
    """Scoreboard class, stores a list of scores"""
        
    scores = []
    
    def addScore(self,score1,score2,lastRound=False):
        """Add a score to the list and updates all previous scores if applicable"""
        print "Bowled this round: ", score1, score2
        score = score1 + score2
        if score < 10 or lastRound:
            self.scores.append(Score(score))
            num_scores = len(self.scores)
            
            for i in range(num_scores-2,-1,-1):
                prev_score = self.scores[i]
                if prev_score.strike == False and prev_score.spare == False :  break
                if prev_score.spare: 
                    self.scores[i].score += score1
                    self.scores[i].spare = False
                else: 
                    self.scores[i].score += score
                    self.scores[i].strike = False
        
        elif score1 == 10: self.scores.append(Score(10,strike = True))
        else: self.scores.append(Score(10,spare = True))
        
        if lastRound:
            if score1 == 10: 
                bowl(self)
                self.scores[-2].score += self.scores[-1].score
                self.scores = self.scores[:-1]
            elif score == 10:
                self.scores[-1].score += getThrow(10) 
        
    def printScores(self):
        for sc in self.scores:
            print sc.score,
        print ""
            

def getThrow(max_score):
    from random import randint
    return randint(0,max_score)


def bowl(scoreboard,lastRound = False):
    n = getThrow(10)
    if n == 10:
        scoreboard.addScore(n, 0, lastRound)
    elif n < 10: 
        scoreboard.addScore(n, getThrow(10-n), lastRound)
        
        
scoreboard = Scoreboard()
for i in range(10):
    if i == 9: bowl(scoreboard,True)
    else: bowl(scoreboard)
    scoreboard.printScores()        

    
