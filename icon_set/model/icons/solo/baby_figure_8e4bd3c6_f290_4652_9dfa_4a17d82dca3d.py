"""A standing infant with a detached round head, angled arms, diaper and outward bent legs; symmetric paired limbs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e4bd3c6-f290-4652-9dfa-4a17d82dca3d'
SOURCE_PATH = 'pictographic-primitives/babies/family baby_8e4bd3c6-f290-4652-9dfa-4a17d82dca3d.svg'
AUTHOR = 'gpt-6'


class BabyFigure(Solo48):
    icon_id = 'baby-figure'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/babies"
    aliases = ()
    keywords = ('baby', 'figure', 'infant', 'nursery')

    def build(self) -> None:
        # Centerline extremes: (5,2)-(43,46).
        self.add_arc('head-top', (18, 8), (30, 8), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (30, 8), (18, 8), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('shoulders', (17, 22), (31, 22))
        self.add_polyline('arm-left', (17, 22), (5, 33), (10, 37), (16, 31))
        self.add_polyline('arm-right', (31, 22), (43, 33), (38, 37), (32, 31))
        self.add_line('waist-left', (16, 31), (16, 37))
        self.add_line('waist-right', (32, 31), (32, 37))
        self.add_line('diaper-band', (16, 37), (32, 37))
        self.add_arc('diaper', (16, 37), (32, 37), radius_x=8, radius_y=7, sweep=False, large_arc=False)
        self.add_polyline('leg-left', (16, 37), (11, 42), (16, 46))
        self.add_polyline('leg-right', (32, 37), (37, 42), (32, 46))
        self.relate("connect", 'shoulders', 'arm-left')
        self.relate("connect", 'shoulders', 'arm-right')
        self.relate("connect", 'arm-left', 'waist-left')
        self.relate("connect", 'arm-right', 'waist-right')
        self.relate("connect", 'waist-left', 'diaper-band')
        self.relate("connect", 'waist-right', 'diaper-band')
        self.relate("connect", 'diaper-band', 'diaper')
        self.relate("connect", 'waist-left', 'diaper')
        self.relate("connect", 'waist-right', 'diaper')
        self.relate("connect", 'leg-left', 'waist-left')
        self.relate("connect", 'leg-left', 'diaper')
        self.relate("connect", 'leg-left', 'diaper-band')
        self.relate("connect", 'leg-right', 'waist-right')
        self.relate("connect", 'leg-right', 'diaper')
        self.relate("connect", 'leg-right', 'diaper-band')
