"""Upright three-pointed crown in a plain pot. Mirrored elliptic leaf construction informed by Lucide sprout."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64e98c12-a497-4ac3-ad90-841c585f54e3'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_64e98c12-a497-4ac3-ad90-841c585f54e3.svg'
AUTHOR = 'gpt-6'


class UprightThreePointedLeafPlant(Solo48):
    icon_id = 'upright-three-pointed-leaf-plant'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "decoration"
    categories = ("decoration", "state")
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('leaf-left-outer',(16, 32),*(((11.581722, 32.0), (8, 23.045695), (8, 12)),))
        self.add_bezier('leaf-left-inner',(8, 12),*(((13.5228475, 11.5), (18.0, 16.92486775), (18, 23)),))
        self.add_bezier('leaf-centre-left',(18, 23),*(((18.5547095, 12.73089052), (21.08570615, 4), (24, 4)),))
        self.add_bezier('leaf-centre-right',(24, 4),*(((26.91429385, 4), (29.4452905, 12.73089052), (30, 23)),))
        self.add_bezier('leaf-right-inner',(30, 23),*(((30.0, 16.92486775), (34.4771525, 11.5), (40, 12)),))
        self.add_bezier('leaf-right-outer',(40, 12),*(((40, 23.045695), (36.418278, 32.0), (32, 32)),))
        self.add_line('mouth-1',(12, 32),(24, 32))
        self.add_line('mouth-2',(24, 32),(36, 32))
        self.add_line('pot-right',(36, 32),(34, 42))
        self.add_bezier('bottom-right',(34,42),((34,44),(32,44),(30,44)))
        self.add_line('bottom',(30,44),(18,44))
        self.add_bezier('bottom-left',(18,44),((16,44),(14,44),(14,42)))
        self.add_line('pot-left',(14, 42),(12, 32))
        self.add_contour('foliage',*('leaf-left-outer', 'leaf-left-inner', 'leaf-centre-left', 'leaf-centre-right', 'leaf-right-inner', 'leaf-right-outer'),closed=False)
        self.add_contour('mouth',*('mouth-1', 'mouth-2'),closed=False)
        self.add_contour('pot',*('pot-right', 'bottom-right', 'bottom', 'bottom-left', 'pot-left'),closed=False)
        self.relate('connect',*('mouth', 'pot'))
        self.relate('connect',*('foliage', 'mouth'))
