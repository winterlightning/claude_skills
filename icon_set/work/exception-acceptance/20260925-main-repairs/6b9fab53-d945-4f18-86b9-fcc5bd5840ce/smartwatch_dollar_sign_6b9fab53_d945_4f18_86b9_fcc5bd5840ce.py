from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='6b9fab53-d945-4f18-86b9-fcc5bd5840ce'
SOURCE_PATH='pictographic-primitives/combination/smart watch circle dollar sign_6b9fab53-d945-4f18-86b9-fcc5bd5840ce.svg'
AUTHOR="gpt-6"
PARENT_RESULT='icon_set/work/primitive-make-ray/6b9fab53-d945-4f18-86b9-fcc5bd5840ce/20260925-feedback-fed4a5e4/result.json'
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
        # Exact circle: centre (24,24), radius 16. Strap caps terminate inside the bezel ink; no tiny tips enter the dial.
        self.circle('dial',24,24,16)
        contact=10
        for x in (16,32):
            for name,y,end in [('top',contact,4),('bottom',48-contact,44)]:
                n=f'band-{name}-{x}';self.add_line(n,(x,y),(x,end));self.relate('connect','dial',n)
        # Clean S with terminal currency ticks, as in the reference.
        # No through-stem closes tiny internal slivers. Tight S spacing remains user-approved.
        self.add_bezier('dollar-start',(28,19),((27,18),(26,18),(24,18)))
        self.add_bezier('dollar-top',(24,18),((16,18),(16,24),(24,24)))
        self.add_bezier('dollar-bottom',(24,24),((32,24),(32,30),(24,30)))
        self.add_bezier('dollar-end',(24,30),((22,30),(21,30),(20,29)))
        self.add_contour('dollar','dollar-start','dollar-top','dollar-bottom','dollar-end')
        self.add_line('dollar-tick-top',(24,17),(24,18))
        self.add_line('dollar-tick-bottom',(24,30),(24,31))
        self.relate('connect','dollar','dollar-tick-top');self.relate('connect','dollar','dollar-tick-bottom')

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'c6c895ff8605afe58364cb00f7bc1a03e74f90eaba41711052224bee45f6f01d', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '6b9fab53-d945-4f18-86b9-fcc5bd5840ce'}
