from hashlib import new
from gameConfig import GameConfig, GamePlay
import random

class Score:
    P1 = 0
    P2 = 0
    PIA = 0


class GameEngine:
    moveList = []
    score:Score = Score() 
    def __init__(self, config:GameConfig):
        self.config = config
        self.possibility = self.config.getPossibility()
        self.initMoveList()
    
    def playPvP(self,inputPlayer:str, inputPlayer2:str):
        if  not self.isGoodInput(inputPlayer) or not self.isGoodInput(inputPlayer2):
            return False
        if inputPlayer == inputPlayer2:
            return False
        if self.isIn(inputPlayer2, self.possibility[inputPlayer]['win']):
            self.score.P1 = self.score.P1 + 1 
            return True
        if self.isIn(inputPlayer, self.possibility[inputPlayer2]['win']):
            if self.config.type == GamePlay.PVP:
                self.score.P2 = self.score.P2 + 1
            if self.config.type == GamePlay.PVIA:
                self.score.PIA = self.score.PIA + 1
            return True
        return False

    def isGoodInput(self, input: str):
        return [ele for ele in self.moveList if(ele in input)]

    def isIn(self, input: str, listWin):
         return [ele for ele in listWin if(ele in input)]

    def initMoveList(self):
        for key in self.possibility:
            self.moveList.append(key)

    def getScore(self):
        if self.config.type == GamePlay.PVP:
            return {
                "P1":self.score.P1,
                "P2":self.score.P2
            }
        else:
            return {
                "P1":self.score.P1,
                "PIA":self.score.PIA
            }

    def iaInput(self):
        return self.moveList[random.randint(0,len(self.moveList)-1)]

    def restart(self):
        self.score = Score()