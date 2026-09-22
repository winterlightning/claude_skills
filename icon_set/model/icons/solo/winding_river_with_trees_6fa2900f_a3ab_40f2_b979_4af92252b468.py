"""A winding stream between two round-crowned trees. SQUARE keeps the two trees and foreground banks balanced. Repeated tree definition shares radius6 and trunk length8. Lucide tree-deciduous supplies crown-to-trunk attachment. Fine crown lobes and foreground boundary omitted; asymmetric bank curves retained.
Source editorial brief is preserved in the gallery; source supplies identity and arrangement.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '6fa2900f-a3ab-40f2-b979-4af92252b468'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bayou_6fa2900f-a3ab-40f2-b979-4af92252b468.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'winding-river-with-trees'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ['Winding River with Trees']
    keywords = ['river', 'stream', 'trees', 'landscape', 'water', 'bank', 'nature']

    def build(self):
        for side,x in enumerate((12,36)):
            self.add_arc(f"crown-{side}-left",(x,18),(x,6),radius_x=6)
            self.add_arc(f"crown-{side}-right",(x,6),(x,18),radius_x=6)
            self.add_contour(f"crown-{side}",f"crown-{side}-left",f"crown-{side}-right",closed=True)
            self.add_line(f"trunk-{side}",(x,18),(x,26))
            self.relate("connect",f"crown-{side}",f"trunk-{side}")
        self.add_bezier("far-bank",(26,26),((18,26),(18,30),(24,32)),((30,34),(36,36),(32,42)))
        self.add_bezier("near-bank",(6,34),((12,34),(17,36),(12,42)))
