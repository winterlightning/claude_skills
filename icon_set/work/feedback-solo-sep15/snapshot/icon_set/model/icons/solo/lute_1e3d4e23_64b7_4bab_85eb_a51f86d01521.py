"""Diagonal pear body and long narrow neck with an open fingerboard; sound hole centered within broad bowl. Omit bridge and frets. Extremes (6,6)-(42,42). Lucide guitar diagonal layout, smooth coherent contour."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e3d4e23-64b7-4bab-85eb-a51f86d01521'
SOURCE_PATH = 'pictographic-primitives/music/lute_1e3d4e23-64b7-4bab-85eb-a51f86d01521.svg'
AUTHOR = 'gpt-6'

class Lute(Solo48):
    icon_id = 'lute'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/music"
    aliases = ()
    keywords = ('lute', 'string', 'instrument', 'renaissance', 'mandolin', 'music', 'plucked')

    def build(self):
        self.add_bezier('bowl',(24,18), ((17,18),(6,21),(6,30)), ((6,37),(11,42),(18,42)), ((27,42),(30,31),(30,24)))
        self.add_line('shoulder',(30,24),(24,18))
        self.add_contour('body','bowl','shoulder',closed=True)
        self.add_polyline('neck',(24,18),(36,6),(42,12),(30,24))
        self.relate('connect','neck','body')
        cx, cy, radius = 18, 30, 2
        points = ((cx-radius,cy),(cx,cy-radius),(cx+radius,cy),(cx,cy+radius))
        for n in range(4):
            self.add_arc(f'sound-hole-{n}',points[n],points[(n+1)%4],radius_x=radius)
        self.add_contour('sound-hole', *[f'sound-hole-{n}' for n in range(4)], closed=True)
