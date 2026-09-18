from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72c9c045-d72a-426c-ae71-33315a0df4b0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/vegetable lavender_72c9c045-d72a-426c-ae71-33315a0df4b0.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/vegetable lavender_72c9c045-d72a-426c-ae71-33315a0df4b0.svg'
# SOLO48 visible extremes (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
# Construction reference: flower-2
# Plan: Two identical open three-petal flowers with paired leaves. Closed petal and leaf loops reduced to open strokes; shared stem origins 12 and 36.

class Batch078Icon(Solo48):
    icon_id = 'two-flower-stems-batch-078'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('two', 'lavender', 'stems')

    def build(self):

        for i,x in enumerate((12,36)):
            n=f'flower-{i}'
            self.add_polyline(n+'-bloom',(x-6,10),(x,16),(x+6,10))
            self.add_line(n+'-petal',(x,6),(x,16))
            self.relate('connect',n+'-bloom',n+'-petal')
            self.add_line(n+'-stem',(x,16),(x,42))
            self.relate('connect',n+'-bloom',n+'-stem')
            self.relate('connect',n+'-petal',n+'-stem')
            self.add_polyline(n+'-leaves',(x-6,28),(x,34),(x+6,28))
            self.relate('connect',n+'-stem',n+'-leaves')


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
