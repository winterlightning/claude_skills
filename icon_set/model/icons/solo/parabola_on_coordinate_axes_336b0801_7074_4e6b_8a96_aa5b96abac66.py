'Parabola on Coordinate Axes.\nSymbol plan: A smooth upward-opening curve crosses a vertical axis above its intersection with a horizontal axis. The horizontal axis ends in a right-facing arrow, while the curve rises symmetrically on either side.\nConstruction: Lucide chart-spline: a clean curve sharing coordinate axes.\nReduction: \nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '336b0801-7074-4e6b-8a96-aa5b96abac66'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/science axis_336b0801-7074-4e6b-8a96-aa5b96abac66.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'parabola-on-coordinate-axes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('parabola', 'axis', 'graph', 'curve', 'mathematics', 'science')
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
        line('x',(6,38),(42,38));line('y',(24,6),(24,42))
        bez('curve',(6,8),((8,22),(14,28),(24,28)),((34,28),(40,22),(42,8)))
        poly('arrow',(36,32),(42,38),(36,42))
        self.relate('connect','x','y');self.relate('connect','curve','y');self.relate('connect','arrow','x')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
