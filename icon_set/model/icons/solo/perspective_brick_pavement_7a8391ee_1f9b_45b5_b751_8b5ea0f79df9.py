'Perspective Brick Pavement.\nSymbol plan: A rectangular pavement slab recedes toward a narrower far edge, with a thick rounded front lip. Staggered brick seams divide the surface into three broad rows of long rectangular paving blocks.\nConstruction: Reference-specific coherent contours; no useful exact Lucide match.\nReduction: \nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a8391ee-1f9b-45b5-b751-8b5ea0f79df9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pavement_7a8391ee-1f9b-45b5-b751-8b5ea0f79df9.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'perspective-brick-pavement'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('pavement', 'bricks', 'path', 'sidewalk', 'paving', 'slab')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry,sweep=s)
        def bez(n,a,*s): self.add_bezier(n,a,*s)
        def con(n,*p,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members)&set(p)]
            self.add_contour(n,*p,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            ps=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                if j%2: arc(n+str(j),ps[j],ps[(j+1)%8],r)
                else: line(n+str(j),ps[j],ps[(j+1)%8])
            con(n,*(n+str(j) for j in range(8)),closed=True)
        poly('slab',(14,6),(34,6),(42,34),(42,42),(6,42),(6,34),(14,6))
        line('row1',(12,16),(36,16));line('row2',(9,26),(39,26));line('row3',(6,34),(42,34))
        line('joint1',(24,6),(24,16));line('joint2',(21,16),(21,26));line('joint3',(28,26),(28,34))
        for n in ('row1','row2','row3'):self.relate('connect',n,'slab')
        self.relate('connect','joint2','row1');self.relate('connect','joint2','row2');self.relate('connect','joint3','row2');self.relate('connect','joint3','row3');self.relate('connect','joint1','row1')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
