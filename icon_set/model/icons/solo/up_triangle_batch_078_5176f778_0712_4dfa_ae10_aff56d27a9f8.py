from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5176f778-0712-4dfa-ae10-aff56d27a9f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/up 2_5176f778-0712-4dfa-ae10-aff56d27a9f8.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/up 2_5176f778-0712-4dfa-ae10-aff56d27a9f8.svg'
# SOLO48 visible extremes (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
# Construction reference: triangle
# Plan: Mirrored sloping sides and horizontal base form a single closed contour.

class Batch078Icon(Solo48):
    icon_id = 'up-triangle-batch-078'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ()
    keywords = ('upward', 'pointing', 'triangle')

    def build(self):

        self.add_polyline('triangle',(24,8),(44,40),(4,40),closed=True)


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
