from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2a9c6ec5-79b6-5a6b-92b4-e35cba30a7db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__type-a-outlet-with-flattened-circular-recess/20260929T090411Z-thuan-mac/reference/power outlet type a_2a9c6ec5-79b6-5a6b-92b4-e35cba30a7db.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The thick compact recess and short slots read as a generic switch face.
# Revision plan: Enlarged the flattened round recess, lengthened the two parallel Type A slots and opened the margins.
# Construction reference: plug: rounded housing and paired terminal spacing

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
    icon_id = 'type-a-outlet-with-flattened-circular-recess'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('power outlet type a',)

    def build(self):
        rounded(self,'plate',4,4,44,44,6)
        curve(self,'recess',(17,11),((9,16),(7,30),(17,37)),((21,37),(27,37),(31,37)),((41,30),(39,16),(31,11)),((27,11),(21,11),(17,11)),closed=True)
        for x in (19,29): self.add_line(f'slot-{x}',(x,20),(x,28))
