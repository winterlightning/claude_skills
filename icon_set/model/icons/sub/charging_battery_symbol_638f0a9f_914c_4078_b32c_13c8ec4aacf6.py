"""Rounded battery case, separate right terminal, and central charging bolt."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import rounded_rect

SOURCE_ICON_ID = "638f0a9f-914c-4078-b32c-13c8ec4aacf6"
SOURCE_PATH = "pictographic-primitives/other/battery 1_638f0a9f-914c-4078-b32c-13c8ec4aacf6.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "charging-battery-symbol"
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/state"
    aliases = ("battery-charging",)
    keywords = ("battery", "charge", "power", "bolt")

    def build(self):
        rounded_rect(self, "battery", 2, 4, 26, 28, 4)
        self.add_line("terminal", (30, 12), (30, 20))
        self.add_polyline("bolt", (18, 9), (11, 18), (17, 17), (13, 24))

# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'charging-battery-symbol': {'status': 'cannot-fix',
                             'date': '2026-09-23',
                             'author': 'gpt-6',
                             'source_icon_id': '638f0a9f-914c-4078-b32c-13c8ec4aacf6',
                             'failures_at_review': ['mic [terminal]: parallel straight edges '
                                                    'terminal and battery-2 are 4 apart on '
                                                    'centerlines (ink gap 0); requires at least 8 '
                                                    'centerline / 4 ink (midpoint-normal)',
                                                    'mic [battery]: battery and terminal are 4 '
                                                    'apart on centerlines nearest (26, 12)<->(30, '
                                                    '12); SUB32 requires at least 6 (ink clearance '
                                                    '2) unless the contact is declared with a '
                                                    'scoped `connect` relationship',
                                                    'mic [battery]: battery and bolt are 4 apart '
                                                    'on centerlines nearest (13, 28)<->(13, 24); '
                                                    'SUB32 requires at least 6 (ink clearance 2) '
                                                    'unless the contact is declared with a scoped '
                                                    '`connect` relationship',
                                                    'internal-spacing [bolt]: bolt-1 and bolt-3 '
                                                    'have 0.2085 units of ink clearance over '
                                                    '3.4204 units; requires 2; review required'],
                             'blocker': 'Separate terminal requires 8px case gap, leaving too '
                                        'little room for a 4px bolt with 2px internal ink '
                                        'clearance',
                             'attempts': ['Original 32px case and bolt: terminal gap 4 (<8) and '
                                          'bolt-to-case MIC 4 (<6)',
                                          'Narrowed case and diagonal Z bolt: self spacing 1.06 '
                                          '(<2) or exact 6px curve clearance remains review'],
                             'evidence': 'icon_set/work/side-sub-repairs-2026-09-23/strict32-evidence'}}
