'Triangular Ozone Molecule.\nSymbol plan: Three circular atoms form an uneven triangle, with one at the left and two stacked on the right. Straight connecting bonds join each pair, enclosing a small open triangular space between them.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: \nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f6112893-74f5-4941-8d09-471ef8c89a26'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/ozone_f6112893-74f5-4941-8d09-471ef8c89a26.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'triangular-ozone-molecule'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('ozone', 'molecule', 'atoms', 'bonds', 'chemistry', 'science')
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
        circle('left',12,26,6);circle('top',34,12,6);circle('bottom',36,36,6)
        line('bond-a',(16,22),(30,16));line('bond-b',(16,30),(31,33));line('bond-c',(39,15),(40,32))
        for n,a,b in [('a','left','top'),('b','left','bottom'),('c','top','bottom')]:self.relate('connect','bond-'+n,a);self.relate('connect','bond-'+n,b)
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
