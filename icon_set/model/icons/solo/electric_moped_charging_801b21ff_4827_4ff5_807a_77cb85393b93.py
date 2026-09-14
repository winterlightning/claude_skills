"""Electric Moped Charging, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '801b21ff-4827-4ff5-807a-77cb85393b93'
SOURCE_PATH = 'pictographic-primitives/transportation/electric scooter charging_801b21ff-4827-4ff5-807a-77cb85393b93.svg'
AUTHOR = 'gpt-6'

class ElectricMopedCharging(Solo48):
    icon_id = 'electric-moped-charging'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('electric scooter', 'moped', 'charging', 'plug', 'e-scooter', 'electric', 'vespa', 'vehicle')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        # Matched circular wheels, step-through body and physically attached plug.
        for i,x in enumerate((8,40)):
            self.add_arc(f'wheel-{i}-a',(x,32),(x,40),radius_x=4)
            self.add_arc(f'wheel-{i}-b',(x,40),(x,32),radius_x=4)
            self.add_contour(f'wheel-{i}',f'wheel-{i}-a',f'wheel-{i}-b',closed=True)
        self.add_arc('rear-left',(8,32),(16,23),radius_x=8,radius_y=9)
        self.add_arc('rear-right',(16,23),(24,32),radius_x=8,radius_y=9)
        self.add_contour('rear-body','rear-left','rear-right')
        self.add_polyline('floor',(8,32),(24,32),(28,32),(34,24),(40,32))
        self.add_polyline('steering',(30,16),(34,16),(34,24))
        self.relate('connect','floor','rear-body')
        self.relate('connect','steering','floor')
        for w in ('wheel-0','wheel-1'): self.relate('connect','floor',w)
        self.relate('connect','rear-body','wheel-0')
        self.add_line('lead',(16,23),(16,18))
        self.relate('connect','lead','rear-body')
        self.add_polyline('plug',(12,8),(12,14),(16,18),(20,14),(20,8))
        self.relate('connect','lead','plug')
