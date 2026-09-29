from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a73a3ea1-b1ee-5adb-a13b-215a290d268a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__view/20260929T090411Z-thuan-mac/reference/view_a73a3ea1-b1ee-5adb-a13b-215a290d268a.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The reference almond eye was replaced by an oval with a heavy tiny pupil.
# Revision plan: Restored pointed eye corners, a balanced almond contour and a larger circular iris.
# Construction reference: eye: pointed almond outline and centered circular iris

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
    icon_id = 'view'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('view',)

    def build(self):
        curve(self,'eye',(4,24),((11,14),(17,10),(24,10)),((31,10),(37,14),(44,24)),((37,34),(31,38),(24,38)),((17,38),(11,34),(4,24)),closed=True)
        circle(self,'iris',24,24,5)
