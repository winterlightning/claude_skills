"""Ram profile with spiral horn, long neck and pendant muzzle. Extrema (2,2)-(46,46). Lucide snail informs nested arcs; source asymmetry retained. Tiny chin crease omitted."""
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
    category = 'animals/wildlife'
    aliases = ()
    keywords = ('ram', 'sheep', 'horn', 'spiral', 'head', 'profile', 'aries', 'animal')

    def build(self) -> None:
        # Ram profile with spiral horn, long neck and pendant muzzle. Extrema (2,2)-(46,46). Lucide snail informs nested arcs; source asymmetry retained. Tiny chin crease omitted.
        self.add_arc('horn-top', (46, 18), (26, 2), radius_x=20, radius_y=16, sweep=False)
        self.add_arc('horn-left', (26, 2), (6, 18), radius_x=20, radius_y=16, sweep=False)
        self.add_arc('horn-bottom', (6, 18), (18, 30), radius_x=12, radius_y=12, sweep=False)
        self.add_arc('horn-in', (18, 30), (30, 18), radius_x=12, radius_y=12, sweep=False)
        self.add_arc('curl-top', (30, 18), (22, 10), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('curl-end', (22, 10), (14, 18), radius_x=8, radius_y=8, sweep=False)
        self.add_contour('horn', 'horn-top', 'horn-left', 'horn-bottom', 'horn-in', 'curl-top', 'curl-end')
        self.add_line('muzzle', (46, 18), (46, 36))
        self.add_arc('chin', (46, 36), (36, 46), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('jaw', (36, 46), (26, 32), radius_x=10, radius_y=14, sweep=True)
        self.add_contour('face', 'muzzle', 'chin', 'jaw')
        self.relate("connect", 'horn', 'face')
        self.add_arc('neck', (18, 30), (2, 46), radius_x=40, radius_y=40, sweep=False)
        self.relate("connect", 'horn', 'neck')
        self.add_arc('cheek', (30, 18), (46, 18), radius_x=8, radius_y=5, sweep=False)
        self.relate("connect", 'cheek', 'horn')
        self.relate("connect", 'cheek', 'face')
