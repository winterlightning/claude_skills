"""Rounded square containing a check, diagonal divider, and cross."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import rounded_rect

SOURCE_ICON_ID = "7dbf66c8-b270-487e-b0d5-155420bf9983"
SOURCE_PATH = "pictographic-primitives/other/rectangle remove and check_7dbf66c8-b270-487e-b0d5-155420bf9983.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "check-and-cross-square"
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/state"
    aliases = ("accept-reject",)
    keywords = ("check", "cross", "yes", "no", "choice")

    def build(self):
        rounded_rect(self, "frame", 2, 2, 30, 30, 4)
        self.add_polyline("check", (7, 11), (10, 15), (15, 7))
        self.add_line("divider", (14, 25), (21, 5))
        self.add_line("cross-a", (22, 20), (27, 25))
        self.add_line("cross-b", (22, 25), (27, 20))
        self.relate("connect", "cross-a", "cross-b")

# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'check-and-cross-square': {'status': 'cannot-fix',
                            'date': '2026-09-23',
                            'author': 'gpt-6',
                            'source_icon_id': '7dbf66c8-b270-487e-b0d5-155420bf9983',
                            'failures_at_review': ['mic [frame]: frame and check are 5 apart on '
                                                   'centerlines nearest (2, 11)<->(7, 11); SUB32 '
                                                   'requires at least 6 (ink clearance 2) unless '
                                                   'the contact is declared with a scoped '
                                                   '`connect` relationship',
                                                   'mic [frame]: frame and divider are 3 apart on '
                                                   'centerlines nearest (21, 2)<->(21, 5); SUB32 '
                                                   'requires at least 6 (ink clearance 2) unless '
                                                   'the contact is declared with a scoped '
                                                   '`connect` relationship',
                                                   'mic [frame]: frame and cross-a are 3 apart on '
                                                   'centerlines nearest (30, 25)<->(27, 25); SUB32 '
                                                   'requires at least 6 (ink clearance 2) unless '
                                                   'the contact is declared with a scoped '
                                                   '`connect` relationship',
                                                   'mic [check]: check and divider are 5.00245 '
                                                   'apart on centerlines nearest (15, '
                                                   '7)<->(19.7216, 8.65256); SUB32 requires at '
                                                   'least 6 (ink clearance 2) unless the contact '
                                                   'is declared with a scoped `connect` '
                                                   'relationship',
                                                   'mic [divider]: divider and cross-a are 5.89911 '
                                                   'apart on centerlines nearest (16.4321, '
                                                   '18.0512)<->(22, 20); SUB32 requires at least 6 '
                                                   '(ink clearance 2) unless the contact is '
                                                   'declared with a scoped `connect` relationship',
                                                   'holes/pinches: 1 undersized holes; 0 pinches'],
                            'blocker': 'The frame, check, divider and X cannot each retain 6px '
                                       'separation inside the 32px square',
                            'attempts': ['Original 32px layout: frame-to-check MIC 5, '
                                         'divider-to-frame 3, and crossed marks crowded',
                                         'Rebalanced 32px layout: check-to-divider and '
                                         'divider-to-X MIC 4.61 (<6)'],
                            'evidence': 'icon_set/work/side-sub-repairs-2026-09-23/strict32-evidence'}}
