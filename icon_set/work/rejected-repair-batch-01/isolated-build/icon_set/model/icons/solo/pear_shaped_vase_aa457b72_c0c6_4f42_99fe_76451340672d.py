"""A pear-shaped vase with mirrored curved shoulders, an inward neck and a flared mouth."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa457b72-c0c6-4f42-99fe-76451340672d'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/bottle_aa457b72-c0c6-4f42-99fe-76451340672d.svg'
AUTHOR = 'gpt-6'


class PearShapedVase(Solo48):
    icon_id = 'pear-shaped-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('vase', 'bottle', 'ceramic', 'vessel', 'decor', 'flared lip', 'pear shape')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('lip',(16, 4),(32, 4))
        self.add_bezier('neck-right',(32, 4),*(((31.13899825, 5.89833042), (30.64575131, 8.62999417), (30.64575131, 11.5)), ((30.64575131, 14.29600466), (31.13899825, 16.48133566), (32, 18))))
        self.add_arc('shoulder-right',(32, 18),(40, 32),radius_x=8,radius_y=14,large_arc=False,sweep=True)
        self.add_bezier('base-right',(40, 32),*(((37.91276084, 39.18226645), (31.32106476, 44), (24, 44)),))
        self.add_bezier('base-left',(24, 44),*(((16.67893524, 44), (10.08723916, 39.18226645), (8, 32)),))
        self.add_arc('shoulder-left',(8, 32),(16, 18),radius_x=8,radius_y=14,large_arc=False,sweep=True)
        self.add_bezier('neck-left',(16, 18),*(((16.86100175, 16.48133566), (17.35424869, 14.29600466), (17.35424869, 11.5)), ((17.35424869, 8.62999417), (16.86100175, 5.89833042), (16, 4))))
        self.add_contour('vase',*('lip', 'neck-right', 'shoulder-right', 'base-right', 'base-left', 'shoulder-left', 'neck-left'),closed=True)
