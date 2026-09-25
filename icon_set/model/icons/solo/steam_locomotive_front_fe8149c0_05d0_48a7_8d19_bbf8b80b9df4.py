"""Steam locomotive front; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fe8149c0-05d0-48a7-8d19-bbf8b80b9df4'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad cargo train_fe8149c0-05d0-48a7-8d19-bbf8b80b9df4.svg'
AUTHOR = 'gpt-6'

class SteamLocomotiveFront(Solo48):
    icon_id = 'steam-locomotive-front'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('steam locomotive', 'train', 'locomotive', 'railway', 'front', 'engine', 'vintage', 'rail')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.

        def wheel(name, x, y, r):
            self.add_arc(name + '-right', (x, y - r), (x, y + r), radius_x=r)
            self.add_arc(name + '-left', (x, y + r), (x, y - r), radius_x=r)
            self.add_contour(name, name + '-right', name + '-left', closed=True)
        wheel('smokebox', 24, 24, 10)
        self.add_dot('smokebox-boss', (24, 24))
        self.add_polyline('chimney', (18, 4), (20, 14), (24, 14), (28, 14), (30, 4), closed=True)
        self.add_polyline('chimney-rim', (16, 4), (18, 4), (30, 4), (32, 4))
        self.relate('connect', 'chimney', 'smokebox')
        self.relate('connect', 'chimney', 'chimney-rim')
        self.add_polyline('buffer', (8, 36), (24, 34), (40, 36), (38, 44), (24, 44), (10, 44), closed=True)
        self.relate('connect', 'buffer', 'smokebox')
