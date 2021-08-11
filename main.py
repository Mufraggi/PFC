from gameEngine import GameEngine, Score
from gameConfig import GameConfig, GamePlay


def main():
    config = GameConfig()
    listChoise = config.getChoices()
    tmpRule, tmpGamePlay, tmpNbPoint = menu(listChoise)
    config.setConfig(tmpRule, tmpGamePlay, tmpNbPoint)
    gameLoop(config)


def menu(choices):
    choicesString = ''
    for choice in choices:
        choicesString = choicesString + ' '  + choice

    print("Witch type of game you would play? ("+ choicesString + " )")
    gameRule = input("Game type: ")
    res = [ele for ele in choices if(ele in gameRule)]
    if not res:
        menu(choices)
    print("How do you want to play? (PVP or PVIA)")
    gamePlay = input("Game play: ")
    resGamePlay = [ele for ele in ["PVP", "PVIA"] if(ele in gamePlay)]
    if not resGamePlay:
        menu(choices)
    print("How many point to win? (enter a number between 1 and 9)")
    nbPoint = input("Number of point: ")
    if (int(nbPoint) < 1 and int(nbPoint) < 9):
        menu(choices)
    return gameRule, gamePlay, nbPoint


    
def gameLoop(config:GameConfig):
    if config.type == GamePlay.PVP:
        runPvPLoop(config)
    else:
        runPVIALoop(config)

def runPVIALoop(config:GameConfig):
    engine = GameEngine(config)
    p2Input = ''
    while True:
        print(chr(27) + "[2J")
        if p2Input != '':
            print("Input PIA: "+ p2Input)
        print("The score is " +concatScoreString(engine.getScore()))
        p1Input = input("Input P1: ")
        p2Input = engine.iaInput()
        print("Input PIA: "+ p2Input)
        engine.playPvP(p1Input, p2Input)
        potentialWinner = winnerIs(engine.getScore(), config.round)
        if potentialWinner != '':
            endMessage(potentialWinner, config)
            break

def runPvPLoop(config:GameConfig):
    engine = GameEngine(config)
    while True:
        print(chr(27) + "[2J")
        print("The score is " +concatScoreString(engine.getScore()))
        p1Input = input("Input P1: ")
        p2Input = input("Input P2: ")
        engine.playPvP(p1Input, p2Input)
        potentialWinner = winnerIs(engine.getScore(), config.round)
        if potentialWinner != '':
            endMessage(potentialWinner, config)
            break

def winnerIs(score, goal):
    for key in score:
        if int(score[key]) == int(goal):
            return key
    return ''

def endMessage(potentialWinner: str, config:GameConfig):
    print(chr(27) + "[2J")
    print("Nice game the player: " + potentialWinner + ' win')
    print("Do you want replay?")
    resReplay = input("yes, no ?")
    if resReplay == 'yes':
        return replay(config)
    return


def concatScoreString(score):
    strTmp = ''
    for key in score:
        strTmp = strTmp + ' ' + key+': ' + str(score[key])
    return strTmp

def replay(config:GameConfig):
    listChoise = config.getChoices()
    tmpRule, tmpGamePlay, tmpNbPoint = menu(listChoise)
    config.setConfig(tmpRule, tmpGamePlay, tmpNbPoint)
    gameLoop(config)


if __name__ == "__main__":
    # execute only if run as a script
    main()
