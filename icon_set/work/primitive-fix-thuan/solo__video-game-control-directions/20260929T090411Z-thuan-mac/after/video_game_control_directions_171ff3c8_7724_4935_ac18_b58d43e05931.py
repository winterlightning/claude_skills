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
    icon.add_contour(name,name+'-curve',closed=closed)

class Drawing(Solo48):
    icon_id = 'video-game-control-directions'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Complete A/B button circles and the outlined D-pad are the defining composition; use compact letter counters and 4px strokes, with visibly separated buttons.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '07c05095fb6b0e6ddf5f2d0e3dcf36f1157dc5b826d6d8f879ccd819d2e02b3f'}
    aliases = ()
    keywords = ('video game control directions',)

    def build(self):

        # Diagonal pair of enclosed A/B buttons and separate outlined D-pad.
        circle(self,'button-a',12,25,10)
        circle(self,'button-b',35,13,11)
        self.add_polyline('a',(9,29),(12,21),(15,29))
        self.add_line('a-bar',(10,27),(14,27));self.relate('connect','a','a-bar')
        self.add_line('b-stem',(32,7),(32,19))
        curve(self,'b',(32,7),((40,7),(40,13),(32,13)),((40,13),(40,19),(32,19)))
        self.relate('connect','b-stem','b')
        self.add_polyline('dpad',(30,28),(38,28),(38,33),(44,33),(44,41),(38,41),(38,46),(30,46),(30,41),(24,41),(24,33),(30,33),closed=True)

