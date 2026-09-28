"""Thermometer over Wave, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7344408f-27b8-52a3-bfa8-c99c266f527d'
SOURCE_PATH = 'pictographic-primitives/transportation/engine temperature warning_7344408f-27b8-52a3-bfa8-c99c266f527d.svg'
AUTHOR = 'gpt-6'

class ThermometerOverWave(Solo48):
    icon_id = 'thermometer-over-wave'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('thermometer', 'engine temperature', 'coolant', 'warning', 'dashboard', 'car', 'overheating', 'gauge')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_arc('bulb-a',(24,15),(24,25),radius_x=5)
        self.add_arc('bulb-b',(24,25),(24,15),radius_x=5)
        self.add_contour('bulb','bulb-a','bulb-b',closed=True)
        self.add_polyline('stem',(24,15),(24,8))
        self.relate('connect','stem','bulb')
        self.add_line('tick',(24,8),(32,8))
        self.relate('connect','tick','stem')
        for i in range(4):
            x=4+i*10
            self.add_arc(f'wave-{i}',(x,37),(x+10,37),radius_x=5,radius_y=3,sweep=bool(i%2))
        self.add_contour('wave',*[f'wave-{i}' for i in range(4)])
