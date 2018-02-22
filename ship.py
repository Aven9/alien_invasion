# coding=utf-8
import pygame


class Ship:

    def __init__(self, screen):
        """初始化飞船并设置其位置"""
        self.screen = screen

        self.image = pygame.image.load('image/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # center, centerx, centery, top, bottom, left, right
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
            self.blitme()
