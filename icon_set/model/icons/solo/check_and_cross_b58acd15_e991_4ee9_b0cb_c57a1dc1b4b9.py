"""Check and Cross. Retains the identifying silhouette and visible features.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b58acd15-e991-4ee9-b0cb-c57a1dc1b4b9'
SOURCE_PATH = 'pictographic-primitives/symbol/cancel and check_b58acd15-e991-4ee9-b0cb-c57a1dc1b4b9.svg'
AUTHOR = 'gpt-6'


class CheckAndCross(Solo48):
    icon_id = 'check-and-cross'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('check', 'cross', 'yes', 'no', 'approve', 'reject', 'true', 'false')

    def build(self) -> None:
        self.add_polyline('check', (4, 26), (12, 34), (20, 8))
        self.add_polyline('cross-down', (28, 8), (36, 24), (44, 40))
        self.add_polyline('cross-up', (28, 40), (36, 24), (44, 8))
        self.relate("connect", 'cross-down', 'cross-up')
