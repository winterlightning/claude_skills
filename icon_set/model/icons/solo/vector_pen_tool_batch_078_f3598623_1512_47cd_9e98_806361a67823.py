from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3598623-1512-47cd-9e98-806361a67823'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/vectors pen anchor_f3598623-1512-47cd-9e98-806361a67823.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/vectors pen anchor_f3598623-1512-47cd-9e98-806361a67823.svg'
# SOLO48 visible extremes (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
# Construction reference: pen-tool
# Plan: Three square nodes form a peaked vector path above an upright nib. Equal 8-unit nodes share corner connections; nib has curved base and slit. Omit the short holder to preserve space.

class Batch078Icon(Solo48):
    icon_id = 'vector-pen-tool-batch-078'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('vector', 'pen', 'tool')

    def build(self):
        # Three square nodes share an 8-unit side; connections reuse corners.
        for name,x,y in [('left',4,20),('top',20,8),('right',36,20)]:
            self.add_polyline(name,(x,y),(x+8,y),(x+8,y+8),(x,y+8),closed=True)
        self.add_line('vector-left',(12,20),(20,16))
        self.add_line('vector-right',(28,16),(36,20))
        for line,node in [('vector-left','left'),('vector-left','top'),('vector-right','top'),('vector-right','right')]:
            self.relate('connect',line,node)
        self.add_line('nib-right',(24,25),(30,34))
        self.add_arc('nib-base',(30,34),(18,34),radius_x=6)
        self.add_line('nib-left',(18,34),(24,25))
        self.add_contour('nib','nib-right','nib-base','nib-left',closed=True)
        self.add_line('slit',(24,25),(24,29))
        self.relate('connect','slit','nib')

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
