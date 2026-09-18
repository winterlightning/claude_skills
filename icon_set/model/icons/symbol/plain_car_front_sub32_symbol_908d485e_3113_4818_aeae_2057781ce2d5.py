"""Independent 32px profile of plain-car-front.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '908d485e-3113-4818-aeae-2057781ce2d5'
SOURCE_PATH = 'pictographic-primitives/transportation/car 1_908d485e-3113-4818-aeae-2057781ce2d5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('908d485e-3113-4818-aeae-2057781ce2d5', 'pictographic-primitives/transportation/car 1_908d485e-3113-4818-aeae-2057781ce2d5.svg'), ('8156415b-cbe0-4085-a1b2-de1314bf33de', 'pictographic-primitives/transportation/car_8156415b-cbe0-4085-a1b2-de1314bf33de.svg'), ('b90b17e9-30a0-4203-bb54-82de55a03dae', 'pictographic-primitives/transportation/car_b90b17e9-30a0-4203-bb54-82de55a03dae.svg'), ('b2a2cd39-2c37-46cd-9a88-38b142304d18', 'pictographic-primitives/transportation/car_b2a2cd39-2c37-46cd-9a88-38b142304d18.svg'), ('55d4a39f-2307-4a74-8263-cac55d88920b', 'pictographic-primitives/transportation/car 1_55d4a39f-2307-4a74-8263-cac55d88920b.svg'), ('6eaf361a-c125-4908-a062-3aee68b537ed', 'pictographic-primitives/transportation/car 1_6eaf361a-c125-4908-a062-3aee68b537ed.svg'))
PROFILE_SOURCE_KEYS = ('solo/plain-car-front', 'solo/car-front-flared-body', 'solo/car-front-straight-legs')
SOLO_SOURCE_ICON_IDS = ('plain-car-front', 'car-front-flared-body', 'car-front-straight-legs')
REFERENCE_EXPORT_SHA256 = '2a09bafbd6002b1230fac3a4d51338742b66c0b7f47a53dcc48c225c9453e7f4'

class DrawingContainerSymbol(Sub32):
    icon_id = 'plain-car-front-sub32-symbol'
    related_origin_icon_id = 'plain-car-front-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/plain-car-front-sub32'
    counterpart_icon_id = 'plain-car-front-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 11), (5, 11))
        self.add_line('p1-r1-2', (5, 11), (27, 11))
        self.add_line('p1-r1-3', (27, 11), (28, 11))
        self.add_arc('p1-r1-4', (28, 11), (30, 13), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (30, 13), (30, 18))
        self.add_line('p1-r1-6', (30, 18), (30, 24))
        self.add_arc('p1-r1-7', (30, 24), (28, 25), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (28, 25), (27, 25))
        self.add_line('p1-r1-9', (27, 25), (22, 25))
        self.add_line('p1-r1-10', (22, 25), (10, 25))
        self.add_line('p1-r1-11', (10, 25), (5, 25))
        self.add_line('p1-r1-12', (5, 25), (4, 25))
        self.add_arc('p1-r1-13', (4, 25), (2, 24), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-14', (2, 24), (2, 18))
        self.add_line('p1-r1-15', (2, 18), (2, 13))
        self.add_arc('p1-r1-16', (2, 13), (4, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', closed=False)
        self.add_line('p2-r1-1', (5, 11), (10, 2))
        self.add_line('p2-r1-2', (10, 2), (22, 2))
        self.add_line('p2-r1-3', (22, 2), (27, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (5, 25), (5, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (27, 25), (27, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
        self.relate('connect', 'p1-r1-9', 'p4-r1-1')
        self.relate('connect', 'p1-r1-11', 'p3-r1-1')
        self.relate('connect', 'p1-r1-12', 'p3-r1-1')
