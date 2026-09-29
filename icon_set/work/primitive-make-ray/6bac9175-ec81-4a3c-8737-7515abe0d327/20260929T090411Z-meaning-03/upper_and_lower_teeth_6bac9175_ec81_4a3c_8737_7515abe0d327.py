from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6bac9175-ec81-4a3c-8737-7515abe0d327'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__upper-and-lower-teeth/20260929T090411Z-thuan-mac/reference/dentistry tooth jaws_6bac9175-ec81-4a3c-8737-7515abe0d327.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The teeth were inverted scalloped bars and the gum outlines were omitted.
# Revision plan: Restored two opposed rows of teeth with rounded crowns, vertical separations and curved gum boundaries.
# Construction reference: No useful Lucide dental match; use mirrored repeated crowns derived from the supplied original.

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
    icon_id = 'upper-and-lower-teeth'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Opposed jaws need four simplified crowns and curved gums; compact crown/gum bands preserve the dental meaning at fixed 4px stroke.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '1cb3f37ac8b7b8d5425e068a2f0d590f6f21208e203a179f27f851a0de0edb9b'}
    aliases = ()
    keywords = ('dentistry tooth jaws',)

    def build(self):

        # Two rows of four crowns; facing bite edges are 8 units apart.
        for jaw in ('upper','lower'):
            def p(x,y):return (x,y if jaw=='upper' else 48-y)
            curve(self,jaw+'-gum',p(4,20),(p(4,16),p(4,10),p(4,7)),(p(15,3),p(33,3),p(44,7)),(p(44,10),p(44,16),p(44,20)))
            self.add_line(jaw+'-bite',p(4,20),p(44,20))
            self.relate('connect',jaw+'-gum',jaw+'-bite')
            for j,x in enumerate((4,14,24,34)):
                curve(self,f'{jaw}-crown-{j}',p(x,14),(p(x+2,9),p(x+8,9),p(x+10,14)))
                if j:
                    self.add_line(f'{jaw}-division-{j}',p(x,14),p(x,20))
                    for part in (f'{jaw}-crown-{j}',f'{jaw}-crown-{j-1}',jaw+'-bite'):
                        self.relate('connect',f'{jaw}-division-{j}',part)
                    self.relate('connect',f'{jaw}-crown-{j}',f'{jaw}-crown-{j-1}')
                if j in (0,3):self.relate('connect',jaw+'-gum',f'{jaw}-crown-{j}')

