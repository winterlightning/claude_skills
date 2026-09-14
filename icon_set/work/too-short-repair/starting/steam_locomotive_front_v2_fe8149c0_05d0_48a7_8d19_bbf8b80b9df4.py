# Variant of steam-locomotive-front; parent file remains unchanged.
"""Steam locomotive front; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fe8149c0-05d0-48a7-8d19-bbf8b80b9df4'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad cargo train_fe8149c0-05d0-48a7-8d19-bbf8b80b9df4.svg'
AUTHOR = 'gpt-6'

class SteamLocomotiveFrontVariant2(Solo48):
    icon_id = 'steam-locomotive-front-v2'
    variant_of = 'steam-locomotive-front'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('steam locomotive', 'train', 'locomotive', 'railway', 'front', 'engine', 'vintage', 'rail')

    def build(self) -> None:

        def wheel(name, x, y, r):
            self.add_arc(name + '-right', (x, y - r), (x, y + r), radius_x=r)
            self.add_arc(name + '-left', (x, y + r), (x, y - r), radius_x=r)
            self.add_contour(name, name + '-right', name + '-left', closed=True)
        wheel('smokebox', 24, 24, 10)
        self.add_dot('smokebox-boss', (24, 24))
        self.add_polyline('chimney', (18, 6), (20, 14), (24, 14), (28, 14), (30, 6), closed=True)
        self.add_polyline('chimney-rim', (16, 6), (18, 6), (30, 6), (32, 6))
        self.relate('connect', 'chimney', 'smokebox')
        self.relate('connect', 'chimney', 'chimney-rim')
        self.add_polyline('buffer', (8, 36), (24, 34), (40, 36), (38, 42), (24, 42), (10, 42), closed=True)
        self.relate('connect', 'buffer', 'smokebox')
