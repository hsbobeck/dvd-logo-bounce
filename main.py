#
# @title DVD Logo Bounce
# 
# @author Henry Bobeck
# @date 230927
#
#

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 23.976
LOGO_WIDTH, LOGO_HEIGHT = 227, 100
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Logo(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(pygame.image.load("sprites/dvdlogo.png"), self.rect.size)
        self.color = color
        self.x_vel = 5
        self.y_vel = 5
        
    def update(self):
        # bounce on screen edges
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.x_vel *= -1
        if self.rect.y <= 0 or self.rect.y + self.rect.height >= SCREEN_HEIGHT:
            self.y_vel *= -1
        
        # move
        self.rect.move_ip(self.x_vel, self.y_vel)


def main():
    pygame.display.set_caption("DVD Logo Bounce")
    clock = pygame.time.Clock()

    logo = Logo(SCREEN_WIDTH/2 - LOGO_WIDTH/2, SCREEN_HEIGHT/2 - LOGO_HEIGHT/2, LOGO_WIDTH, LOGO_HEIGHT, "blue")
    logos = pygame.sprite.Group()
    logos.add(logo)

    run = True
    while run:
        clock.tick(FPS)

        # event handler
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                run = False
                break

        logos.update()
        win.fill("black")
        logos.draw(win)
        pygame.display.flip()
    
    pygame.quit()
    quit()

if __name__ == "__main__":
  main()