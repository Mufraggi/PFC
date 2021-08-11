from gameConfig import GameConfig, GamePlay
import unittest

class TestGameconfig(unittest.TestCase):
    gameConfig = GameConfig()

    def test_init_config(self):
        self.assertEqual(self.gameConfig.type, GamePlay.UNDEFINED)
        self.assertEqual(self.gameConfig.round, 3)
        self.assertEqual(self.gameConfig.choice, '')
        self.assertEqual(len(self.gameConfig.listChoise), 2)

    def test_set_config(self):
        self.gameConfig.setConfig("normal", 'PVIA', 4)
        self.assertEqual(self.gameConfig.round, 4)
        self.assertEqual(self.gameConfig.choice, 'normal')
        self.assertEqual(self.gameConfig.type, GamePlay.PVIA)
    
    
    def test_get_choise(self):
        self.assertEqual(self.gameConfig.getChoices(), ['normal', 'custom'])
    
    def test_test_getPossibility(self):
         self.gameConfig.setConfig("normal", 'PVIA', 4)
         self.assertEqual(self.gameConfig.getPossibility(), {
        "rock": {
            "key":"r",
            "win":["scissors"]

        }, "paper": {
            "key":"p",
            "win":["rock"]

        }, "scissors": {
            "key": "s",
            "win":["paper"]
        }
    },)


if __name__ == '__main__':
    unittest.main()