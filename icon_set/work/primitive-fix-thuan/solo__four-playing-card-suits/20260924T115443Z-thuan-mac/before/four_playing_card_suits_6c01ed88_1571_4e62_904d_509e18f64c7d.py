"Playing Card Suits.\nSymbol plan: Four outlined suits remain separate, with compact lobes and shared stems.\nConstruction: Lucide original and atomic-debug: bath, truck, notebook, piano, orbit, sprout and pill-bottle; coherent arcs, shared joins and repeated dimensions.\nKeyshape SQUARE: exact SOLO48 contract envelope, selected for this subject's proportions.\nSource UUID and original reference preserved."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6c01ed88-1571-4e62-904d-509e18f64c7d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/card game symbols_6c01ed88-1571-4e62-904d-509e18f64c7d.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'four-playing-card-suits'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('cards', 'suits', 'diamond', 'club', 'spade', 'heart', 'game')
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
        poly('diamond',(13,6),(20,13),(13,20),(6,13),closed=True)
        # Four suit symbols occupy four distinct quadrants; no modifier relationship.
        bez('heart',(35,42),((30,38),(28,35),(29,32)),((29,28),(33,27),(35,31)),((38,27),(42,28),(42,32)),((42,36),(38,39),(35,42)))
        bez('spade',(13,29),((10,32),(6,34),(6,37)),((6,41),(10,41),(13,38)),((16,41),(20,41),(20,37)),((20,34),(16,32),(13,29)))
        line('spadestem',(13,38),(13,42))
        bez('club',(32,13),((28,8),(32,6),(35,6)),((40,6),(40,10),(38,13)),((42,10),(42,14),(42,16)),((42,20),(38,20),(35,17)),((32,20),(28,20),(28,16)),((28,13),(30,12),(32,13)))
        line('clubstem',(35,17),(35,20))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
