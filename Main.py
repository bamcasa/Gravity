import pygame
import sys
import random

pygame.init()

class Flappybird:
    def __init__(self):
        self.FPS = 30
        self.screen = pygame.display.set_mode((500, 500))
        self.screen.fill((255,255,255))
        self.ball_x = 100
        self.ball_y = 100
        self.ball = 0
        self.speed = 1
        self.clicked = False
        self.abc = False
    def show(self):
        self.screen.fill((255,255,255))
        self.ball = pygame.draw.circle(self.screen, (190,190,190), [self.ball_x, self.ball_y], 40)
        #print(self.ball_y)
    def gravity(self):
        if self.crash(self.ball_x,self.ball_y + 5):
            self.ball_y += 460 - self.ball_y
            return
        self.speed *= (9.8 / 9)
        self.ball_y += self.speed

    def crash(self,x,y):
        if y >= 460:
            self.speed = 1
            return True

    def drag(self):
        if self.clicked:
            pos = pygame.mouse.get_pos()
            if self.abc:
                self.ball_x, self.ball_y = pos[0], pos[1]
                self.speed = 0

    def main(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        while True:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked = True
                    pos = pygame.mouse.get_pos()
                    if self.ball.collidepoint(pos):
                        self.abc = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.abc:
                        self.speed = 1
                        self.clicked = False
                        self.abc = False
            self.drag()
            self.gravity()
            Flappybird.show(self)
            pygame.display.flip()

if __name__ == "__main__":
    Flappybird().main()
