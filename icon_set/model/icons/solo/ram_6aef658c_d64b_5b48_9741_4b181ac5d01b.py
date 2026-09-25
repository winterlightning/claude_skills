"""Ram profile with spiral horn, long neck and pendant muzzle. Extrema (6,6)-(42,42). Lucide snail informs nested arcs; source asymmetry retained. Tiny chin crease omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6aef658c-d64b-5b48-9741-4b181ac5d01b'
SOURCE_PATH = 'pictographic-primitives/animals/ram_6aef658c-d64b-5b48-9741-4b181ac5d01b.svg'
AUTHOR = 'gpt-6'


class RamHeadProfile(Solo48):
    icon_id = 'ram-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    aliases = ()
    keywords = ('ram', 'sheep', 'horn', 'spiral', 'head', 'profile', 'aries', 'animal')

    def build(self) -> None:
        # Ram profile with spiral horn, long neck and pendant muzzle. Extrema (6,6)-(42,42). Lucide snail informs nested arcs; source asymmetry retained. Tiny chin crease omitted.
        self.add_arc('horn-top', (42, 18), (26, 6), radius_x=20, radius_y=16, sweep=False)
        self.add_bezier('horn-left', (26, 6), *(((16.6446712, 6), (8.33532079, 10.74880085), (6, 18)),))
        self.add_arc('horn-bottom', (6, 18), (18, 30), radius_x=12, radius_y=12, sweep=False)
        self.add_arc('horn-in', (18, 30), (30, 18), radius_x=12, radius_y=12, sweep=False)
        self.add_arc('curl-top',(30,18),(22,20),radius_x=5,sweep=False)
        self.add_contour('horn', 'horn-top', 'horn-left', 'horn-bottom', 'horn-in', 'curl-top')
        self.add_line('muzzle', (42, 18), (42, 36))
        self.add_arc('chin', (42, 36), (36, 42), radius_x=10, radius_y=10, sweep=True)
        self.add_bezier('jaw', (36, 42), *(((31.42433452, 42), (27.30452448, 38.14581316), (26, 32)),))
        self.add_contour('face', 'muzzle', 'chin', 'jaw')
        self.relate("connect", 'horn', 'face')
        self.add_arc('neck', (18, 30), (6, 42), radius_x=40, radius_y=40, sweep=False)
        self.relate("connect", 'horn', 'neck')
        self.add_arc('cheek', (30, 18), (42, 18), radius_x=8, radius_y=5, sweep=False)
        self.relate("connect", 'cheek', 'horn')
        self.relate("connect", 'cheek', 'face')
