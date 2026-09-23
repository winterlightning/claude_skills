"""Tall rounded card containing a left-facing crescent moon."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import rounded_rect

SOURCE_ICON_ID = "23e48a73-6f3a-4649-8e2c-1ae7c754ab02"
SOURCE_PATH = "pictographic-primitives/other/card moon_23e48a73-6f3a-4649-8e2c-1ae7c754ab02.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "crescent-moon-card"
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/symbol"
    aliases = ("moon-card",)
    keywords = ("crescent", "moon", "card", "night")

    def build(self):
        rounded_rect(self, "card", 4, 2, 28, 30, 4)
        self.add_bezier("moon", (18, 9), ((9, 9), (9, 23), (18, 23)), ((13, 19), (13, 13), (18, 9)))
        self.add_contour("crescent", "moon", closed=True)

# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'crescent-moon-card': {'status': 'fixed',
                        'date': '2026-09-23',
                        'author': 'gpt-6',
                        'source_icon_id': '23e48a73-6f3a-4649-8e2c-1ae7c754ab02',
                        'failures_at_review': ['holes/pinches: 1 undersized holes; 1 pinches'],
                        'variant': 'crescent-moon-card-v2',
                        'evidence': 'icon_set/work/side-sub-repairs-2026-09-23/strict32-evidence'}}
