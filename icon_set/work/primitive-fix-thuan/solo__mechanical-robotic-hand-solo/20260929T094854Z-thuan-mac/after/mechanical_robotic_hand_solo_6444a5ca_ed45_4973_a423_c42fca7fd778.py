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
    exception = {'reason': 'Mechanical wrist, palm and thumb seams need compact connected panels; preserve the side-view hand silhouette and4px strokes.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'a314a43e7a2dd1890fbe2eb0b3fd7c2417e5294d251742a41560ddf3afa3cbde'}
    aliases = ()
    keywords = ('hand robot',)

    def build(self):
        # Natural asymmetry: side-view hand with thumb pointing up-right.
        curve(self,'outline',(4,12),((6,10),(8,9),(11,10)),((14,10),(17,11),(19,12)),((22,13),(25,14),(28,15)),((31,16),(33,19),(31,23)),((31,23),(36,18),(36,18)),((36,18),(38,16),(38,16)),((42,12),(47,18),(42,23)),((42,23),(40,25),(40,25)),((40,25),(32,33),(32,33)),((30,35),(28,36),(25,36)),((20,36),(14,35),(10,34)),((10,34),(4,33),(4,33)),((4,33),(4,12),(4,12)),closed=True)
        curve(self,'cuff',(11,10),((16,18),(15,27),(10,34)))
        self.add_polyline('folded-finger',(19,12),(19,23))
        curve(self,'knuckle',(19,23),((22,24),(24,26),(27,26)),((29,26),(31,26),(31,23)))
        self.relate('connect','folded-finger','knuckle')
        self.relate('connect','outline','folded-finger');self.relate('connect','outline','knuckle')
        self.relate('connect','outline','cuff')
        self.relate('connect','knuckle','palm-seam')
        self.add_line('palm-seam',(27,26),(25,36));self.relate('connect','outline','palm-seam')
        self.add_line('thumb-joint',(36,18),(40,25));self.relate('connect','outline','thumb-joint')
