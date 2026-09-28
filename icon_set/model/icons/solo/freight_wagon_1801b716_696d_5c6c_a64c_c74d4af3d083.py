"""Freight Wagon, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1801b716-696d-5c6c-a64c-c74d4af3d083'
SOURCE_PATH = 'pictographic-primitives/transportation/goods train_1801b716-696d-5c6c-a64c-c74d4af3d083.svg'
AUTHOR = 'gpt-6'

class FreightWagon(Solo48):
    icon_id = 'freight-wagon'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('freight', 'goods train', 'wagon', 'railway', 'cargo', 'container', 'train', 'rail')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_polyline('container',(8,32),(8,8),(16,8),(24,8),(32,8),(40,8),(40,32))
        self.add_polyline('chassis',(4,32),(8,32),(10,32),(16,32),(24,32),(32,32),(38,32),(40,32),(44,32))
        self.relate('connect','container','chassis')
        for x in (16,24,32):
            self.add_line(f'slat-{x}',(x,8),(x,32))
            self.relate('connect',f'slat-{x}','container')
            self.relate('connect',f'slat-{x}','chassis')
        for i,x in enumerate((10,38)):
            self.add_arc(f'wheel-{i}-a',(x,32),(x,40),radius_x=4)
            self.add_arc(f'wheel-{i}-b',(x,40),(x,32),radius_x=4)
            self.add_contour(f'wheel-{i}',f'wheel-{i}-a',f'wheel-{i}-b',closed=True)
            self.relate('connect',f'wheel-{i}','chassis')
