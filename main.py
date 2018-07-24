import keras
import FlapPyBird.flappy as flappy
import os

if __name__ == "__main__":
    # Change work dir for game to work
    os.chdir(os.getcwd() + r"\FlapPyBird")

    # Start game
    flappy.Emulator().runSingleGame(lambda x,y,z: 0, lambda x: 0)
    flappy.Emulator().runSingleGame(lambda x, y, z: 0, lambda x: 0)
