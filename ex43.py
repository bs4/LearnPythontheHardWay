from sys import exit
from random import randint


class Scene(object):
        
    def enter(self):  
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
        
        
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
        current_scene.enter()
    
        
class Death(Scene):
    
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
        
        
class CentralCorridor(Scene):
    
    def enter(self):
        print "This is the first paragraph of CentralCorridor."
        
        action = raw_input('> ')
        
        if action == "shoot!":
            print "This is if action of CentralCorridor."
            return 'death'
            
        elif action == "dodge!":
            print "This is elif action dodge of CentralCorridor."
            return 'death'
            
        elif action == "tell a joke":
            print "This is elif action tell a joke of CentralCorridor."
            return 'laser_weapon_armory'
            
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'
        
        
class LaserWeaponArmory(Scene):

    def enter(self):
        print "This is the first paragraph of LaserWeaponArmory."
        
        code = "%d%d%d" % (randint(1,2), randint(1,2), randint(1,2))
        guess = raw_input("[keypad]> ")
        guesses = 1
        cheat = '000'
        
        while guess != code and guess != cheat and guesses < 10:
            print "BSSSSEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
            
        if guess == code:
            print "You got the code right! Grab bomb, run to bridge."
            return 'the_bridge'
            
        elif guess == cheat:
            print "Clever girl (english accent, a la Jurassic Park)"
            return 'the_bridge'
            
        else:
            print "You lose the keypad # guessing game."
            return 'death'

        
class TheBridge(Scene):
    
    def enter(self):
        print "This is the first paragraph on TheBridge."
        
        action = raw_input('> ')
        
        if action == "throw the bomb":
            print "if action of TheBridge."
            return 'death'
            
        elif action == "slowly place the bomb":
            print "elif action slowly place bomb of TheBridge."
            return 'escape_pod'
        
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"
        
        
class EscapePod(Scene):

    def enter(self):
        print "This is the first paragraph of EscapePod."
        
        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")
        
        if int(guess) != good_pod:
            print "This is if EscapePod. pod guess: %s." % guess
            print "but oh no! this damaged pod implodes crushing you."
            return 'death'
            
        else:
            print "This is else EscapePod. pod guess: %s." % guess
            print "Yeah! this is the safe pod. you win!"
            return 'finished'
        

class Finished(Scene):
    
    def enter(self):
        print "I won? No, you won! Hahahahaha!!"
        return 'finished'
        

class Map(object):
    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'finished': Finished(),
        'death': Death()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

































