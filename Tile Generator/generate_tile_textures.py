import arcade
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
class NoiseUtils:
 def __init__(self, imageSize):
        self.imageSize = imageSize
        self.gradientNumber = 256

        self.grid = [[]]
        self.gradients = []
        self.permutations = []
        self.img = {}

        self.__generateGradientVectors()
        self.__normalizeGradientVectors()
        self.__generatePermutationsTable(

platforms_layer_name = 'Platforms'
moving_platforms_layer_name = 'Moving Platforms'


self.wall_list = arcade.tilemap.process_layer(my_map, platforms_layer_name, TILE_SCALING
moving_platforms_list = arcade.tilemap.process_layer(my_map, moving_platforms_layer_name, TILE_SCALING)
for sprite in moving_platforms_list:
    self.wall_list.append(sprite)

    def __generateGradientVectors(self):
            while True:
                x, y = random.uniform(-1, 1), random.uniform(-1, 1)
                    self.gradients.append([x, y])
                    break
