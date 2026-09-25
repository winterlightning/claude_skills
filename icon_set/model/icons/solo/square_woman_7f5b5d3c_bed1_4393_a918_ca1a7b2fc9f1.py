from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='7f5b5d3c-bed1-4393-a918-ca1a7b2fc9f1'
SOURCE_PATH='pictographic-primitives/other/square woman_7f5b5d3c-bed1-4393-a918-ca1a7b2fc9f1.svg'
AUTHOR="gpt-6"
PARENT_RESULT='icon_set/work/primitive-make-ray/7f5b5d3c-bed1-4393-a918-ca1a7b2fc9f1/20260925-fresh-c5fdae55/result.json'
class Drawing(Solo48):
    icon_id='square-woman'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    human_construction="bust"
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
        # Full circular face, long hair and detached, broad shoulder arch.
        self.box('frame',6,6,42,42,2)
        self.circle('head',24,20,5)
        for side in (-1,1):
            n=f'hair-{side}';self.add_bezier(n,(24+side*5,20),((24+side*5,22),(24+side*6,25),(24+side*7,26)));self.relate('connect','head',n)
        self.add_arc('shoulder-left',(15,42),(24,33),radius_x=9)
        self.add_arc('shoulder-right',(24,33),(33,42),radius_x=9)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        self.relate('connect','frame','shoulders')

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '89edbc14acc9412e448f9e4a4752671f0d1a257b5a576ddfd4c0d94900518fc7', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '7f5b5d3c-bed1-4393-a918-ca1a7b2fc9f1'}
