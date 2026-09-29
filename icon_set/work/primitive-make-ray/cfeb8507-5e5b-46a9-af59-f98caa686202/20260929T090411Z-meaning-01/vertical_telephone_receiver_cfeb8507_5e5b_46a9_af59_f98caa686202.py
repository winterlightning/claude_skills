from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cfeb8507-5e5b-46a9-af59-f98caa686202'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vertical-telephone-receiver/20260929T090411Z-thuan-mac/reference/phone vertical_cfeb8507-5e5b-46a9-af59-f98caa686202.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The receiver became a wide block letter C instead of a bowed handset.
# Revision plan: Restored the narrow curved spine, cupped earpiece and mouthpiece, and tapered inner grip.
# Construction reference: phone: continuous rounded receiver contour and smooth inner bend

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
    icon_id = 'vertical-telephone-receiver'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('phone vertical',)

    def build(self):
        # One smooth bowed spine and two rounded, forward-facing receiver cups.
        curve(self,'handset',(29,4),((18,4),(10,12),(10,24)),((10,36),(18,44),(29,44)),((33,44),(38,44),(38,40)),((38,38),(36,34),(35,32)),((34,30),(28,32),(26,30)),((23,27),(23,21),(26,18)),((28,16),(34,18),(35,16)),((36,14),(38,8),(38,7)),((38,4),(33,4),(29,4)),closed=True)
