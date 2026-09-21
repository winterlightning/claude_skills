"""Digital Time 9:40. Stacks 9: over 40, retaining every digit and the separator.

SQUARE visible extremes (4, 4, 44, 44), centerlines (6, 6, 42, 42).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '893943bc-8343-4560-8eb4-9293b26dcad3'
SOURCE_PATH = 'pictographic-primitives/symbol/9-40_893943bc-8343-4560-8eb4-9293b26dcad3.svg'
AUTHOR = 'gpt-6'


class Time940(Solo48):
    icon_id = 'time-9-40'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('time', 'clock', '9:40', 'digital', 'hour', 'minutes', 'schedule', 'text')

    def build(self) -> None:
        self.add_arc('nine-head-right', (18, 6), (18, 14), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('nine-head-left', (18, 14), (18, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('nine-head', 'nine-head-right', 'nine-head-left', closed=True)
        self.add_line('nine-stem', (22, 10), (22, 17))
        self.add_arc('nine-tail', (22, 17), (14, 17), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('nine-descender', 'nine-stem', 'nine-tail')
        self.relate("connect", 'nine-head', 'nine-descender')
        self.add_dot('colon-top', (32, 8))
        self.add_dot('colon-bottom', (32, 17))
        self.add_polyline('four-arm', (16, 30), (6, 38), (18, 38))
        self.add_polyline('four-stem', (18, 30), (18, 38), (18, 42))
        self.relate("connect", 'four-arm', 'four-stem')
        self.add_arc('zero-right', (35, 30), (35, 42), radius_x=7, radius_y=6, sweep=True)
        self.add_arc('zero-left', (35, 42), (35, 30), radius_x=7, radius_y=6, sweep=True)
        self.add_contour('zero', 'zero-right', 'zero-left', closed=True)
