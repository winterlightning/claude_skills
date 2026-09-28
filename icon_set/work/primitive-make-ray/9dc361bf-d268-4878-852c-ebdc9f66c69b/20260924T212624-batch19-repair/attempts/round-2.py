"""5G lettering is framed by paired network brackets and side ticks.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 SQUARE; omissions: None; hand-authored 5 and G plus all framing marks retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9dc361bf-d268-4878-852c-ebdc9f66c69b'
SOURCE_PATH = 'pictographic-primitives/technology/network 5g_9dc361bf-d268-4878-852c-ebdc9f66c69b.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id='network-5g'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('network', '5g')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):
        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            self.add_polyline('top-'+str(side),p(18,6),p(10,6),p(6,10))
            self.add_polyline('bottom-'+str(side),p(18,42),p(10,42),p(6,38))
        self.add_polyline('five-top',(20,18),(10,18),(10,26),(15,26))
        self.add_arc('five-bowl',(15,26),(15,34),radius_x=4)
        self.add_line('five-foot',(15,34),(10,34))
        self.relate('connect','five-top','five-bowl');self.relate('connect','five-bowl','five-foot')
        self.add_polyline('g',(38,18),(29,18),(29,30),(38,30),(38,26),(34,26))


# Final visible bounds: (4, 4, 44, 44)
# Construction: No useful local Lucide match was used; the supplied reference and shared geometric construction guidance informed this composition.
# Final reductions: None; hand-authored 5 and G plus all framing marks retained.
# Visual review: 5G and surrounding brackets remain recognizable, but ticks merge into letters at native size. Letter/frame and interletter MIC failures retained; not approved.
