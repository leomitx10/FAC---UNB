import pygame

# Inicialização do Pygame
pygame.init()

# Definição da tela
screen = pygame.display.set_mode((800, 600))

# Título da janela
pygame.display.set_caption("Jogo de Plataforma")

# Definição do personagem
player_image = pygame.image.load("player.png").convert_alpha()
player_pos = [400, 500]

# Definição do inimigo
enemy_image = pygame.image.load("enemy.png").convert_alpha()
enemy_pos = [100, 100]

# Loop de jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_pos[1] -= 10
            if event.key == pygame.K_s:
                player_pos[1] += 10
            if event.key == pygame.K_a:
                player_pos[0] -= 10
            if event.key == pygame.K_d:
                player_pos[0] += 10

    # Atualização da tela
    screen.fill((0,0,0))
    screen.blit(player_image, player_pos)
    screen.blit(enemy_image, enemy_pos)
    pygame.display.update()

# Finalização do Pygame
pygame.quit()
