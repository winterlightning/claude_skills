from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '529f66ce-bbc1-4b10-b496-db11d5c10c2e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/typing machine 1_529f66ce-bbc1-4b10-b496-db11d5c10c2e.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/typing machine 1_529f66ce-bbc1-4b10-b496-db11d5c10c2e.svg'
# SOLO48 visible extremes (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
# Construction reference: keyboard
# Plan: Sheet, carriage and curved body; one row of keys replaces small roller knobs and front-panel details.

class Batch078Icon(Solo48):
    icon_id = 'manual-typewriter-batch-078'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "office"
    categories = ("office", "primitive", "primitives")
    aliases = ()
    keywords = ('vintage', 'manual', 'typewriter')

    def build(self):

        self.add_polyline('paper',(14,16),(14,6),(34,6),(34,16))
        self.add_line('carriage',(6,16),(42,16))
        self.relate('connect','paper','carriage')
        self.rect('body',6,24,42,42,4)
        for i,x in enumerate((16,24,32)):
            self.add_dot(f'key-{i}',(x,33))


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
