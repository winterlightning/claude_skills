"""Sunbather on Lounger. Figure reclines on a sloping lounger under a sun; omit rays and minor chair braces.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sun: circular disk; person-standing: a reduced reclining figure. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '839f7645-d246-443b-948f-0ee346ad3a52'
SOURCE_PATH = 'pictographic-primitives/recreation/sunbathe_839f7645-d246-443b-948f-0ee346ad3a52.svg'
AUTHOR = 'gpt-6'


class SunbatherOnLounger(Solo48):
    icon_id = 'sunbather-on-lounger'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('sunbather', 'on', 'lounger')

    def build(self) -> None:
        self.add_arc('head-top', (13, 14), (19, 14), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (19, 14), (13, 14), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('person-1', (16, 26), (24, 29))
        self.add_line('person-2', (24, 29), (31, 25))
        self.add_line('person-3', (31, 25), (38, 38))
        self.add_contour('person', 'person-1', 'person-2', 'person-3', closed=False)
        self.add_arc('sun-top', (32, 10), (40, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('sun-bottom', (40, 10), (32, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
        self.add_line('lounger-1', (6, 26), (17, 38))
        self.add_line('lounger-2', (17, 38), (37, 38))
        self.add_line('lounger-3', (37, 38), (38, 38))
        self.add_line('lounger-4', (38, 38), (42, 38))
        self.add_contour('lounger', 'lounger-1', 'lounger-2', 'lounger-3', 'lounger-4', closed=False)
        self.relate("connect", 'person', 'lounger')
        self.add_line('leg-left', (17, 38), (15, 42))
        self.add_line('leg-right', (37, 38), (39, 42))
        self.relate("connect", 'leg-left', 'lounger')
        self.relate("connect", 'leg-right', 'lounger')
