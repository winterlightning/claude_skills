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
    icon.add_contour(name,name+'-curve',closed=closed)

class Drawing(Solo48):
    icon_id = 'vertical-telephone-receiver'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Preserve the tall narrow handset proportions rather than widening the bowed receiver into a letter C; centered 20-unit body with clean 4px outlines.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '31f9fd17f3cc27a75668158267103625982b0cd3e483f476e10f936b6cb2176d'}
    aliases = ()
    keywords = ('phone vertical',)

    def build(self):
        curve(self,'handset',(26,4),((18,4),(14,14),(14,24)),((14,34),(18,44),(26,44)),((31,44),(34,44),(34,41)),((34,40),(33,36),(32,34)),((31,31),(28,34),(26,31)),((23,28),(23,20),(26,17)),((28,14),(31,17),(32,14)),((33,12),(34,8),(34,7)),((34,4),(31,4),(26,4)),closed=True)
