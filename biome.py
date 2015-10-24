class Biome():
    #Tile Outputs
    ocean = 'o'
    forest = 'f'
    desert = 'd'
    grassland = 'g'
    mountain = 'm'
    peak = 'p'
    tundra = 't'
    tropical = 'r'
    shore = 's'

    #Height Constants
    ocean_height = 120
    shore_height = 125
    peak_height = 195
    mountain_height = 185

    #Moisture Constarints
    tundra_moisture = 180
    tropical_moisture = 145
    forest_moisture = 130
    grassland_moisture = 100
    desert_moisture = 0

    #Default Colors
    ocean_color = (0,0,255)
    forest_color = (0,92, 9)
    desert_color = (255,229,167)
    grassland_color = (1, 142, 14)
    mountain_color = (95, 95, 95)
    peak_color = (255, 255, 255)
    tundra_color = (204, 242, 255)
    tropical_color = (0, 118, 93)
    shore_color = (255,209,110)

    @staticmethod
    def GenerateBiomeDefs():
        defs = dict()
        defs[Biome.ocean] = Biome.ocean_color
        defs[Biome.forest] = Biome.forest_color
        defs[Biome.desert] = Biome.desert_color
        defs[Biome.grassland] = Biome.grassland_color
        defs[Biome.mountain] = Biome.mountain_color
        defs[Biome.peak] = Biome.peak_color
        defs[Biome.tundra] = Biome.tundra_color
        defs[Biome.tropical] = Biome.tropical_color
        defs[Biome.shore] = Biome.shore_color
        return defs
