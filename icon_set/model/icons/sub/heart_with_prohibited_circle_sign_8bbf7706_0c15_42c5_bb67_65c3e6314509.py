"""Heart inside a prohibition circle with the source's two exposed slash ends."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import circle

SOURCE_ICON_ID = "8bbf7706-0c15-42c5-bb67-65c3e6314509"
SOURCE_PATH = "pictographic-primitives/other/slash heart_8bbf7706-0c15-42c5-bb67-65c3e6314509.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "heart-with-prohibited-circle-sign"
    keyshape = Keyshape.CIRCLE
    semantic_role = "SUB"
    semantic_kind = "state"
    category = "primitives/state"
    aliases = ("no-heart", "heart-prohibited")
    keywords = ("heart", "prohibited", "ban", "slash", "no")

    def build(self):
        circle(self, "frame", 16, 16, 14)
        self.add_line("slash-upper", (4, 9), (8, 11))
        self.add_line("slash-lower", (24, 21), (28, 23))
        self.add_bezier("heart", (16, 24), ((9, 18), (8, 15), (8, 12)), ((8, 8), (13, 7), (16, 11)), ((19, 7), (24, 8), (24, 12)), ((24, 16), (21, 19), (16, 24)))
        self.add_contour("heart-shape", "heart", closed=True)

# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'heart-with-prohibited-circle-sign': {'status': 'fixed',
                                       'date': '2026-09-23',
                                       'author': 'gpt-6',
                                       'source_icon_id': '8bbf7706-0c15-42c5-bb67-65c3e6314509',
                                       'failures_at_review': ['mic [frame]: frame and slash-upper '
                                                              'are 0.107522 apart on centerlines '
                                                              'nearest (3.90744, 8.94529)<->(4, '
                                                              '9); SUB32 requires at least 6 (ink '
                                                              'clearance 2) unless the contact is '
                                                              'declared with a scoped `connect` '
                                                              'relationship',
                                                              'mic [frame]: frame and slash-lower '
                                                              'are 0.107522 apart on centerlines '
                                                              'nearest (28.0926, 23.0547)<->(28, '
                                                              '23); SUB32 requires at least 6 (ink '
                                                              'clearance 2) unless the contact is '
                                                              'declared with a scoped `connect` '
                                                              'relationship',
                                                              'mic [frame]: frame and heart-shape '
                                                              'are 4.38301 apart on centerlines '
                                                              'nearest (26.3524, '
                                                              '6.5754)<->(23.1229, 9.53873); SUB32 '
                                                              'requires at least 6 (ink clearance '
                                                              '2) unless the contact is declared '
                                                              'with a scoped `connect` '
                                                              'relationship',
                                                              'mic [slash-upper]: slash-upper and '
                                                              'heart-shape are 0.111958 apart on '
                                                              'centerlines nearest (8, '
                                                              '11)<->(8.10876, 11.0266); SUB32 '
                                                              'requires at least 6 (ink clearance '
                                                              '2) unless the contact is declared '
                                                              'with a scoped `connect` '
                                                              'relationship',
                                                              'mic [slash-lower]: slash-lower and '
                                                              'heart-shape are 3.75281 apart on '
                                                              'centerlines nearest (24, '
                                                              '21)<->(21.1012, 18.6166); SUB32 '
                                                              'requires at least 6 (ink clearance '
                                                              '2) unless the contact is declared '
                                                              'with a scoped `connect` '
                                                              'relationship'],
                                       'variant': 'heart-with-prohibited-circle-sign-v2',
                                       'evidence': 'icon_set/work/side-sub-repairs-2026-09-23/strict32-evidence'}}
