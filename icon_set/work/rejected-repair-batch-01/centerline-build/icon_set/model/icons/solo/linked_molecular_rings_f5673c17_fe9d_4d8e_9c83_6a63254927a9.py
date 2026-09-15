"""Two hexagonal molecular rings connect diagonally from lower left to upper right by a short bond. A separate circular atom joins the upper-left corner of the higher ring through another straight bond.

SQUARE visible bounds (4,4)-(44,44); two hexagonal rings, connecting bond and terminal circular atom. Lucide network informed node attachments, with molecular geometry preserving the diagonal arrangement. No ring count reduction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5673c17-fe9d-4d8e-9c83-6a63254927a9'
SOURCE_PATH = 'pictographic-primitives/science/molecule strucutre_f5673c17-fe9d-4d8e-9c83-6a63254927a9.svg'
AUTHOR = 'gpt-6'

class LinkedMolecularRings(Solo48):
    icon_id = 'linked-molecular-rings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('molecule', 'ring', 'bond', 'atom', 'chemistry', 'structure')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_polyline('lower-ring',(6,29),(14,24),(22,29),(22,37),(14,42),(6,37),closed=True)
        self.add_polyline('upper-ring',(26,13),(34,8),(42,13),(42,21),(34,26),(26,21),closed=True)
        self.add_line('inter-ring-bond',(22,29),(26,21))
        self.relate('connect','inter-ring-bond','lower-ring');self.relate('connect','inter-ring-bond','upper-ring')
        self.circle('terminal-atom',13,10,4)
        self.add_line('terminal-bond',(17,10),(26,13))
        self.relate('connect','terminal-bond','terminal-atom');self.relate('connect','terminal-bond','upper-ring')
