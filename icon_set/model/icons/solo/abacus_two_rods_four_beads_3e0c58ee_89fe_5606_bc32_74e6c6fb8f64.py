"""Traditional Counting Abacus."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e0c58ee-89fe-5606-bc32-74e6c6fb8f64'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/abacus_3e0c58ee-89fe-5606-bc32-74e6c6fb8f64.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'abacus-two-rods-four-beads'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/finance'
    aliases = ()
    keywords = ('abacus', 'counting', 'bead', 'rod', 'math', 'finance', 'calculation')

    def build(self):
        # Plan: Frame owns two rod instances spaced 18 units. Each has two rounded beads; staggered bead centers. No useful Lucide abacus match. Bounds (6,6)-(42,42).
        self.add_polyline('frame',(6,6),(15,6),(33,6),(42,6),(42,42),(33,42),(15,42),(6,42),closed=True)
        for i,(x,ys) in enumerate([(15,(15,31)),(33,(17,33))]):
            y0,y1=ys
            for j,(a,b) in enumerate([(6,y0),(y0,y1),(y1,42)]):
                self.add_line(f'rod-{i}-{j}',(x,a),(x,b))
            self.add_contour(f'rod-{i}',*[f'rod-{i}-{j}' for j in range(3)])
            self.relate('connect',f'rod-{i}','frame')
            for j,y in enumerate(ys):
                self.add_line(f'bead-{i}-{j}',(x-3,y),(x,y))
                self.add_line(f'bead-r-{i}-{j}',(x,y),(x+3,y))
                self.add_contour(f'bead-shape-{i}-{j}',f'bead-{i}-{j}',f'bead-r-{i}-{j}')
                self.relate('connect',f'rod-{i}',f'bead-shape-{i}-{j}')
