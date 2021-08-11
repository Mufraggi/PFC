from gameEngine import GameEngine
from gameConfig import GameConfig, GamePlay
import unittest

class TestGameEngine(unittest.TestCase):
    gameConfig = GameConfig()
    gameConfig.setConfig("normal", 'PVIA', 4)
    gameEngine = GameEngine(gameConfig)

    def test_init_testPvp(self):
        self.assertEqual(self.gameEngine.playPvP('a','per'), False)
        self.assertEqual(self.gameEngine.playPvP('rock','per'), False)
        self.assertEqual(self.gameEngine.playPvP('rock','paper'), True)
        self.assertEqual(self.gameEngine.getScore(), {"P1": 1, "PIA": 2})
        self.assertEqual(self.gameEngine.playPvP('paper','rock'), True)
        self.assertEqual(self.gameEngine.getScore(), {"P1": 2, "PIA": 2})

    def test_get_stats(self):
        self.assertEqual(self.gameEngine.playPvP('rock','paper'), True)
        self.assertEqual(self.gameEngine.playPvP('paper','rock'), True)
        self.assertEqual(self.gameEngine.getScore(), {"P1": 1, "PIA": 1})

if __name__ == '__main__':
    unittest.main()