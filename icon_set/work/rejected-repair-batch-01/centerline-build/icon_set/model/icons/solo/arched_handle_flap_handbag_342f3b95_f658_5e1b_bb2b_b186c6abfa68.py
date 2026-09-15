"""Lucide shopping-bag: arched handle and rounded body; mirrored flap. Omitted tiny clasp to keep the flap clear."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '342f3b95-f658-5e1b-bb2b-b186c6abfa68'
SOURCE_PATH = 'pictographic-primitives/shopping/products purse_342f3b95-f658-5e1b-bb2b-b186c6abfa68.svg'
AUTHOR = 'gpt-6'

class ArchedHandleFlapHandbag(Solo48):
    icon_id = 'arched-handle-flap-handbag'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('handbag', 'purse', 'bag', 'handle', 'clasp', 'fashion', 'accessory')

    def build(self) -> None:
        # VRECT_L centerline extremes (8,4)-(40,44).
        axis=24
        self.add_polyline('top',(8,22),(8,18),(14,18),(34,18),(40,18),(40,22))
        self.add_line('right',(40,22),(40,36))
        self.add_arc('br',(40,36),(32,44),radius_x=8)
        self.add_line('base',(32,44),(16,44))
        self.add_arc('bl',(16,44),(8,36),radius_x=8)
        self.add_line('left',(8,36),(8,22))
        self.add_contour('body','right','br','base','bl','left')
        self.relate('connect','top','body')
        self.add_arc('handle',(14,18),(2*axis-14,18),radius_x=10,radius_y=14)
        self.relate('connect','handle','top')
        self.add_arc('flap',(8,22),(40,22),radius_x=16,radius_y=12,sweep=False)
        self.relate('connect','flap','top')
        self.relate('connect','flap','body')
