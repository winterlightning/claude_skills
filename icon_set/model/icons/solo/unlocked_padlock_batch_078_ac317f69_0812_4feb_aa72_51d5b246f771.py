from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac317f69-0812-4feb-aa72-51d5b246f771'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/unlock keyhole_ac317f69-0812-4feb-aa72-51d5b246f771.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/unlock keyhole_ac317f69-0812-4feb-aa72-51d5b246f771.svg'
# SOLO48 visible extremes (6, 2, 42, 46); centerline extremes (8, 4, 40, 44).
# Construction reference: lock-keyhole-open
# Plan: Open arched shackle and rounded padlock. Round-headed keyhole reduced to a short central slot.

class Batch078Icon(Solo48):
    icon_id = 'unlocked-padlock-batch-078'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('unlocked', 'padlock', 'with', 'keyhole')

    def build(self):

        self.rect('body',8,22,40,44)
        self.add_line('shackle-side',(16,22),(16,12))
        self.add_arc('shackle-top',(16,12),(32,12),radius_x=8)
        self.add_contour('shackle','shackle-side','shackle-top')
        self.relate('connect','shackle','body')
        self.add_line('keyhole',(24,31),(24,35))


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
