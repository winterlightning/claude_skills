'Open Scissors with Round Finger Loops.\nSymbol plan: A pair of open scissors has two large round finger loops beneath long crossing blades. The blades flare slightly near their pointed tips, forming a tall open V above the crossing point.\nConstruction: Lucide scissors: round finger loops and crossing blade strokes.\nReduction: Single broad blade strokes replace narrow double outlines.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c19bdc8c-e6d8-415f-8dbf-d5c6f7397b98'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shears_c19bdc8c-e6d8-415f-8dbf-d5c6f7397b98.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-scissors-with-round-finger-loops'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('scissors', 'shears', 'cutting', 'blades', 'handles', 'tool')
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
        circle('loop-left',13,35,7);circle('loop-right',35,35,7)
        line('blade-a',(17,29),(42,6));line('blade-b',(31,29),(6,6))
        self.relate('connect','blade-a','loop-left');self.relate('connect','blade-b','loop-right')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
