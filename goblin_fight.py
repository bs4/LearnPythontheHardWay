# Rock 'em, Sock 'em Goblins

import random


class EnterRing(object):

    def __init__(self):
        pass
        
    def fighter(self):
        
        #gladiator = ['Hacker', 'Slasher', 'Poker', 'Gouger', 'Ripper']
        
        random.shuffle(gladiator)
        self.gladiator = gladiator.pop()
                    
        return self.gladiator
    
    def health(self):
    
        self.healthpoints = random.randint(19, 22)
        return self.healthpoints 
        
    def weapon(self):
        
        weap = ['axe', 'sword', 'mattock', 'bow', 'poo nugget', 'wiener',
            'loud voice', 'pretty eyes', 'bare fists', 'spinal column']
        
        random.shuffle(weap)
        self.type = weap.pop()
        return self.type


class Battle(object):
    
    def __init__(self):
        pass    
    
    def attack(self, goblin1, goblin2, goblin1_hp, goblin2_hp):
        
        while goblin1_hp > 0 and goblin2_hp > 0:
        
            dmg_x = random.randint(1, 4)
            
            goblin2_hp = goblin2_hp - dmg_x
            
            print "%s hits %s for %d damage, %s's hp = %d" % (goblin1, 
                goblin2, dmg_x, goblin2, goblin2_hp)
                
            dmg_y = random.randint(1, 4)
                
            goblin1_hp = goblin1_hp - dmg_y
            
            print "%s hits %s for %d damage, %s's hp = %d" % (goblin2,
                goblin1, dmg_y, goblin1, goblin1_hp)
        
            
        
        if goblin1_hp <= 0 and goblin2_hp <= 0:
            return 'Nobody...simultaneous death-blows have left us with only one winner, the crowd!'
            
        elif goblin1_hp <= 0:
            return goblin2
            
        else:
            return goblin1
        
gladiator = ['Hacker', 'Slasher', 'Poker', 'Gouger', 'Ripper']
        
gob1 = EnterRing()
gob2 = EnterRing()

gob1_name = gob1.fighter()
gob2_name = gob2.fighter()

gob1_health = gob1.health()
gob2_health = gob2.health()

gob1_weap = gob1.weapon()
gob2_weap = gob2.weapon()

batt = Battle()


print "\nEntering the ring is %s" % gob1_name
print "%s wields a %s and touts an HP of %d" % (gob1_name, gob1_weap,
    gob1_health)
    
print "Now coming into the ring is %s." % gob2_name
print "%s wields a %s and boasts an HP of %d.\n" % (gob2_name,
    gob2_weap, gob2_health)
    
#print "%s hits for %s. %s is current health of %s." % gob1_name, batt.attack(gob2_health), gob2_name

winner = batt.attack(gob1_name, gob2_name, gob1_health, gob2_health)

print "\nOur gladiators have fought tooth, nail...%s and %s." % (gob1_weap,
    gob2_weap)
print "And the champion is....%s!!!" % winner






































