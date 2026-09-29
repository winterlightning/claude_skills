from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ba09f2a8-8b62-435c-9541-abb3adc7212a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wip-logo/20260929T090411Z-thuan-mac/reference/wip logo_ba09f2a8-8b62-435c-9541-abb3adc7212a.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The distinctive outlined diagonal parallelogram was reduced to a slash.
# Revision plan: Restored the closed slanted logo bar within its rounded square.
# Construction reference: monitor: consistent rounded frame

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
    icon_id = 'wip-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('wip logo',)

    def build(self):
        rounded(self,'frame',6,6,42,42,5)
        self.add_polyline('logo',(15,34),(25,14),(35,14),(25,34),closed=True)
