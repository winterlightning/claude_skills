'Scalloped Pattypan Squash.\nSymbol plan: A squat squash has a broad scalloped upper outline and rounded lower lobes. A short curved stem rises from the center, while two long curved grooves descend toward the base.\nConstruction: Reference-specific coherent contours; no useful exact Lucide match.\nReduction: Omit narrow internal grooves; retain scalloped body and curved stem.\nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dba8c5fe-82e8-4f2f-81f0-a110247ef3d8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pattypan_dba8c5fe-82e8-4f2f-81f0-a110247ef3d8.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'scalloped-pattypan-squash'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('squash', 'pattypan', 'vegetable', 'stem', 'lobes', 'food')
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
        bez('squash',(4,24),((4,18),(10,16),(14,18)),((16,10),(24,12),(24,16)),((28,12),(36,12),(36,18)),((44,16),(44,22),(44,24)),((44,28),(40,28),(38,32)),((36,40),(28,40),(24,40)),((18,40),(10,40),(8,32)),((4,30),(4,28),(4,24)))
        bez('stem',(24,16),((24,12),(26,8),(30,8)))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
