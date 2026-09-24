'Diagonal Satellite with a Dish.\nSymbol plan: A rounded satellite body tilts from lower left to upper right between two rectangular solar panels. A curved dish projects from its lower-left end, with two radiating signal arcs beyond it.\nConstruction: Lucide satellite: diagonal central body, opposing panels and emitted signal arc.\nReduction: Retain the central body, two broad solar panels, and dish; omit the small feed and signal arcs.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ff0c5fdb-1159-4e0b-9e80-1a4fa4f96e73'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/antenna 1_ff0c5fdb-1159-4e0b-9e80-1a4fa4f96e73.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'diagonal-satellite-with-a-dish'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('satellite', 'dish', 'solar panels', 'space', 'signal', 'communication', 'orbit')
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
        poly('body',(20,20),(32,8),(40,16),(28,28),closed=True)
        poly('panel-a',(20,20),(6,10),(16,6),(28,16))
        poly('panel-b',(32,24),(42,34),(34,42),(24,32))
        bez('dish',(6,26),((6,36),(12,42),(22,42)))
        self.relate('connect','panel-a','body');self.relate('connect','panel-b','body')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
