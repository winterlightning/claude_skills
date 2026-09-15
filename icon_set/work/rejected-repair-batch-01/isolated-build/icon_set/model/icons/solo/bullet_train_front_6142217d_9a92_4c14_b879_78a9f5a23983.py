"""Bullet train front; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6142217d-9a92-4c14-b879-78a9f5a23983'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad metro_6142217d-9a92-4c14-b879-78a9f5a23983.svg'
AUTHOR = 'gpt-6'

class BulletTrainFront(Solo48):
    icon_id = 'bullet-train-front'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('bullet train', 'metro', 'train', 'front', 'railway', 'high speed', 'rail', 'subway')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('roof', (11, 14), (37, 14), radius_x=13, radius_y=10)
        self.add_line('right-flank', (37, 14), (37, 30))
        self.add_arc('lower-right', (37, 30), (29, 38), radius_x=8)
        self.add_line('base', (29, 38), (19, 38))
        self.add_arc('lower-left', (19, 38), (11, 30), radius_x=8)
        self.add_line('left-flank', (11, 30), (11, 14))
        self.add_contour('body', 'roof', 'right-flank', 'lower-right', 'base', 'lower-left', 'left-flank', closed=True)
        self.add_line('windscreen-base', (11, 14), (37, 14))
        self.relate('connect', 'windscreen-base', 'body')
        self.add_arc('headlight-right', (24, 23), (24, 29), radius_x=3)
        self.add_arc('headlight-left', (24, 29), (24, 23), radius_x=3)
        self.add_contour('headlight', 'headlight-right', 'headlight-left', closed=True)
        self.add_line('left-rail', (19, 38), (8, 44))
        self.add_line('right-rail', (29, 38), (40, 44))
        self.relate('connect', 'left-rail', 'body')
        self.relate('connect', 'right-rail', 'body')
