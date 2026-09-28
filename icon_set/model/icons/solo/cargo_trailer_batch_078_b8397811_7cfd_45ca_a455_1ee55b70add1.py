from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8397811-7cfd-45ca-a455-1ee55b70add1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/utility trailer_b8397811-7cfd-45ca-a455-1ee55b70add1.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/utility trailer_b8397811-7cfd-45ca-a455-1ee55b70add1.svg'
# SOLO48 visible extremes (2, 8, 46, 40); centerline extremes (4, 10, 44, 38).
# Construction reference: No useful local Lucide subject match
# Plan: Cargo bed and stepped right hitch attach to the exposed wheel at its side extrema. Deliberate side-view asymmetry.

class Batch078Icon(Solo48):
    icon_id = 'cargo-trailer-batch-078'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('utility', 'cargo', 'trailer')

    def build(self):

        self.add_polyline('bed',(4,32),(4,10),(34,10),(34,32),(44,32),(44,18))
        self.add_line('base-left',(4,32),(13,32))
        self.add_line('base-right',(25,32),(34,32))
        self.circle('wheel',19,32,6)
        self.relate('connect','wheel','base-left')
        self.relate('connect','wheel','base-right')
        self.relate('connect','bed','base-left')
        self.relate('connect','bed','base-right')


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
