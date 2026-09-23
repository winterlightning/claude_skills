"""Rounded chat bubble with lower-left tail and centered clock."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import circle

SOURCE_ICON_ID = "18f6d5a3-0426-4e7b-b6b1-88cb5fcf97ed"
SOURCE_PATH = "pictographic-primitives/symbol/chat time clock_18f6d5a3-0426-4e7b-b6b1-88cb5fcf97ed.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "chat-bubble-with-clock"
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/symbol"
    aliases = ("message-time", "chat-time")
    keywords = ("chat", "message", "clock", "time")

    def build(self):
        self.add_line("top", (7, 2), (25, 2))
        self.add_arc("top-right", (25, 2), (30, 7), radius_x=5)
        self.add_line("right", (30, 7), (30, 21))
        self.add_arc("bottom-right", (30, 21), (25, 26), radius_x=5)
        self.add_line("bottom", (25, 26), (16, 26))
        self.add_line("tail-upper", (16, 26), (9, 30))
        self.add_line("tail-lower", (9, 30), (9, 26))
        self.add_line("bottom-left-run", (9, 26), (7, 26))
        self.add_arc("bottom-left", (7, 26), (2, 21), radius_x=5)
        self.add_line("left", (2, 21), (2, 7))
        self.add_arc("top-left", (2, 7), (7, 2), radius_x=5)
        self.add_contour("bubble", "top", "top-right", "right", "bottom-right", "bottom", "tail-upper", "tail-lower", "bottom-left-run", "bottom-left", "left", "top-left", closed=True)
        circle(self, "clock", 16, 14, 7)
        self.add_polyline("hands", (16, 9), (16, 14), (21, 14))
        self.relate("connect", "clock", "hands")

# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'chat-bubble-with-clock': {'status': 'cannot-fix',
                            'date': '2026-09-23',
                            'author': 'gpt-6',
                            'source_icon_id': '18f6d5a3-0426-4e7b-b6b1-88cb5fcf97ed',
                            'failures_at_review': ['mic [bubble]: bubble and clock are 5 apart on '
                                                   'centerlines nearest (16, 2)<->(16, 7); SUB32 '
                                                   'requires at least 6 (ink clearance 2) unless '
                                                   'the contact is declared with a scoped '
                                                   '`connect` relationship',
                                                   'holes/pinches: 1 undersized holes; 0 pinches'],
                            'blocker': 'The full clock circle plus two hands creates undersized '
                                       'openings when enclosed in a 32px speech bubble',
                            'attempts': ['Original 32px clock: bubble-to-clock MIC 5 (<6) and an '
                                         'undersized hole',
                                         'Smaller connected clock: two undersized holes and '
                                         'internal-spacing 0.33 (<2)'],
                            'evidence': 'icon_set/work/side-sub-repairs-2026-09-23/strict32-evidence'}}
