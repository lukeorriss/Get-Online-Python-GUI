import unittest 


isPaused = True

sound = False
class testGameFunctions(unittest.TestCase): 

    def test_sound(self):
        if sound == False:
            print("Test Sound: Sound Off.")
            self.assertFalse(sound, False)
        else:
            print("Test Sound: Sound On.")
            self.assertTrue(sound, True)

    def test_game_state(self):
        if isPaused == False:
            print("Game is running.")
            self.assertFalse(isPaused, False)
        else:
            print("Game is paused.")
            self.assertTrue(isPaused, True)

if __name__ == '__main__': 
    unittest.main()