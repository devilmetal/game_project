import pygame
import constants
import routines

class CharacterMenu:
    selected = 0
    font_size = 32
    font_path = 'data/coders_crux/coders_crux.ttf'
    font = pygame.font.Font
    screen = None
    characters = None
    def __init__(self,screen,unlocked_chars):
        #Init the menu
        #Draw with position = 1
        self.screen=screen
        bob = routines.load_png('hero_3/idle_l.png')
        hulk = routines.load_png('hero_1/idle_l.png')
        little_fat = routines.load_png('hero_2/idle_l.png')
        #bob2 = routines.load_png('hero/idle_l.png')


        #self.characters = [bob,hulk]
        if unlocked_chars == 0:
            self.characters = [hulk]
        elif unlocked_chars == 1:
            self.characters = [hulk, bob]
        else:
            self.characters = [hulk, bob, little_fat]

        self.draw(0)

    def fib(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

    #Used inside the run() function with events.
    def draw_by_hop(self,menu_hop):
        # menu_hop = +1/-1
        #Compute new_position according to menu_hop and self.char_list
        modulo = len(self.characters)
        new_position = (self.selected+menu_hop) % modulo
        self.selected = new_position
        #Draw the menu at new position
        self.draw(new_position)


    def draw(self,position):
        #Set the new selected character according to position
        self.selected = position
        #Draw the next position of menu
        #Draw background
        bg = routines.draw_rectangle(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.BLACK)
        #Draw funky text
        txt1 = routines.draw_text("Select your Badass", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/5 - 20, 52, "data/coders_crux/coders_crux.ttf", constants.WHITE)
        txt2 = routines.draw_text("and go kick some asses !", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/5 + 20, 38, "data/coders_crux/coders_crux.ttf", constants.WHITE)
        bg.blit(txt1[0], txt1[1])
        bg.blit(txt2[0], txt2[1])
        self.screen.blit(bg, (0,0))

        #Create layout of character display according to lenght of self.char_list
        #standard width of character frame
        image_width=40
        x_deviation = int(constants.SCREEN_WIDTH/(len(self.characters)+1))
        y_position = constants.SCREEN_HEIGHT/2
        scale_tail = self.fib(len((self.characters)))
        #Draw all figures
        for character in self.characters:
            #Compute position
            position = self.characters.index(character)
            x_position = x_deviation * (position+1) - image_width/2
            character[1].x = x_position
            character[1].y = y_position
            #Rescale image
            character_scale = pygame.transform.scale(character[0], (int(float(character[1].width)*float(2.0/scale_tail)), int(float(character[1].height)*float(2.0/scale_tail))))
            #Draw background rect of selected figure according to self.selected
            if position == self.selected:
                back = pygame.Surface([int(float(character[1].width)*float(2.0/scale_tail))+40, int(float(character[1].height)*float(2.0/scale_tail))+40])
                back.fill((153,102,255))
                back_rect = character[1].copy()
                back_rect.x-=20
                back_rect.y-=20
                self.screen.blit(back, back_rect)
            #Blit
            self.screen.blit(character_scale, character[1])
            #Draw figure
        #Update the stuff
        pygame.display.update()

    def run(self,joystick):
        #Run the menu selection
        done = False
        while not done:
            #Catch events
            #If ok press => return character selected (aka this.selected)
            for event in pygame.event.get():

                #Joystick stuff
                if event.type == pygame.JOYHATMOTION:
                    hat = joystick.get_hat(0)
                    if (1, 0) == hat:
                        self.draw_by_hop(1)
                    if (-1, 0) == hat:
                        self.draw_by_hop(-1)
                if event.type == pygame.JOYBUTTONDOWN:
                    if joystick.get_button(1) == 1:#X button
                        constants.GAME_STATUS = "menuLevel"
                        return self.selected
                    if joystick.get_button(2) == 1:#O button
                        constants.GAME_STATUS = "menuDiff"
                        done = True

                #Keyboard stuff
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.draw_by_hop(1)
                    if event.key == pygame.K_LEFT:
                        self.draw_by_hop(-1)
                    if event.key == pygame.K_RETURN:
                        constants.GAME_STATUS = "menuLevel"
                        return self.selected
                    if event.key == pygame.K_BACKSPACE:
                        constants.GAME_STATUS = "menuDiff"
                        done = True
                    if event.key == pygame.K_ESCAPE:
                        constants.GAME_STATUS="exit"
                        done = True
                elif event.type == pygame.QUIT:
                    constants.GAME_STATUS="exit"
                    done = True
            pygame.time.wait(8)
