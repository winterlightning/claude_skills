"""A strapless sweetheart bodice opens into a bell skirt. SQUARE 6..42 retains broad hem and small fitted bodice. Symmetry about x24 derives paired silhouette curves. Source supplies neckline and bell silhouette; Lucide shirt supplies clean garment outline. No skirt folds added."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'ff85b0ce-bebc-440e-aed8-c28fc6532c33'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_13/crinoline_ff85b0ce-bebc-440e-aed8-c28fc6532c33.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'sweetheart-bodice-ball-gown'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Elegant Ball Gown Dress',)
    keywords = ('gown', 'dress', 'ball', 'clothing', 'skirt', 'bodice', 'formal')
    def build(self):
        def mirror(p): return (48-p[0],p[1])
        neckline_left = [(16,6),(19,6),(22,8),(24,10)]
        self.add_bezier("neckline",neckline_left[0],tuple(neckline_left[1:]),tuple(mirror(p) for p in reversed(neckline_left[:-1])))
        waist_left, shoulder_left = (18,18),(16,6)
        self.add_line("bodice-right",mirror(shoulder_left),mirror(waist_left))
        skirt_left = [(6,38),(8,30),(11,23),waist_left]
        self.add_bezier("skirt-right",mirror(waist_left),tuple(mirror(p) for p in reversed(skirt_left[:-1])))
        self.add_arc("hem",(42,38),(6,38),radius_x=18,radius_y=4)
        self.add_bezier("skirt-left",skirt_left[0],tuple(skirt_left[1:]))
        self.add_line("bodice-left",waist_left,shoulder_left)
        self.add_contour("gown","neckline","bodice-right","skirt-right","hem","skirt-left","bodice-left",closed=True)
        self.add_line("waist",(18,18),(30,18))
        self.relate("connect","gown","waist")
