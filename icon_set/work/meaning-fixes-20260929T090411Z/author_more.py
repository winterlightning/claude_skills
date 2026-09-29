from author_batch import *
# Fresh attempts preserve the narrower natural source proportions.
SPECS[0]['body']=SPECS[0]['body'].replace("((9,16),(7,30),(17,37))","((8,19),(8,29),(17,37))").replace("((41,30),(39,16),(31,11))","((40,29),(40,19),(31,11))")
SPECS[1]['body']=SPECS[1]['body'].replace("x,24,2)","x,24,3)")
for i in (4,5):
 SPECS[i]['body']="""curve(self,'handset',(26,4),((18,4),(14,14),(14,24)),((14,34),(18,44),(26,44)),((31,44),(34,44),(34,41)),((34,39),(33,36),(32,34)),((31,31),(28,34),(26,31)),((23,28),(23,20),(26,17)),((28,14),(31,17),(32,14)),((33,12),(34,8),(34,7)),((34,4),(31,4),(26,4)),closed=True)"""
 SPECS[i]['exception']='Preserve the tall narrow handset proportions rather than widening the bowed receiver into a letter C; centered 20-unit body with clean 4px outlines.'
SPECS[6]['body']="""self.add_arc('cap',(10,12),(26,12),radius_x=8)
self.add_line('tube-right',(26,12),(26,28))
self.add_arc('bulb',(26,28),(10,28),radius_x=10,large_arc=True)
self.add_line('tube-left',(10,28),(10,12))
self.add_contour('thermometer','cap','tube-right','bulb','tube-left',closed=True)
self.add_line('mercury',(18,19),(18,35))
self.add_line('scale-top',(35,11),(40,11))
self.add_line('scale-middle',(35,21),(38,21))"""
SPECS[6]['exception']=None
SPECS[12]['body']=SPECS[12]['body'].replace("24,24,6)","24,24,5)")
SPECS[18]['body']=SPECS[18]['body'].replace("(15,34),(25,14),(35,14),(25,34)","(14,34),(24,14),(34,14),(24,34)")
SPECS[18]['exception']=None

define(2,'SQUARE','The drone became an empty capsule with feet, no visible propellers, and angular water.','Restored curved water waves, paired propeller shafts, a broad central body and an underslung equipment pod.', '''
for j,x in enumerate((4,17,30)):
    curve(self,f'wave-{j}',(x,5),((x+4,10),(x+9,10),(x+13,5)))
for x in (9,39):
    self.add_line(f'propeller-{x}',(x-4,16),(x+4,16))
    self.add_line(f'shaft-{x}',(x,16),(x,25))
    self.relate('connect',f'propeller-{x}',f'shaft-{x}')
curve(self,'body',(4,25),((11,25),(12,21),(24,21)),((36,21),(37,25),(44,25)),((47,25),(47,31),(44,31)),((37,31),(33,35),(24,35)),((15,35),(11,31),(4,31)),((1,31),(1,25),(4,25)),closed=True)
for x in (9,39):self.relate('connect','body',f'shaft-{x}')
curve(self,'pod',(15,34),((15,37),(15,42),(19,42)),((22,42),(26,42),(29,42)),((33,42),(33,37),(33,34)))
self.relate('connect','body','pod')
''','gamepad-2: smoothly joined lateral lobes; original supplies the drone-specific body and propulsion','Water, propellers and underside pod are all essential to the underwater drone. Preserve their compact 48px arrangement and true contacts with 4px strokes.')

define(3,'SQUARE','The teeth were inverted scalloped bars and the gum outlines were omitted.','Restored two opposed rows of teeth with rounded crowns, vertical separations and curved gum boundaries.', '''
# Four repeated tooth crowns, mirrored vertically for the lower jaw.
for jaw in ('upper','lower'):
    sy=1 if jaw=='upper' else -1
    def p(x,y):return (x,y if sy==1 else 48-y)
    curve(self,jaw+'-gum',p(4,22),(p(4,17),p(4,10),p(4,8)),(p(15,4),p(33,4),p(44,8)),(p(44,10),p(44,17),p(44,22)))
    self.add_line(jaw+'-bite',p(4,22),p(44,22))
    self.relate('connect',jaw+'-gum',jaw+'-bite')
    for j,x in enumerate((4,14,24,34)):
        curve(self,f'{jaw}-crown-{j}',p(x,16),(p(x+2,10),p(x+8,10),p(x+10,16)))
        if j:
            self.add_line(f'{jaw}-division-{j}',p(x,16),p(x,22))
        self.relate('connect',jaw+'-gum',f'{jaw}-crown-{j}') if j in (0,3) else None
        if j: self.relate('connect',f'{jaw}-division-{j}',f'{jaw}-crown-{j}',f'{jaw}-crown-{j-1}',jaw+'-bite')
''','No useful Lucide dental match; use mirrored repeated crowns derived from the supplied original.','Opposed jaws need four simplified crowns and curved gums; compact crown/gum bands preserve the dental meaning at fixed 4px stroke.')

define(8,'SQUARE','Unenclosed A/B letters and a small plus lost the game-button arrangement and outlined D-pad.','Restored circular A/B buttons and a large outlined directional pad with a center mark.', '''
circle(self,'button-a',12,22,8)
circle(self,'button-b',34,10,8)
# Simple native letterforms are intentionally compact inside their own buttons.
self.add_polyline('a',(9,25),(12,18),(15,25))
self.add_line('a-bar',(10,23),(14,23));self.relate('connect','a','a-bar')
self.add_line('b-stem',(31,6),(31,14))
curve(self,'b',(31,6),((39,5),(39,10),(31,10)),((39,10),(39,15),(31,14)))
self.relate('connect','b-stem','b')
self.add_polyline('dpad',(28,25),(36,25),(36,31),(42,31),(42,39),(36,39),(36,45),(28,45),(28,39),(22,39),(22,31),(28,31),closed=True)
self.add_dot('dpad-center',(32,35))
''','gamepad-2: recognizable directional controls; supplied original: circular A/B buttons and outlined cross','Complete A/B button circles and the outlined D-pad are the defining composition; use compact letter counters and 4px strokes, with visibly separated buttons.')

GAMEPAD='''
curve(self,'controller',(12,26),((7,26),(6,28),(5,34)),((4,39),(4,43),(8,43)),((11,43),(14,37),(17,37)),((21,37),(27,37),(31,37)),((34,37),(37,43),(40,43)),((44,43),(44,39),(43,34)),((42,28),(41,26),(36,26)),((30,26),(18,26),(12,26)),closed=True)
self.add_line('dpad-h',(10,32),(18,32));self.add_line('dpad-v',(14,28),(14,36));self.relate('connect','dpad-h','dpad-v')
self.add_dot('button-left',(31,32));self.add_dot('button-right',(37,32))
'''
define(10,'SQUARE','The team heads were tiny ring marks and the controller lacked any controls.','Restored a recognizable controller with D-pad and action buttons below three clear player busts.', '''
# Repeated players share head radius and shoulder geometry.
for j,cx in enumerate((10,24,38)):
    circle(self,f'head-{j}',cx,7,4)
    curve(self,f'shoulders-{j}',(cx-6,20),((cx-6,13),(cx+6,13),(cx+6,20)))
''' +GAMEPAD,'human_ref/user.svg: circular heads and rounded shoulders; gamepad-2: grips, D-pad and action buttons','Three teammates and a populated controller need compact spacing. Preserve the three-head count and control marks at 48px, with circular heads and rounded shoulders.')
define(11,'SQUARE','The empty controller and two detached arcs lose the familiar gamepad and complete Wi-Fi signal.','Added D-pad and action buttons and restored a centered three-level wireless signal.', '''
curve(self,'wifi-outer',(7,10),((16,2),(32,2),(41,10)))
curve(self,'wifi-inner',(14,16),((20,11),(28,11),(34,16)))
self.add_dot('wifi-point',(24,20))
''' +GAMEPAD,'wifi: nested centered signal arcs; gamepad-2: controller grips and controls','Preserve Wi-Fi plus recognizable controller controls within a single 48px composition. Signal and control spacing remains readable with fixed 4px strokes.')

define(9,'SQUARE','The monitor is blank and the controller has no controls or cable, losing the gaming scene.','Restored the game character on screen, the monitor stand, a connecting cable and gamepad controls.', '''
rounded(self,'monitor',4,4,34,25,3)
self.add_line('stand',(19,25),(19,31));self.add_line('foot',(12,31),(24,31));self.relate('connect','monitor','stand');self.relate('connect','stand','foot')
# Open-mouthed game character is a single closed wedge circle.
self.add_arc('pac-arc',(22,9),(22,21),radius_x=7,large_arc=True,sweep=False)
self.add_polyline('pac-mouth',(22,21),(16,15),(22,9));self.add_contour('pacman','pac-arc','pac-mouth-1','pac-mouth-2',closed=True)
curve(self,'cable',(34,16),((44,16),(44,24),(38,29)));self.relate('connect','monitor','cable')
curve(self,'controller',(21,34),((25,31),(32,30),(37,30)),((44,30),(47,38),(42,42)),((38,46),(34,40),(31,41)),((26,42),(24,46),(20,44)),((14,41),(16,36),(21,34)),closed=True)
self.relate('connect','cable','controller')
self.add_line('dpad-h',(21,39),(27,39));self.add_line('dpad-v',(24,36),(24,42));self.relate('connect','dpad-h','dpad-v')
self.add_dot('button',(37,36))
''','monitor: rounded display and centered stand; gamepad-2: controls and grip silhouette','Gaming on a monitor needs both the on-screen character and gamepad controls. Compact foreground overlap, small letter-like counter and cable are retained with 4px strokes.')

if __name__=='__main__':
 for i in map(int,sys.argv[1:]):write(i,'02' if i in (0,1,4,5,6,12,18) else '01')
