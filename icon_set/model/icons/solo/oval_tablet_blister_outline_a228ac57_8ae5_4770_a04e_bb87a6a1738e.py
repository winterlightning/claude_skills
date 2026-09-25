'Oval Tablet Blister Outline.\nSymbol plan: A small horizontal capsule shaped form sits inside a larger matching oval surround. Both outlines have straight middle sections and rounded ends, with a broad even gap between them.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: \nKeyshape HRECT_M.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a228ac57-8ae5-4770-a04e-bb87a6a1738e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blister_a228ac57-8ae5-4770-a04e-bb87a6a1738e.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'oval-tablet-blister-outline'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('tablet', 'blister', 'pill', 'oval', 'capsule', 'medicine', 'packaging')
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
        rect('outer',4,10,40,28,14)
        rect('inner',14,19,20,10,5)
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
