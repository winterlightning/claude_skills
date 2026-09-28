'Pencil beside Drawn Squiggle.\nSymbol plan: A broad pencil tilts from a pointed lower left tip toward a rounded upper right end. A loose curling line runs beside the tip, bending downward across the left side of the drawing.\nConstruction: Lucide pencil: diagonal barrel, rounded cap and pointed end.\nReduction: One loose squiggle beside the broad pencil.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '09802860-599e-4eb4-b68f-43ddebc59be7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pen draw 2_09802860-599e-4eb4-b68f-43ddebc59be7.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'pencil-drawn-squiggle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('pencil', 'scribble', 'drawing', 'line', 'writing', 'tool')
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
        poly('pencil',(20,36),(24,22),(34,12));arc('cap',(34,12),(42,20),8,s=True)
        poly('edge',(42,20),(32,30),(20,36))
        bez('squiggle',(14,6),((10,10),(6,14),(6,18)),((6,22),(14,22),(12,26)),((12,32),(6,34),(6,38)),((6,42),(8,42),(10,42)))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
