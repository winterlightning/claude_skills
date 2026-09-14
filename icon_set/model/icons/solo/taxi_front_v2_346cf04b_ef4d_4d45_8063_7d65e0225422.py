"""A front-facing taxi with a roof sign, windscreen and paired headlights. VRECT_L ink (6,6)-(42,42) provides room for the sign. Lucide car-front informed symmetry; tyres reduced to short stubs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '346cf04b-ef4d-4d45-8063-7d65e0225422'
SOURCE_PATH = 'pictographic-primitives/transportation/car 1_346cf04b-ef4d-4d45-8063-7d65e0225422.svg'
SOURCE_REFERENCES = (('346cf04b-ef4d-4d45-8063-7d65e0225422', 'pictographic-primitives/transportation/car 1_346cf04b-ef4d-4d45-8063-7d65e0225422.svg'),)
AUTHOR = 'gpt-6'

class TaxiFrontVariant2(Solo48):
    icon_id = 'taxi-front-v2'
    variant_of = 'taxi-front'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('taxi', 'cab', 'car', 'front', 'roof sign', 'vehicle', 'ride', 'transport')

    def build(self) -> None:
        self.add_line('body-top-0', (10, 20), (12, 20))
        self.add_line('body-top-1', (12, 20), (36, 20))
        self.add_line('body-top-2', (36, 20), (38, 20))
        self.add_arc('body-top-corner', (38, 20), (40, 22), radius_x=2)
        self.add_line('body-right-0', (40, 22), (40, 36))
        self.add_arc('body-right-corner', (40, 36), (38, 38), radius_x=2)
        self.add_line('body-bottom-0', (38, 38), (36, 38))
        self.add_line('body-bottom-1', (36, 38), (12, 38))
        self.add_line('body-bottom-2', (12, 38), (10, 38))
        self.add_arc('body-bottom-corner', (10, 38), (8, 36), radius_x=2)
        self.add_line('body-left-0', (8, 36), (8, 22))
        self.add_arc('body-left-corner', (8, 22), (10, 20), radius_x=2)
        self.add_contour('body', 'body-top-0', 'body-top-1', 'body-top-2', 'body-top-corner', 'body-right-0', 'body-right-corner', 'body-bottom-0', 'body-bottom-1', 'body-bottom-2', 'body-bottom-corner', 'body-left-0', 'body-left-corner', closed=True)
        self.add_polyline('cabin', (12, 20), (16, 12), (18, 12), (30, 12), (32, 12), (36, 20))
        self.add_polyline('roof-sign', (18, 12), (18, 4), (30, 4), (30, 12))
        self.relate('connect', 'roof-sign', 'cabin')
        self.relate('connect', 'cabin', 'body')
        for side, x in [('left', 12), ('right', 36)]:
            self.add_line(side + '-wheel', (x, 38), (x, 44))
            self.relate('connect', side + '-wheel', 'body')
        self.add_line('left-light', (17, 29), (18, 29))
        self.add_line('right-light', (30, 29), (31, 29))
