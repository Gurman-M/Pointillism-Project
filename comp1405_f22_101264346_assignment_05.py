import sys, pygame, random

# stores the image from command line into a window
src_img = pygame.image.load(sys.argv[1])

# gets width and height of source image
(w, h) = src_img.get_size()

# creates window with image scaled 5 times its size
win_sfc = pygame.display.set_mode((w*5, h*5))

for y in range(h):
    for x in range(w):
        
        # gets the r, g, b values at a specific pixel in original image
        (r, g, b, _) = src_img.get_at((x, y))
        
        # temporary counter variables
        j = 0
        k = 0
        l = 0
        
        # randomizes the order of colours painted so that the last colour doesn't dominate window bceause it was painted last
        # loop will not break until all colours are painted and will not repaint colours by accident
        while (j != (r // 5) and k != (g // 5) and l != (b // 5)):
        
            # stores a temporary counter that will determine which colour will be drawn
            temp = random.randint(0, 3)
            
            # draws red if temp == 0
            if (j <= (r // 5) and temp == 0):
                for i in range ((r // 5)):
                    pygame.draw.rect(win_sfc, (255, 0, 0), (random.randint(x*5, (x+1)*5 - 1), random.randint(y*5, (y+1)*5 - 1), 1, 1))
                    j += 1
            # draws green if temp == 1
            if (k <= (g // 5) and temp == 1):
                for i in range ((g // 5)):
                    pygame.draw.rect(win_sfc, (0, 255, 0), (random.randint(x*5, (x+1)*5 - 1), random.randint(y*5, (y+1)*5 - 1), 1, 1))
                    k += 1
            # draws blue if temp == 2
            if (l <= (b // 5) and temp == 2):
                for i in range ((b // 5)):
                    pygame.draw.rect(win_sfc, (0, 0, 255), (random.randint(x*5, (x+1)*5 - 1), random.randint(y*5, (y+1)*5 - 1), 1, 1))
                    l += 1
            
# updates window with drawing
pygame.display.update()

# closes pygame window when user presses X button
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()	
