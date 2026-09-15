"""A capital G drawn as a thick outline with a plus sign attached to the end of its crossbar at the right.

Plan: Elliptical capital G with detached plus sharing its crossbar baseline.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful exact brand match; elliptical G and shared plus junction.
Simplification: Double outline reduces to single letter stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21a87bc5-199b-493f-991b-725b026db17b'
SOURCE_PATH = 'pictographic-primitives/logos/google plus logo_21a87bc5-199b-493f-991b-725b026db17b.svg'
AUTHOR = 'gpt-6'


class GooglePlusLogo(Solo48):
    icon_id = 'google-plus-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-plus', 'google', 'social', 'letter-g', 'plus', 'logo', 'brand')

    def build(self):
        self.add_bezier('top',(23,12),((21,9),(19,8),(16,8)))
        self.add_arc('left',(16,8),(4,24),radius_x=12,radius_y=16,sweep=False)
        self.add_arc('bottom',(4,24),(28,24),radius_x=12,radius_y=16,sweep=False)
        self.add_line('bar',(28,24),(17,24))
        self.add_contour('g','top','left','bottom','bar')
        self.add_polyline('plus-h',(36,24),(40,24),(44,24))
        self.add_polyline('plus-v',(40,18),(40,24),(40,30))
        self.relate('connect','plus-h','plus-v')
