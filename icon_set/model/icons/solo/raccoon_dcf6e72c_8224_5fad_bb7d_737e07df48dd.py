"""Curled silhouette, muzzle and two stripes in a broad tail. No useful local raccoon match; circular construction re-authored from the supplied image. Four stripes reduced to two."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcf6e72c-8224-5fad-bb7d-737e07df48dd'
SOURCE_PATH = 'pictographic-primitives/animals/raccoon_dcf6e72c-8224-5fad-bb7d-737e07df48dd.svg'
AUTHOR = 'gpt-6'


class CurledRaccoon(Solo48):
    icon_id = 'curled-raccoon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('raccoon', 'curled', 'tail', 'stripes', 'mask', 'animal', 'wildlife', 'nocturnal')

    def build(self) -> None:
        self.add_line('outline-1', (2, 13), (9, 12))
        self.add_arc('outline-2', (9, 12), (24, 2), radius_x=20, radius_y=16, sweep=True)
        self.add_arc('outline-3', (24, 2), (46, 24), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('outline-4', (46, 24), (24, 46), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('outline-5', (24, 46), (12, 42), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('outline-6', (12, 42), (2, 27), radius_x=20, radius_y=18, sweep=True)
        self.add_line('outline-7', (2, 27), (8, 27))
        self.add_line('outline-8', (8, 27), (16, 30))
        self.add_line('outline-9', (16, 30), (24, 36))
        self.add_arc('outline-10', (24, 36), (36, 24), radius_x=12, radius_y=12, sweep=False)
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', 'outline-10', closed=False)
        self.add_line('face-1', (2, 13), (4, 16))
        self.add_arc('face-2', (4, 16), (11, 21), radius_x=8, radius_y=5, sweep=False)
        self.add_line('face-3', (11, 21), (20, 21))
        self.add_arc('face-4', (20, 21), (26, 27), radius_x=6, radius_y=6, sweep=True)
        self.add_line('face-5', (26, 27), (26, 28))
        self.add_contour('face', 'face-1', 'face-2', 'face-3', 'face-4', 'face-5', closed=False)
        self.add_line('ear-1', (24, 2), (24, 10))
        self.add_line('ear-2', (24, 10), (31, 9))
        self.add_contour('ear', 'ear-1', 'ear-2', closed=False)
        self.add_line('stripe-one-1', (12, 42), (16, 30))
        self.add_contour('stripe-one', 'stripe-one-1', closed=False)
        self.add_line('stripe-two-1', (24, 46), (24, 36))
        self.add_contour('stripe-two', 'stripe-two-1', closed=False)
        self.add_dot('eye', (17, 12))
        self.relate("connect", 'outline', 'face')
        self.relate("connect", 'outline', 'ear')
        self.relate("connect", 'outline', 'stripe-one')
        self.relate("connect", 'outline', 'stripe-two')
