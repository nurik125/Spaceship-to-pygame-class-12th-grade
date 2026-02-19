import pygame

class spritesheet:
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as message:
            print ('Unable to load spritesheet image:', filename)
            raise (SystemExit, message)
          
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        '''
        Loads image from x, y, x+offset, y+offset
        
        :param self: Description
        :param rectangle: Description
        :param colorkey: Description
        '''
        
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
      
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        '''
        Loads multiple images, supply a list of coordinates
        
        :param self: Description
        :param rects: Description
        :param colorkey: Description
        '''
        
        return [self.image_at(rect, colorkey) for rect in rects]
      
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None, horizontal=True):
        '''
        Loads a strip of images and returns them as a list
        
        :param self: Description
        :param rect: Description
        :param image_count: Description
        :param colorkey: Description
        '''
        
        #! If spritesheet is horizontal
        if horizontal:
            tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                    for x in range(image_count)]
        else:
            #! If spritesheet is vertical
            tups = [(rect[0], rect[1]+rect[3]*y, rect[2], rect[3])
                            for y in range(image_count)]
        return self.images_at(tups, colorkey)