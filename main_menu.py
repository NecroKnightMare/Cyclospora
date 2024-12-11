import pygame
import sys

def main_menu_screen(screen, font, text_color, screen_width, screen_height, clock, main_menu_image, menu_options, selected_option):
    global current_scene
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if selected_option == 0:
                        return "intro"
                    elif selected_option == 1:
                        pygame.quit()
                        sys.exit()

        screen.blit(main_menu_image, (0, 0))
        
        menu_text = font.render("Cyclospora", True, text_color)
        screen.blit(menu_text, (screen_width // 2 - menu_text.get_width() // 2, 100))
        
        for i, option in enumerate(menu_options):
            option_text = font.render(option, True, text_color)
            screen.blit(option_text, (screen_width // 2 - option_text.get_width() // 2, 300 + i * 50))
            if i == selected_option:
                pygame.draw.rect(screen, (255, 255, 255), (screen_width // 2 - option_text.get_width() // 2 - 10, 300 + i * 50 - 10, option_text.get_width() + 20, option_text.get_height() + 20), 2)
        
        pygame.display.flip()
        clock.tick(60)
