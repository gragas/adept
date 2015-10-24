import pygame
import random

class Disk: # Something we can create and manipulate
    def __init__(self,color,pos,size): # initialize the properties of the object
        self.color=color
        self.pos=pos
        self.size=50
    
    def Render(self,screen):
        pygame.draw.circle(screen,self.color,self.pos,self.size)
        #circle = pygame.draw.circle(screen,self.color,self.pos,self.size)

def main(): # Where we start
    screen=pygame.display.set_mode((600,400))
    running=True
    RenderList=[] # list of objects
    MousePressed=False # Pressed down THIS FRAME
    MouseDown=False # mouse is held down
    MouseReleased=False # Released THIS FRAME
    Target=None # target of Drag/Drop
    while running:
        screen.fill((255,255,255)) # clear screen
        pos=pygame.mouse.get_pos()
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                running=False
                break # get out now
            
            if Event.type == pygame.MOUSEBUTTONDOWN:
                MousePressed=True 
                MouseDown=True
                #circle.fill((int(random.random()+254),int(random.random()+254),int(random.random()+254))) 
               
            if Event.type == pygame.MOUSEBUTTONUP:
                MouseReleased=True
                MouseDown=False
                
             
        if MousePressed==True:
            for item in RenderList: # search all items
                if (pos[0]>=(item.pos[0]-item.size) and 
                    pos[0]<=(item.pos[0]+item.size) and 
                    pos[1]>=(item.pos[1]-item.size) and 
                    pos[1]<=(item.pos[1]+item.size) ): # inside the bounding box
                    Target=item # "pick up" item
            
            if Target is None: # didn't find any?
                Target=Disk((0,0,255),pos,10) # create a new one
                RenderList.append(Target) # add to list of things to draw
            
        if MouseDown and Target is not None: # if we are dragging something
            Target.pos=pos # move the target with us
        
        if MouseReleased:
            Target=None # Drop item, if we have any
            
        for item in RenderList:
            item.Render(screen) # Draw all items
            
        MousePressed=False # Reset these to False
        MouseReleased=False # Ditto        
        pygame.display.flip()
    return # End of function
    
if __name__ == '__main__': # Are we RUNNING from this module?
    main() # Execute our main function