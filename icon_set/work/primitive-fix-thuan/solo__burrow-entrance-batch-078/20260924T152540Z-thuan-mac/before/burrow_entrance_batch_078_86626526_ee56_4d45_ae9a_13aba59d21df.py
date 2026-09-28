from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86626526-ee56-4d45-ae9a-13aba59d21df'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/warren_86626526-ee56-4d45-ae9a-13aba59d21df.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/warren_86626526-ee56-4d45-ae9a-13aba59d21df.svg'
# SOLO48 visible extremes (2, 8, 46, 40); centerline extremes (4, 10, 44, 38).
# Construction reference: No useful local Lucide subject match
# Plan: Mirrored mound and centered tunnel arch; broad horizontal fit keeps the ground low.

class Batch078Icon(Solo48):
    icon_id = 'burrow-entrance-batch-078'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('underground', 'burrow', 'entrance')

    def build(self):

        self.add_arc('mound',(4,38),(44,38),radius_x=20,radius_y=28)
        self.add_line('ground-left',(4,38),(16,38))
        self.add_arc('entrance',(16,38),(32,38),radius_x=8,radius_y=14)
        self.add_line('ground-right',(32,38),(44,38))
        self.add_contour('earth','ground-left','entrance','ground-right')
        self.relate('connect','mound','earth')


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
