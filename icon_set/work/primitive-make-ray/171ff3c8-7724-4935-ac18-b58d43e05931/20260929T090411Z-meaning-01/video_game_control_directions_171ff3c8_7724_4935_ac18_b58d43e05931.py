from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '171ff3c8-7724-4935-ac18-b58d43e05931'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__video-game-control-directions/20260929T090411Z-thuan-mac/reference/video game control directions_171ff3c8-7724-4935-ac18-b58d43e05931.svg'
AUTHOR = "gpt-6"

# Original/current comparison: Unenclosed A/B letters and a small plus lost the game-button arrangement and outlined D-pad.
# Revision plan: Restored circular A/B buttons and a large outlined directional pad with a center mark.
# Construction reference: gamepad-2: recognizable directional controls; supplied original: circular A/B buttons and outlined cross

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
    icon_id = 'video-game-control-directions'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('video game control directions',)

    def build(self):
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
