from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b1f2ce85-d591-4522-b2a6-64d3fc5c75f6'
SOURCE_PATH='pictographic-primitives/combination/smart watch circle yuan sign_b1f2ce85-d591-4522-b2a6-64d3fc5c75f6.svg'
AUTHOR="gpt-6"
PARENT_RESULT='icon_set/work/primitive-make-ray/b1f2ce85-d591-4522-b2a6-64d3fc5c75f6/20260925-feedback-fed4a5e4/result.json'
class Drawing(Solo48):
    icon_id='smart-watch-yuan-symbol'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        points=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        for i,a in enumerate(points):
            z=points[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,z,radius_x=rad)
            else:self.add_line(n+str(i),a,z)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)
    def build(self):
        # Exact circle: centre (24,24), radius 16. Strap caps terminate inside the bezel ink; no tiny tips enter the dial.
        self.circle('dial',24,24,16)
        contact=10
        for x in (16,32):
            for name,y,end in [('top',contact,4),('bottom',48-contact,44)]:
                n=f'band-{name}-{x}';self.add_line(n,(x,y),(x,end));self.relate('connect','dial',n)
        self.add_polyline('yuan-fork',(19,19),(24,25),(29,19))
        self.add_polyline('yuan-bar',(20,25),(24,25),(28,25))
        self.add_line('yuan-stem',(24,25),(24,31));self.relate('connect','yuan-fork','yuan-bar','yuan-stem')
