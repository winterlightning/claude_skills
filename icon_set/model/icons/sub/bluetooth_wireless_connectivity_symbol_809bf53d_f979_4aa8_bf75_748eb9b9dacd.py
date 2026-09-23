"""Bluetooth rune enclosed by the source's complete circular frame."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import circle

SOURCE_ICON_ID = "809bf53d-f979-4aa8-bf75-748eb9b9dacd"
SOURCE_PATH = "pictographic-primitives/other/circle bluetooth_809bf53d-f979-4aa8-bf75-748eb9b9dacd.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "bluetooth-wireless-connectivity-symbol"
    keyshape = Keyshape.CIRCLE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/symbol"
    aliases = ("bluetooth",)
    keywords = ("wireless", "connectivity", "radio")

    def build(self):
        circle(self, "frame", 16, 16, 14)
        self.add_polyline("bluetooth", (7, 10), (16, 16), (25, 10), (16, 6), (16, 26), (25, 22), (16, 16), (7, 22))

# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'bluetooth-wireless-connectivity-symbol': {'status': 'cannot-fix',
                                            'date': '2026-09-23',
                                            'author': 'gpt-6',
                                            'source_icon_id': '809bf53d-f979-4aa8-bf75-748eb9b9dacd',
                                            'failures_at_review': ['mic [frame]: frame and '
                                                                   'bluetooth are 3.18322 apart on '
                                                                   'centerlines nearest (4.34245, '
                                                                   '8.24777)<->(7, 10); SUB32 '
                                                                   'requires at least 6 (ink '
                                                                   'clearance 2) unless the '
                                                                   'contact is declared with a '
                                                                   'scoped `connect` relationship',
                                                                   'holes/pinches: 4 undersized '
                                                                   'holes; 0 pinches'],
                                            'blocker': "MIC 8 between rune's paired straight runs "
                                                       'and two undersized triangular holes inside '
                                                       'its required circle',
                                            'attempts': ['Original 32px rune: frame-to-rune MIC '
                                                         '3.18 and four undersized holes',
                                                         'Rebalanced 32px rune: parallel gap 6.95 '
                                                         '(<8), frame gap 5.94 (<6), and two '
                                                         'undersized holes'],
                                            'evidence': 'icon_set/work/side-sub-repairs-2026-09-23/strict32-evidence'}}
