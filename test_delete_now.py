class CentralCorridor(object):
    def test_print(self):
        print "This is only a test"
        
    def enter(self):
        print "Test for CentralCorridor.Enter()"
        

class LaserWeaponArmory(object):
    pass
    
class TheBridge(object):
    pass
    
class EscapePod(object):
    pass
    
class Death(object):
    pass
    
class Finished(object):
    pass


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)



class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()
        
      





      
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()