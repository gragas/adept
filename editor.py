import pygame

from buffalo import utils

def main():
    
    while not utils.end:
        utils.scene.logic()
        utils.scene.update()
        utils.scene.render()
        utils.delta = utils.clock.tick( utils.FRAMES_PER_SECOND )

if __name__ == "__main__":
    
    if not utils.init(
            caption='Adept Editor',
    ):
        print('buffalo.utils failed to initialize')
        pygame.quit()
        exit()
    
    from editorMenu import EditorMenu

    utils.set_scene( EditorMenu() )
    
    main()
    
    pygame.quit()
