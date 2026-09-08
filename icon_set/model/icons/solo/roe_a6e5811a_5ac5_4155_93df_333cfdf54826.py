"""Frontal roe deer with mirrored leaf ears and tapered muzzle; source supplies face and neck. Centerline (2,2)-(46,46)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6e5811a-5ac5-4155-93df-333cfdf54826'
SOURCE_PATH = 'pictographic-primitives/animals/roe_a6e5811a-5ac5-4155-93df-333cfdf54826.svg'
AUTHOR = 'gpt-6'


class RoeDeerHead(Solo48):
    icon_id = 'roe-deer-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('roe deer', 'deer', 'head', 'ears', 'face', 'fawn', 'wildlife', 'muzzle')

    def build(self) -> None:
        self.add_arc('face-1', (14, 16), (34, 16), radius_x=12, radius_y=10, sweep=True)
        self.add_arc('face-2', (34, 16), (30, 31), radius_x=20, radius_y=20, sweep=True)
        self.add_line('face-3', (30, 31), (28, 36))
        self.add_arc('face-4', (28, 36), (20, 36), radius_x=5, radius_y=5, sweep=True)
        self.add_line('face-5', (20, 36), (18, 31))
        self.add_arc('face-6', (18, 31), (14, 16), radius_x=20, radius_y=20, sweep=True)
        self.add_contour('face', 'face-1', 'face-2', 'face-3', 'face-4', 'face-5', 'face-6', closed=True)
        self.add_arc('ear-left-1', (14, 16), (2, 2), radius_x=12, radius_y=14, sweep=True)
        self.add_line('ear-left-2', (2, 2), (5, 2))
        self.add_arc('ear-left-3', (5, 2), (16, 10), radius_x=13, radius_y=13, sweep=True)
        self.add_contour('ear-left', 'ear-left-1', 'ear-left-2', 'ear-left-3', closed=False)
        self.add_arc('ear-right-1', (34, 16), (46, 2), radius_x=12, radius_y=14, sweep=False)
        self.add_line('ear-right-2', (46, 2), (43, 2))
        self.add_arc('ear-right-3', (43, 2), (32, 10), radius_x=13, radius_y=13, sweep=False)
        self.add_contour('ear-right', 'ear-right-1', 'ear-right-2', 'ear-right-3', closed=False)
        self.relate("connect", 'face', 'ear-left')
        self.relate("connect", 'face', 'ear-right')
        self.add_line('neck-left-1', (16, 26), (13, 37))
        self.add_arc('neck-left-2', (13, 37), (2, 46), radius_x=11, radius_y=9, sweep=True)
        self.add_contour('neck-left', 'neck-left-1', 'neck-left-2', closed=False)
        self.add_line('neck-right-1', (32, 26), (35, 37))
        self.add_arc('neck-right-2', (35, 37), (46, 46), radius_x=11, radius_y=9, sweep=False)
        self.add_contour('neck-right', 'neck-right-1', 'neck-right-2', closed=False)
        self.relate("connect", 'face', 'neck-left')
        self.relate("connect", 'face', 'neck-right')
