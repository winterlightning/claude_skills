"""Flat Tyre, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e64d5532-b5af-40bd-abb3-502f9c2c172a'
SOURCE_PATH = 'pictographic-primitives/transportation/flat tire_e64d5532-b5af-40bd-abb3-502f9c2c172a.svg'
AUTHOR = 'gpt-6'

class FlatTyre(Solo48):
    icon_id = 'flat-tyre'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('flat tyre', 'flat tire', 'tyre', 'wheel', 'puncture', 'car', 'warning', 'rim')

    def build(self) -> None:
        # Current contract centerline extremes: (6,6)-(42,42).
        self.add_arc('tyre-crown',(6,24),(42,24),radius_x=18)
        points = ((42,24),(42,30),(38,36),(40,42),(8,42),(10,36),(6,30),(6,24))
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'flat-base-{i}',a,b)
        self.add_contour('tyre','tyre-crown',*[f'flat-base-{i}' for i in range(1, 8)],closed=True)
        self.add_arc('rim-a',(24,16),(24,32),radius_x=8)
        self.add_arc('rim-b',(24,32),(24,16),radius_x=8)
        self.add_contour('rim','rim-a','rim-b',closed=True)
