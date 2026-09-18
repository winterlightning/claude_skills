from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f13e2b9-c07a-43d0-9624-7e137d24fb27'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/vectors pen new anchor_7f13e2b9-c07a-43d0-9624-7e137d24fb27.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-078/references/vectors pen new anchor_7f13e2b9-c07a-43d0-9624-7e137d24fb27.svg'
# SOLO48 visible extremes (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
# Construction reference: pen-tool
# Plan: Downward nib uses a rounded cap above the central square anchor and mirrored vector arcs. Omit slit and small endpoint squares to preserve the editing action at native size.

class Batch078Icon(Solo48):
    icon_id = 'pen-editing-anchor-batch-078'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('vector', 'pen', 'tool', 'and', 'anchor', 'point')

    def build(self):

        self.add_arc('nib-cap',(16,14),(32,14),radius_x=8)
        self.add_line('nib-right',(32,14),(24,22))
        self.add_line('nib-left',(24,22),(16,14))
        self.add_contour('nib','nib-cap','nib-right','nib-left',closed=True)
        self.add_polyline('anchor',(19,30),(29,30),(29,40),(19,40),closed=True)
        self.add_arc('curve-left',(6,42),(19,35),radius_x=13,radius_y=7)
        self.add_arc('curve-right',(29,35),(42,42),radius_x=13,radius_y=7)
        self.relate('connect','curve-left','anchor')
        self.relate('connect','curve-right','anchor')


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
