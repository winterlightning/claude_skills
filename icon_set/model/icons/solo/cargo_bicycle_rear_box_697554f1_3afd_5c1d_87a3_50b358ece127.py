"""A cargo bicycle with a rounded rear carrier and hooked handlebar. SQUARE ink (6,6)-(42,42). Lucide bike informed equal wheels. The mounted carrier is intrinsic cargo, not a modifier; lower frame detail omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '697554f1-3afd-5c1d-87a3-50b358ece127'
SOURCE_PATH = 'pictographic-primitives/transportation/bike cargo back_697554f1-3afd-5c1d-87a3-50b358ece127.svg'
SOURCE_REFERENCES = (('697554f1-3afd-5c1d-87a3-50b358ece127', 'pictographic-primitives/transportation/bike cargo back_697554f1-3afd-5c1d-87a3-50b358ece127.svg'),)
AUTHOR = 'gpt-6'

class CargoBicycleRearBox(Solo48):
    icon_id = 'cargo-bicycle-rear-box'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('cargo bike', 'bicycle', 'delivery', 'box', 'carrier', 'cycling', 'transport', 'courier')

    def build(self) -> None:
        for side,x in [('rear',12),('front',36)]:
            self.add_arc(side+'-right',(x,30),(x,42),radius_x=6)
            self.add_arc(side+'-left',(x,42),(x,30),radius_x=6)
            self.add_contour(side+'-wheel',side+'-right',side+'-left',closed=True)
        # The box owns repeated corner radii and explicit frame/rack attachment nodes.
        self.add_line('box-top',(9,6),(21,6))
        self.add_arc('box-tr',(21,6),(24,9),radius_x=3)
        self.add_line('box-right-1',(24, 9),(24, 12))
        self.add_line('box-right-2',(24, 12),(24, 15))
        self.add_arc('box-br',(24,15),(21,18),radius_x=3)
        self.add_line('box-bottom-1',(21, 18),(12, 18))
        self.add_line('box-bottom-2',(12, 18),(9, 18))
        self.add_arc('box-bl',(9,18),(6,15),radius_x=3)
        self.add_line('box-left',(6,15),(6,9))
        self.add_arc('box-tl',(6,9),(9,6),radius_x=3)
        self.add_contour('box','box-top','box-tr','box-right-1','box-right-2','box-br','box-bottom-1','box-bottom-2','box-bl','box-left','box-tl',closed=True)
        self.add_line('rack',(12,18),(12,30))
        self.add_line('top-tube',(24,12),(33,12))
        self.add_polyline('fork',(36,30),(33,12),(33,6),(39,6))
        self.add_arc('bar-curl',(39,6),(39,12),radius_x=3)
        for a,b in [('rack','box'),('rack','rear-wheel'),('top-tube','box'),('top-tube','fork'),('fork','front-wheel'),('fork','bar-curl')]:
            self.relate('connect',a,b)
