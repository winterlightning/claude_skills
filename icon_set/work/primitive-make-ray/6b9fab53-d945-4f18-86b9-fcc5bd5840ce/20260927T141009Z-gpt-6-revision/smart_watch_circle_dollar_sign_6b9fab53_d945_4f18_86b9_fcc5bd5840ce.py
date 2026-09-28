from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6b9fab53-d945-4f18-86b9-fcc5bd5840ce'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smartwatch-dollar-sign/20260927T140026Z-thuan-mac-1/reference/smart watch circle dollar sign_6b9fab53-d945-4f18-86b9-fcc5bd5840ce.svg'
AUTHOR="gpt-6"
PARENT_RESULT='icon_set/work/primitive-make-ray/6b9fab53-d945-4f18-86b9-fcc5bd5840ce/20260925-feedback-fed4a5e4/result.json'
USER_SPACING_EXCEPTION={"scope":"dollar symbol only", "approved_by":"user", "reason":"Dollar sign spacing need not be 4 units; explicit feedback in this task."}
class Drawing(Solo48):
    icon_id='smartwatch-dollar-sign'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "combination"
    categories = ("combination", "primitives")
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
        self.circle('dial',24,24,16)
        for x in (16,32):
            for name,y,end in [('top',10,4),('bottom',38,44)]:
                n=f'band-{name}-{x}'
                self.add_line(n,(x,y),(x,end))
                self.relate('connect','dial',n)
        self.add_bezier('s-upper',(29,19),((25,16),(19,17),(19,21)))
        self.add_bezier('s-middle',(19,21),((19,24),(29,24),(29,27)))
        self.add_bezier('s-lower',(29,27),((29,31),(23,33),(19,30)))
        self.add_contour('dollar','s-upper','s-middle','s-lower')
        self.add_line('stem-upper',(24,17),(24,18))
        self.add_line('stem-lower',(24,30),(24,31))
        self.relate('connect','dollar','stem-upper')
        self.relate('connect','dollar','stem-lower')

# Explicit user approval for this exact SVG; changes invalidate the exception.

