from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7221711-2b13-4937-944a-889c96a2a3f7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/vials_b7221711-2b13-4937-944a-889c96a2a3f7.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/vials_b7221711-2b13-4937-944a-889c96a2a3f7.svg'
# SOLO48 visible extremes (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
# Construction reference: test-tubes
# Plan: Repeated rounded test tubes retain unequal liquid levels. Broad rim overhangs reduced to a single top edge.

class Batch078Icon(Solo48):
    icon_id = 'two-test-tubes-batch-078'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('two', 'laboratory', 'test', 'tubes')

    def build(self):

        for i,x in enumerate((6,30)):
            n=f'tube-{i}'
            self.add_line(n+'-left',(x,6),(x,36))
            self.add_arc(n+'-base',(x,36),(x+12,36),radius_x=6,sweep=False)
            self.add_line(n+'-right',(x+12,36),(x+12,6))
            self.add_line(n+'-rim',(x+12,6),(x,6))
            self.add_contour(n,n+'-left',n+'-base',n+'-right',n+'-rim',closed=True)
            self.add_line(n+'-liquid',(x,22+i*8),(x+12,22+i*8))
            self.relate('connect',n,n+'-liquid')


    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rect(self, name, l, t, r, b, radius=4):
        k=radius
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        for j in range(8):
            a,z=pts[j],pts[(j+1)%8]
            if j%2: self.add_arc(name+str(j),a,z,radius_x=k)
            else: self.add_line(name+str(j),a,z)
        self.add_contour(name,*(name+str(j) for j in range(8)),closed=True)
