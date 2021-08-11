from enum import Enum;
import json
class GamePlay(Enum):
  UNDEFINED = "UNDEFINED"
  PVP = "PVP"
  PVIA = "PVIA" 


class GameConfig:
  type = GamePlay.UNDEFINED
  round = 3
  rule = ""
  choice =""
  listChoise = []
  
  def __init__(self):
    self.rule = self.loadRule()
      

  def loadRule(self):
    with open("./rule.json") as jsonFile:
      tmpRule = json.load(jsonFile)

      for key in tmpRule:
        self.listChoise.append(key)
      jsonFile.close()
    return tmpRule

  def getChoices(self):
    return self.listChoise
  
  def setConfig(self, rule:str, gamePlayType:str,round:int):
    self.choice = rule
    self.type = GamePlay[gamePlayType]
    self.round = round

  def getPossibility(self):
    return self.rule[self.choice]
    
