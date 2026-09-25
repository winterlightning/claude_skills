from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6b9fab53-d945-4f18-86b9-fcc5bd5840ce'
SOURCE_PATH='pictographic-primitives/combination/smart watch circle dollar sign_6b9fab53-d945-4f18-86b9-fcc5bd5840ce.svg'
AUTHOR="gpt-6"
PARENT_RESULT='icon_set/work/primitive-make-ray/6b9fab53-d945-4f18-86b9-fcc5bd5840ce/20260925-fresh-c5fdae55/result.json'
USER_SPACING_EXCEPTION={"scope":"dollar symbol only", "approved_by":"user", "reason":"Dollar sign spacing need not be 4 units; explicit feedback in this task."}
class Drawing(Solo48):
    icon_id='smartwatch-dollar-sign'
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
        # Exact circle: centre (24,24), radius 16. Strap rails overlap the bezel at their actual intersections.
        from math import sqrt
        self.circle('dial',24,24,16)
        contact=11
        for x in (16,32):
            for name,y,end in [('top',contact,4),('bottom',48-contact,44)]:
                n=f'band-{name}-{x}';self.add_line(n,(x,y),(x,end));self.relate('connect','dial',n)
        # Full recognizable S and a through-stem. User explicitly accepts tight dollar spacing.
        self.add_bezier('dollar-top',(28,19),((20,15),(16,22),(24,24)))
        self.add_bezier('dollar-bottom',(24,24),((32,26),(28,33),(20,29)))
        self.add_contour('dollar','dollar-top','dollar-bottom')
        self.add_line('dollar-stem',(24,17),(24,31));self.relate('connect','dollar','dollar-stem')
