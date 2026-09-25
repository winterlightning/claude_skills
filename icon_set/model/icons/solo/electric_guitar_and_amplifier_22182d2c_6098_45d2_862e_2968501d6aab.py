"""Flying V guitar at left, amplifier cabinet at right; preserve characteristic pointed body and speaker. Omit strings, grille and controls. Extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22182d2c-6098-45d2-862e-2968501d6aab'
SOURCE_PATH = 'pictographic-primitives/music/modern music bass guitar_22182d2c-6098-45d2-862e-2968501d6aab.svg'
AUTHOR = 'gpt-6'

class ElectricGuitarAndAmplifier(Solo48):
    icon_id = 'electric-guitar-and-amplifier'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "music"
    aliases = ()
    keywords = ('electric-guitar', 'amplifier', 'rock', 'bass', 'band', 'speaker', 'instrument', 'music')

    def build(self):
        self.add_polyline('guitar',(6,42),(12,24),(24,42),(15,36),closed=True)
        self.add_line('neck',(12,6),(12,24))
        self.add_line('head',(12,6),(20,6))
        self.relate('connect','neck','guitar')
        self.relate('connect','neck','head')
        self.add_polyline('amplifier',(24,16),(42,16),(42,42),(34,42))
        
        cx, cy, radius = 30, 28, 3
        points = ((cx-radius,cy),(cx,cy-radius),(cx+radius,cy),(cx,cy+radius))
        for n in range(4):
            self.add_arc(f'speaker-{n}',points[n],points[(n+1)%4],radius_x=radius)
        self.add_contour('speaker', *[f'speaker-{n}' for n in range(4)], closed=True)
