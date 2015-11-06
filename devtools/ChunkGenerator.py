"""
Simple tool to develop sample random chunks.
Currently generates three types of tiles, of random color.
"""

import argparse
from random import Random
parser = argparse.ArgumentParser(description='Chunk generator')
parser.add_argument('-x', type=str, help='Number of chunks to generate in x direction', default = 3)
parser.add_argument('-y', type=str, help='Number of chunks to generate in y direction', default = 3)

def generateChunk(x,y):
    with open( str(x) + "," + str(y) + ".chunk", "w+") as f:
        random = Random()
        f.write("define a as #" +
            str("%X" %random.randint(1048577,16777216)
            + "\n")
        )
        f.write("define b as #" +
            str("%X" %random.randint(1048577,16777216)
            + "\n")
        )
        f.write("define c as #" +
            str("%X" %random.randint(1048577,16777216)
            + "\n")
        )
        for y in range(0,64):
            for x in range(0,64):
                rand = random.randint(1,3)
                if(rand == 1):
                    f.write("a ")
                elif(rand == 2):
                    f.write("b ")
                else:
                    f.write("c ")
            f.write("\n")

for x in range(0, parser.parse_args().x):
    for y in range(0, parser.parse_args().y):
        generateChunk(x,y)
