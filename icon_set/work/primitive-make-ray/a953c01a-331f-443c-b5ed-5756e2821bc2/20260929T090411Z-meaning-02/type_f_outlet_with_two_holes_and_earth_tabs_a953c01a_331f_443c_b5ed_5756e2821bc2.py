from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a953c01a-331f-443c-b5ed-5756e2821bc2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__type-f-outlet-with-two-holes-and-earth-tabs/20260929T090411Z-thuan-mac/reference/power outlet type f_a953c01a-331f-443c-b5ed-5756e2821bc2.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The tiny holes and heavy concentric frames read as a face; earth contacts are cramped.
# Revision plan: Balanced the circular recess and clearly separated two pin holes with aligned earth contacts.
# Construction reference: plug: paired terminals and rounded housing

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
    icon_id = 'type-f-outlet-with-two-holes-and-earth-tabs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Retain the defining two circular holes and top/bottom earth tabs within a complete socket plate; compact concentric margins remain visibly open at 48px.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'e34cbddad943ba946c36102213ccd2fce91252084dfd3cb2a7cd9956f393d3b5'}
    aliases = ()
    keywords = ('power outlet type f',)

    def build(self):
        rounded(self,'plate',4,4,44,44,6)
        circle(self,'recess',24,24,14)
        for x in (18,30): circle(self,f'pin-{x}',x,24,3)
        self.add_line('earth-top',(24,10),(24,15))
        self.add_line('earth-bottom',(24,33),(24,38))
        self.relate('connect','recess','earth-top')
        self.relate('connect','recess','earth-bottom')
