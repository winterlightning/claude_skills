"""An empty three-block winners podium with the center block tallest and the side blocks lower. Exclude the numeral 1; retain an empty central face for separately composed text.

Plan: Three stepped faces share one baseline; central face is tallest. Centerline bounds (2,10)-(62,54).
Hosting at the standard slot: add-sub32: invalid, heart-state-63: review, check-mark: valid.
Construction reference: Lucide podium: connected step silhouette with independently sized heights."""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '537f61ca-8ecd-4e15-bb46-ac683be40ccd'
SOURCE_PATH = 'pictographic-primitives/rating/ranking first_537f61ca-8ecd-4e15-bb46-ac683be40ccd.svg'
SOURCE_ICON_IDS = ('537f61ca-8ecd-4e15-bb46-ac683be40ccd',)
AUTHOR = 'gpt-6'

class ThreeStepPodiumContainer(Container64):
    icon_id = 'three-step-podium-container'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'containers'
    aliases = ()
    keywords = ('three', 'step', 'podium', 'container')

    def build(self) -> None:
        self.add_polyline('outline',(2,54),(2,28),(20,28),(20,10),(44,10),(44,34),(62,34),(62,54),closed=True)
        for x,top in ((20,28),(44,34)):
            self.add_line(f'divider-{x}',(x,top),(x,54))
            self.relate('connect','outline',f'divider-{x}')
