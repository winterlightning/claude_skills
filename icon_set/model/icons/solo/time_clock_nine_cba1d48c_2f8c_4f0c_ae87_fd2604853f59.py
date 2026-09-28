"""Time clock nine (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cba1d48c-2f8c-4f0c-ae87-fd2604853f59'
SOURCE_PATH = 'pictographic-primitives/interface-essential/time clock nine_cba1d48c-2f8c-4f0c-ae87-fd2604853f59.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class TimeClockNine(Solo48):
    icon_id = 'time-clock-nine'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('time', 'clock', 'nine', 'interface-essential')

    def build(self):
        self.add_line('e0', (38, 23), (42, 23))
        self.add_line('e1', (24, 38), (24, 42))
        self.add_line('e2', (14, 35), (12, 37))
        self.add_line('e3', (24, 6), (24, 23))
        self.add_line('e4', (24, 23), (6, 23))
        self.add_bezier('e5', (42, 23), ((42, 22.738), (41.992, 22.658), (41.992, 22.388)), ((41.992, 21.275), (41.73, 20.097), (41.419, 19.034)), ((39.775, 13.355), (35.193, 8.774), (29.637, 6.835)), ((28.361, 6.385), (26.921, 6.008), (25.563, 6.008)), ((25.252, 6.008), (24.941, 6), (24.63, 6)), ((24.417, 6), (24.213, 6), (24, 6)))
        self.add_bezier('e6', (6, 23), ((6, 23.466), (6.008, 24.115), (6.008, 24.581)), ((6.008, 29.04), (8.692, 33.99), (11.727, 37.091)), ((14.509, 39.93), (19.025, 41.984), (23.051, 41.984)), ((23.141, 41.992), (23.239, 41.992), (23.329, 42)), ((23.55, 42), (23.779, 42), (24, 42)))
        self.add_bezier('e7', (42, 23), ((42, 23.442), (41.992, 24.065), (41.992, 24.507)), ((41.992, 33.237), (33.9, 41.992), (25.015, 41.992)), ((24.892, 41.992), (24.769, 42), (24.646, 42)), ((24.434, 42), (24.213, 42), (24, 42)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e5', 'e3', 'e4', 'e6')
        self.add_contour('c4', 'e7')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
