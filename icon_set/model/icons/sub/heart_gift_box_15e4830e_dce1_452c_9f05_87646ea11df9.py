"""Gift box with two-loop bow and centered heart on its front."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import rounded_rect

SOURCE_ICON_ID = "15e4830e-dce1-452c-9f05-87646ea11df9"
SOURCE_PATH = "pictographic-primitives/romance/love gift box heart_15e4830e-dce1-452c-9f05-87646ea11df9.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "heart-gift-box"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/symbol"
    aliases = ("love-gift",)
    keywords = ("heart", "gift", "box", "present", "romance")

    def build(self):
        rounded_rect(self, "box", 4, 12, 28, 30, 3)
        self.add_bezier("bow-left", (16, 12), ((9, 12), (7, 10), (7, 7)), ((7, 4), (11, 4), (16, 12)))
        self.add_bezier("bow-right", (16, 12), ((21, 4), (25, 4), (25, 7)), ((25, 10), (23, 12), (16, 12)))
        self.add_contour("bow", "bow-left", "bow-right", closed=True)
        self.relate("connect", "box", "bow")
        self.add_bezier("heart", (16, 26), ((10, 22), (10, 17), (14, 17)), ((15, 17), (16, 19), (16, 19)), ((16, 19), (17, 17), (19, 17)), ((23, 17), (22, 22), (16, 26)))
        self.add_contour("heart-shape", "heart", closed=True)

# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'heart-gift-box': {'status': 'cannot-fix',
                    'date': '2026-09-23',
                    'author': 'gpt-6',
                    'source_icon_id': '15e4830e-dce1-452c-9f05-87646ea11df9',
                    'failures_at_review': ['canvas/keyshape bounds: visible ink (2, 3.15396, 30, '
                                           '32) does not match the SQUARE envelope (0, 0, 32, 32) '
                                           '(deltas [2.0, 3.154, 2.0, 0.0], tolerance 0.0)',
                                           'mic [box]: box and heart-shape are 4 apart on '
                                           'centerlines nearest (16, 30)<->(16, 26); SUB32 '
                                           'requires at least 6 (ink clearance 2) unless the '
                                           'contact is declared with a scoped `connect` '
                                           'relationship',
                                           'holes/pinches: 2 undersized holes; 0 pinches',
                                           'internal-spacing [box / bow]: box-0 and bow-left have '
                                           '-3.9938 units of ink clearance over 7 units; requires '
                                           '2; review required',
                                           'internal-spacing [box / bow]: box-0 and bow-right have '
                                           '-3.9938 units of ink clearance over 7 units; requires '
                                           '2; review required'],
                    'blocker': 'The enclosing box, two bow loops, and inset heart produce '
                               'undersized holes and bow-to-box overlap at 4px stroke',
                    'attempts': ['Original 32px gift: heart-to-box MIC 4 and two undersized holes',
                                 'Wider 32px box with smaller heart: three undersized holes and '
                                 'bow-to-box internal overlap'],
                    'evidence': 'icon_set/work/side-sub-repairs-2026-09-23/strict32-evidence'}}
