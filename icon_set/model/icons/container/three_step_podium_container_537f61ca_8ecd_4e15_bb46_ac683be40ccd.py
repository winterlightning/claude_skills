"""An empty three-block winners podium with the center block tallest and the side blocks lower. Exclude the numeral 1; retain an empty central face for separately composed text.

Plan: Three stepped faces share one baseline; central face is tallest. Centerline bounds (2,10)-(62,54).
Hosting at the standard slot: add-sub32: invalid, heart-state-63: review, check-mark: valid.
Construction reference: Lucide podium: connected step silhouette with independently sized heights.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (three-step-podium-container HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '537f61ca-8ecd-4e15-bb46-ac683be40ccd'
SOURCE_ICON_IDS = ('537f61ca-8ecd-4e15-bb46-ac683be40ccd',)
SOURCE_PATH = 'pictographic-primitives/rating/ranking first_537f61ca-8ecd-4e15-bb46-ac683be40ccd.svg'
AUTHOR = 'claude-opus-5-5'


class ThreeStepPodiumContainer(Container64):
    icon_id = 'three-step-podium-container'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rating'
    categories = ('rating', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('three', 'step', 'podium', 'container')

    def build(self) -> None:
        self.add_line('outline-1', (4, 52), (4, 28))
        self.add_line('outline-2', (4, 28), (21, 28))
        self.add_line('outline-3', (21, 28), (21, 12))
        self.add_line('outline-4', (21, 12), (43, 12))
        self.add_line('outline-5', (43, 12), (43, 34))
        self.add_line('outline-6', (43, 34), (60, 34))
        self.add_line('outline-7', (60, 34), (60, 52))
        self.add_line('outline-8', (60, 52), (4, 52))
        self.add_line('divider-20', (21, 28), (21, 52))
        self.add_line('divider-44', (43, 34), (43, 52))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', closed=True)
        self.relate('connect', 'outline', 'divider-20')
        self.relate('connect', 'outline', 'divider-44')
