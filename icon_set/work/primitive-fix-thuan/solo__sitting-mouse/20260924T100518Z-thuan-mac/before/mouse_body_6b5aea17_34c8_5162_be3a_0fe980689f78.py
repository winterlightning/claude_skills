"""Upright mouse with two rounded ears and haunch; eye and paw scoring omitted. Lucide rat informs ears."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b5aea17-34c8-5162-be3a-0fe980689f78'
SOURCE_PATH = 'pictographic-primitives/animals/mouse body_6b5aea17-34c8-5162-be3a-0fe980689f78.svg'
AUTHOR = 'gpt-6'


class SittingMouse(Solo48):
    icon_id = 'sitting-mouse'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('sitting', 'mouse')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_arc('ear-left-base',(18, 16),(10, 10),radius_x=8,radius_y=6,large_arc=False,sweep=True)
        self.add_bezier('ear-left',(10, 10),*(((10.0, 6.6862915), (13.13400675, 4.0), (17.0, 4)), ((20.86599325, 4), (24.0, 6.6862915), (24, 10))))
        self.add_bezier('ear-right',(24, 10),*(((24.0, 6.6862915), (27.13400675, 4.0), (31.0, 4)), ((34.86599325, 4), (38.0, 6.6862915), (38, 10))))
        self.add_arc('ear-right-base',(38, 10),(34, 16),radius_x=6,radius_y=6,large_arc=False,sweep=True)
        self.add_line('nose',(34, 16),(40, 22))
        self.add_arc('muzzle',(40, 22),(32, 28),radius_x=8,radius_y=6,large_arc=False,sweep=True)
        self.add_line('chest',(32, 28),(32, 34))
        self.add_bezier('belly',(32, 34),*(((30.22736717, 40.30129534), (25.33504611, 44), (20, 44)),))
        self.add_bezier('rump',(20, 44),*(((14.66495389, 44), (9.77263283, 40.30129534), (8, 34)),))
        self.add_arc('back',(8, 34),(18, 24),radius_x=10,radius_y=10,large_arc=False,sweep=True)
        self.add_line('neck',(18, 24),(18, 16))
        self.add_bezier('tail',(32, 34),*(((36.418278, 34.0), (40, 38.4771525), (40, 44)),))
        self.add_contour('mouse',*('ear-left-base', 'ear-left', 'ear-right', 'ear-right-base', 'nose', 'muzzle', 'chest', 'belly', 'rump', 'back', 'neck'),closed=True)
        self.relate('connect',*('mouse', 'tail'))
