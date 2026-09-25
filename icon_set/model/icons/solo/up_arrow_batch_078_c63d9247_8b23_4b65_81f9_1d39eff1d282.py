from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c63d9247-8b23-4b65-81f9-1d39eff1d282'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/up 3_c63d9247-8b23-4b65-81f9-1d39eff1d282.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/up 3_c63d9247-8b23-4b65-81f9-1d39eff1d282.svg'
# SOLO48 visible extremes (6, 2, 42, 46); centerline extremes (8, 4, 40, 44).
# Construction reference: arrow-up
# Plan: Single shared apex joins mirrored open arrowhead to vertical shaft.

class Batch078Icon(Solo48):
    icon_id = 'up-arrow-batch-078'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    categories = ("arrows", "primitive", "primitives")
    aliases = ()
    keywords = ('upward', 'pointing', 'arrow')

    def build(self):

        axis=24
        apex=(axis,4)
        self.add_polyline('arrowhead',(8,20),apex,(40,20))
        self.add_line('shaft',apex,(axis,44))
        self.relate('connect','arrowhead','shaft')


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
