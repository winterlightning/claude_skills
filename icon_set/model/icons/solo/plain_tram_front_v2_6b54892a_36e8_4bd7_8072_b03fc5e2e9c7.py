"""Plain tram front; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6b54892a-36e8-4bd7-8072-b03fc5e2e9c7'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad train_6b54892a-36e8-4bd7-8072-b03fc5e2e9c7.svg'
AUTHOR = 'gpt-6'

class PlainTramFrontVariant2(Solo48):
    icon_id = 'plain-tram-front-v2'
    variant_of = 'plain-tram-front'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('tram', 'train', 'front', 'streetcar', 'railway', 'light rail', 'simple', 'transport')

    def build(self) -> None:
        self.add_line('roof-1', (12, 12), (24, 12))
        self.add_line('roof-2', (24, 12), (36, 12))
        self.add_arc('upper-right', (36, 12), (40, 16), radius_x=4)
        self.add_line('right-wall-1', (40, 16), (40, 26))
        self.add_line('right-wall-2', (40, 26), (40, 32))
        self.add_line('right-wall-3', (40, 32), (40, 36))
        self.add_arc('lower-right', (40, 36), (36, 40), radius_x=4)
        self.add_line('base-1', (36, 40), (34, 40))
        self.add_line('base-2', (34, 40), (30, 40))
        self.add_line('base-3', (30, 40), (18, 40))
        self.add_line('base-4', (18, 40), (14, 40))
        self.add_line('base-5', (14, 40), (12, 40))
        self.add_arc('lower-left', (12, 40), (8, 36), radius_x=4)
        self.add_line('left-wall-1', (8, 36), (8, 32))
        self.add_line('left-wall-2', (8, 32), (8, 26))
        self.add_line('left-wall-3', (8, 26), (8, 16))
        self.add_arc('upper-left', (8, 16), (12, 12), radius_x=4)
        self.add_contour('body', 'roof-1', 'roof-2', 'upper-right', 'right-wall-1', 'right-wall-2', 'right-wall-3', 'lower-right', 'base-1', 'base-2', 'base-3', 'base-4', 'base-5', 'lower-left', 'left-wall-1', 'left-wall-2', 'left-wall-3', 'upper-left', closed=True)
        self.add_polyline('divider', (8, 26), (24, 26), (40, 26))
        self.relate('connect', 'body', 'divider')
        for name, x, end in [('left', 14, 8), ('right', 34, 40)]:
            self.add_line(name + '-rail', (x, 40), (end, 44))
            self.relate('connect', name + '-rail', 'body')
        self.add_line('mast', (24, 4), (24, 12))
        self.add_polyline('pantograph-bar', (16, 4), (24, 4), (32, 4))
        self.relate('connect', 'mast', 'body')
        self.relate('connect', 'mast', 'pantograph-bar')
