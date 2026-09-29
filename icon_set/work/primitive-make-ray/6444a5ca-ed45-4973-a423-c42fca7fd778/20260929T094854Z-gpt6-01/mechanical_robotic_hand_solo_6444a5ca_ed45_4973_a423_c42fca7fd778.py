from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6444a5ca-ed45-4973-a423-c42fca7fd778'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mechanical-robotic-hand-solo/20260929T094854Z-thuan-mac/reference/hand robot_6444a5ca-ed45-4973-a423-c42fca7fd778.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The robotic hand lost its closed palm and folded finger joints, becoming an open tool or gripper.
# Revision plan: Restored a closed palm, curved wrist cuff, folded finger segment and articulated extended thumb.
# Construction reference: hand: continuous rounded palm and finger construction; original supplies mechanical joints and side-view pose

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
    icon_id = 'mechanical-robotic-hand-solo'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('hand robot',)

    def build(self):
        # Natural asymmetry: side-view hand with thumb pointing up-right.
        curve(self,'upper',(4,12),((10,8),(14,10),(19,12)),((22,13),(25,14),(28,15)),((31,16),(33,19),(31,23)))
        self.add_polyline('thumb-upper',(31,23),(36,18),(38,16))
        curve(self,'thumb-tip',(38,16),((42,12),(47,18),(42,23)))
        self.add_polyline('thumb-lower',(42,23),(40,25),(32,33))
        curve(self,'lower',(32,33),((30,35),(28,36),(25,36)),((18,36),(10,34),(4,33)))
        self.add_line('wrist-edge',(4,33),(4,12))
        self.add_contour('outline','upper-curve','thumb-upper-1','thumb-upper-2','thumb-tip-curve','thumb-lower-1','thumb-lower-2','lower-curve','wrist-edge',closed=True)
        curve(self,'cuff',(11,10),((16,18),(15,27),(10,34)))
        self.add_polyline('folded-finger',(19,12),(19,23))
        curve(self,'knuckle',(19,23),((24,24),(29,29),(31,23)))
        self.relate('connect','folded-finger','knuckle')
        self.relate('connect','outline','folded-finger');self.relate('connect','outline','knuckle')
        self.add_line('palm-seam',(27,26),(25,36));self.relate('connect','outline','palm-seam')
        self.add_line('thumb-joint',(36,18),(40,25));self.relate('connect','outline','thumb-joint')
