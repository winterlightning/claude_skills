"""Re-authored the three-bead chain diagonally to preserve circular beads and avoid an oversized middle bead.

SQUARE: visible ink (4, 4, 44, 44). Diagonal square construction preserves a narrow subject without stretching it sideways.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '591f9997-10dd-5172-97f4-64f26187164d'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/earring_591f9997-10dd-5172-97f4-64f26187164d.svg'
AUTHOR = 'gpt-6'

class ThreeBeadDropEarring(Solo48):
    icon_id = 'three-bead-drop-earring'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('earring', 'bead', 'drop', 'pearl', 'jewellery', 'jewelry', 'circle', 'accessory')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). Diagonal chain preserves three round beads;
        # a shared circular definition and two true attachment nodes control links.
        for name,cx,cy in [('stud',9,9),('drop',39,39)]:
            self.add_arc(name+'-right',(cx,cy-3),(cx,cy+3),radius_x=3)
            self.add_arc(name+'-left',(cx,cy+3),(cx,cy-3),radius_x=3)
            self.add_contour(name,name+'-right',name+'-left',closed=True)
        points=((16,18),(30,16),(32,30),(18,32),(16,18))
        for i,(a,b) in enumerate(zip(points,points[1:])):self.add_arc(f'main-{i}',a,b,radius_x=10)
        self.add_contour('main',*[f'main-{i}' for i in range(4)],closed=True)
        self.add_line('upper-link',(9,12),(16,18))
        self.add_line('lower-link',(32,30),(39,36))
        for a,b in [('stud','upper-link'),('main','upper-link'),('main','lower-link'),('drop','lower-link')]:self.relate('connect',a,b)
