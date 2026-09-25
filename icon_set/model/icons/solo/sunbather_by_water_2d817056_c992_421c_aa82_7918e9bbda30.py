"""Sunbather by Water. Reclining figure with bent knees beside water; retain the sun disk and omit its rays to keep clear separation.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sun: circular solar disk; person-standing: sparse limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d817056-c992-421c-aa82-7918e9bbda30'
SOURCE_PATH = 'pictographic-primitives/recreation/sunbathe activitiies_2d817056-c992-421c-aa82-7918e9bbda30.svg'
AUTHOR = 'gpt-6'


class SunbatherByWater(Solo48):
    icon_id = 'sunbather-by-water'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ('sunbather', 'by', 'water')

    def build(self) -> None:
        self.add_arc('head-top', (9, 14), (15, 14), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (15, 14), (9, 14), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('person-1', (6, 30), (14, 26))
        self.add_line('person-2', (14, 26), (23, 31))
        self.add_line('person-3', (23, 31), (31, 25))
        self.add_line('person-4', (31, 25), (42, 31))
        self.add_contour('person', 'person-1', 'person-2', 'person-3', 'person-4', closed=False)
        self.add_line('support-arm', (14, 26), (13, 31))
        self.relate("connect", 'person', 'support-arm')
        self.add_arc('sun-top', (32, 10), (40, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('sun-bottom', (40, 10), (32, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
        self.add_arc('wave-left', (6, 40), (24, 40), radius_x=9, radius_y=2, sweep=False)
        self.add_arc('wave-right', (24, 40), (42, 40), radius_x=9, radius_y=2, sweep=False)
        self.add_contour('water', 'wave-left', 'wave-right', closed=False)
