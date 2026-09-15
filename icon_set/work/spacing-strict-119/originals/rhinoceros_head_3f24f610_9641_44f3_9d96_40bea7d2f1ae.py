"""Upright-horn rhinoceros profile with blunt low jaw and rear ear. Centerline (8,6)-(40,42). Asymmetry follows profile."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f24f610-9641-44f3-9d96-40bea7d2f1ae'
SOURCE_PATH = 'pictographic-primitives/animals/rhinoceros head_3f24f610-9641-44f3-9d96-40bea7d2f1ae.svg'
AUTHOR = 'gpt-6'


class RhinoHeadProfile(Solo48):
    icon_id = 'rhino-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('rhino', 'rhinoceros', 'head', 'horn', 'ears', 'profile', 'animal', 'wildlife')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('top-1',(40, 6),*(((36.68274283, 9.59295314), (31.976566, 11.40302115), (27, 12)),))
        self.add_line('top-2',(27, 12),(27, 4))
        self.add_line('top-3',(27, 4),(20, 8))
        self.add_bezier('top-4',(20, 8),*(((18.21367205, 11.61751346), (18.21367205, 15.90598923), (20, 19)),))
        self.add_line('top-5',(20, 19),(15, 23))
        self.add_bezier('top-6',(15, 23),*(((11.37839694, 17.95369024), (8.98176624, 11.66662675), (8, 4)),))
        self.add_line('top-7',(8, 4),(8, 17))
        self.add_arc('top-8',(8, 17),(12, 31),radius_x=4,radius_y=14,large_arc=False,sweep=False)
        self.add_bezier('jaw-1',(12, 31),*(((9.6376769, 32.57225203), (8.15522233, 35.45818441), (8, 39)),))
        self.add_bezier('jaw-2',(8, 39),*(((9.60262661, 42.54843067), (12.7674284, 44), (16, 44)),))
        self.add_line('jaw-3',(16, 44),(29, 44))
        self.add_bezier('jaw-4',(29, 44),*(((33.80344084, 44), (38.26029632, 40.86141459), (40, 35)),))
        self.add_line('eye',(29, 28),(29, 28))
        self.add_contour('top',*('top-1', 'top-2', 'top-3', 'top-4', 'top-5', 'top-6', 'top-7', 'top-8'),closed=False)
        self.add_contour('jaw',*('jaw-1', 'jaw-2', 'jaw-3', 'jaw-4'),closed=False)
        self.relate('connect',*('top', 'jaw'))
