from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '36ec33e6-3587-4196-b433-a5ed4e77ad2d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__video-game-controller-wifi/20260929T090411Z-thuan-mac/reference/video game controller wifi_36ec33e6-3587-4196-b433-a5ed4e77ad2d.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The empty controller and two detached arcs lose the familiar gamepad and complete Wi-Fi signal.
# Revision plan: Added D-pad and action buttons and restored a centered three-level wireless signal.
# Construction reference: wifi: nested centered signal arcs; gamepad-2: controller grips and controls

def circle(icon, name, cx, cy, r):
    icon.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+'-top',name+'-bottom',closed=True)

def rounded(icon,name,x0,y0,x1,y1,r):
    points=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
    ids=[]
    for j,a in enumerate(points):
        b=points[(j+1)%8];n=f'{name}-{j}';ids.append(n)
        if j%2: icon.add_arc(n,a,b,radius_x=r)
        else: icon.add_line(n,a,b)
    icon.add_contour(name,*ids,closed=True)

def curve(icon,name,start,*segments,closed=False):
    icon.add_bezier(name+'-curve',start,*segments)
    if closed: icon.add_contour(name,name+'-curve',closed=True)

class Drawing(Solo48):
    icon_id = 'video-game-controller-wifi'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('video game controller wifi',)

    def build(self):
        curve(self,'wifi-outer',(7,10),((16,2),(32,2),(41,10)))
        curve(self,'wifi-inner',(14,16),((20,11),(28,11),(34,16)))
        self.add_dot('wifi-point',(24,20))

        curve(self,'controller',(12,26),((7,26),(6,28),(5,34)),((4,39),(4,43),(8,43)),((11,43),(14,37),(17,37)),((21,37),(27,37),(31,37)),((34,37),(37,43),(40,43)),((44,43),(44,39),(43,34)),((42,28),(41,26),(36,26)),((30,26),(18,26),(12,26)),closed=True)
        self.add_line('dpad-h',(10,32),(18,32));self.add_line('dpad-v',(14,28),(14,36));self.relate('connect','dpad-h','dpad-v')
        self.add_dot('button-left',(31,32));self.add_dot('button-right',(37,32))
