import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Primitives")
screen.fill((255, 255, 255))

# Отрисовка окружности, линии, и текста
pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)
pygame.draw.line(screen, (0, 255, 0), (100, 100), (700, 500), 3)
pygame.draw.line(screen, (0, 0, 255), (200, 500), (600, 100), 3)

# Текст
font = pygame.font.Font(None, 36)
text = font.render("Примитивы в Pygame", True, (0, 0, 0))
screen.blit(text, (250, 50))

pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
